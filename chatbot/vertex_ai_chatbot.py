import os

# Define the configuration content
config_content = """
[server]
headless = true

[theme]
base="light"

[layout]
wideMode = true
"""

# Ensure the .streamlit directory exists
os.makedirs('.streamlit', exist_ok=True)

# Write the configuration content to the config.toml file
with open('.streamlit/config.toml', 'w') as config_file:
    config_file.write(config_content)

import uuid
import requests
from dataclasses import dataclass
from subprocess import PIPE, Popen
import streamlit as st
import json
import os
from streamlit.web.server.websocket_headers import _get_websocket_headers
import streamlit.components.v1 as components

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'vertex_ai_creds.json')) as creds_file:
	json_creds = json.load(creds_file)

#### Credentials
agent_id = json_creds["agent_id"]
project_name = json_creds["project_name"]
location = json_creds["location"]

### running in command line for getting "gcloud auth application-default print-access-token"
def cmdline(command):
	process = Popen(
			args=command,
			stdout=PIPE,
			shell=True
	)
	return process.communicate()[0]

def vertex_resp(prompt,session_token):
	try:
		dialogflow_url = f"https://dialogflow.googleapis.com/v3/projects/{project_name}/locations/{location}/agents/{agent_id}/sessions/{session_token}:detectIntent"
		body = {
						"queryInput": {
								"text": {
										"text": prompt
								},
								"languageCode": "en"
						}
				}
		access_token = cmdline("gcloud auth application-default print-access-token").decode("utf-8").replace('\n','')
		headers = {"Authorization": f"Bearer {access_token}"}
		token_internal = requests.get(f"https://cloudresourcemanager.googleapis.com/v3/projects/{project_name}",headers=headers)
		json_response_of_token_interval_for_project_id = token_internal.json()
		if "error" in json_response_of_token_interval_for_project_id:
			return {"success":False,"message":"Please contact support Team to Change Token which is expired. \nHint : gcloud auth application-default print-access-token"}
		proj_id = json_response_of_token_interval_for_project_id["name"].split("/")[-1]
		headers = {"Authorization": f"Bearer {access_token}","x-goog-user-project":proj_id}

		dialogflow_request = requests.post(url=dialogflow_url, data=json.dumps(body),headers=headers)
		if "text" in dialogflow_request.json()["queryResult"]["responseMessages"][0]:
			return {"success":True,"message":dialogflow_request.json()["queryResult"]["responseMessages"][0]["text"]["text"][0]}
		else:
			return {"success":True,"message":dialogflow_request.json()["queryResult"]["match"]["parameters"]["execution_summary"]}
	except Exception as e:
			return {"success":False,"message":"Sorry for the inconvenience caused. Please try Later!. Refreshing your page might solve the 'PROBLEM'."}

@dataclass
class Message:
		actor: str
		payload: str

def on_refresh_method():
	json_creds["session_id"] = str(uuid.uuid4())
	updating_file = open(os.path.join(__location__, 'vertex_ai_creds.json'),'w')
	updating_file.write(json.dumps(json_creds))
	updating_file.close()

USER = "user"
ASSISTANT = "ai"
MESSAGES = "messages"
COPIED_MESSAGES = "copied_conversation"

st.set_page_config(layout="wide")

if MESSAGES not in st.session_state:
		st.session_state[MESSAGES] = [Message(actor=ASSISTANT, payload="Hi! How can I help you?")]
		st.session_state[COPIED_MESSAGES] = [{ASSISTANT:"Hi! How can I help you?"}]
msg: Message

# import time

# with st.empty():
#     for seconds in range(60):
#         st.write(f"⏳ {seconds} seconds have passed")
#         time.sleep(1)
#     st.write("✔️ 1 minute over!")
if 'input_disabled' not in st.session_state:
    st.session_state.input_disabled = True

if 'refresh_flag' not in st.session_state:
	st.session_state['refresh_flag'] = True
	on_refresh_method()

def process_session_token():
	'''
	WARNING: We use unsupported features of Streamlit
			 However, this is quite fast and works well with
			 the latest version of Streamlit (1.27)
			 Also, this does not verify the session token's
			 authenticity. It only decodes the token.
	'''
	headers = _get_websocket_headers()
	host_and_session = str(headers["Host"].split(":")[-1]) + str(headers["Sec-Websocket-Key"])
	if "Sec-Websocket-Key" in headers:
		return {"success":True,"message":host_and_session}
	else:
		return {"success":False,"message":"Sorry for the inconvenience. Internal Server Error Near streamlit. Please Try Later.."}

session_token = process_session_token()
if session_token["success"] == False:
	st.error("Sorry for the inconvenience.... Please Try Later. Refreshing your page might solve the 'PROBLEM'.")
	st.stop()

session_token = session_token["message"]

for msg in st.session_state[MESSAGES]:
	st.chat_message(msg.actor).write(msg.payload)

if "disabled" not in st.session_state:
	st.session_state["disabled"] = False

def disable_chat_input():
	st.session_state["disabled"] = True

def enable_chat_input():
    st.session_state["disabled"] = False


# Define custom CSS to change the chat input color when disabled
custom_css = """
<style>
    .disabled-input {
        background-color: #f0f0f0 !important; /* Change to your desired color */
        color: #888 !important;
    }
</style>
"""

# Inject custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Check if the input should be disabled and apply the custom CSS class
disabled_class = "disabled-input" if st.session_state["disabled"] else ""

if prompt:= st.chat_input("How may I help you?",disabled=st.session_state.disabled,on_submit=disable_chat_input):
	st.session_state[MESSAGES].append(Message(actor=USER, payload=prompt))
	st.session_state[COPIED_MESSAGES].append({USER:prompt})
	st.chat_message(USER).write(prompt)
	
	with st.spinner('Generating...'):
		answer_is = vertex_resp(prompt,session_token)
		if not answer_is["success"]:
			st.error(answer_is["message"])
			st.stop()
		st.chat_message(ASSISTANT).write(answer_is["message"])
		st.session_state[MESSAGES].append(Message(actor=ASSISTANT, payload=answer_is["message"]))
		st.session_state[COPIED_MESSAGES].append({ASSISTANT:answer_is["message"]})
	enable_chat_input()
	st.rerun()
entire_conversation = str(st.session_state[COPIED_MESSAGES])
entire_conversation = '%s' % json.dumps(entire_conversation)

css = """<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/toastr.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/remixicon/fonts/remixicon.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/toastr.min.js"></script>
<style>
    #toast-container > div {
        background-color: black !important;
        color: white !important;
        padding: 15px 10px 10px 40px !important;
        font-size: 14px !important;
        min-height: auto !important;
        border-radius: 2px !important;
        box-shadow: none !important;
        width: 100px !important;
    }
    .toast-top-right {
        top: 60px; /* Adjust this value to move it further down */
        right: 12px;
    }
</style>
<br>
<button style="font-size:24px;border: solid 1px white;border-radius: 4px;background: white;float: inline-end;
    cursor: pointer;" onclick="copyToClipboard()"><i class="ri-file-copy-line"></i></button>
<script>
    function copyToClipboard() {
        var textToCopy = """ + f'''{entire_conversation}''' + """
        var tempInput = document.createElement('input');
        tempInput.value = textToCopy;
        document.body.appendChild(tempInput);
        tempInput.select();
        document.execCommand('copy');
        document.body.removeChild(tempInput);
		toastr.success('Copied');
    }
</script>
"""
components.html(css, height=100)
