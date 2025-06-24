def detect_intent_texts(project_id, session_id, texts, language_code):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation."""
    from google.cloud import dialogflow

    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print("Session path: {}\n".format(session))

    for text in texts:
        text_input = dialogflow.TextInput(text=text, language_code=language_code)

        query_input = dialogflow.QueryInput(text=text_input)

        response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )

        print("=" * 20)
        print("Query text: {}".format(response.query_result.query_text))
        print(
            "Detected intent: {} (confidence: {})\n".format(
                response.query_result.intent.display_name,
                response.query_result.intent_detection_confidence,
            )
        )
        print("Fulfillment text: {}\n".format(response.query_result.fulfillment_text))

# import uuid
# project_id="veertex-clbs"
# agent_id="2e805113-f846-4687-83ef-5cedec1ec8c3"
# language_code="en"
# session_id = uuid.uuid4()
# detect_intent_texts(project_id,session_id,"whats the buffet timmings?",language_code)
# url = "https://dialogflow.cloud.google.com/v1/cx/integrations/messenger/webhook/projects/veertex-clbs/agents/2e805113-f846-4687-83ef-5cedec1ec8c3/sessions/dfMessenger-bcfa651b-ee91-4b0d-9fee-fb27e64c0fc8"
# payload = {"queryInput": {"text": {"text": "wts buffet timmings?"}, "languageCode": "en"}},{"queryParams": {"channel": "DF_MESSENGER"}}
# import requests
# integrations_url = "https://dialogflow.clients6.google.com/v3alpha1/projects/veertex-clbs/locations/global/agents/2e805113-f846-4687-83ef-5cedec1ec8c3/integrations:start?alt=json&key=AIzaSyD1dO8oRagJkmtkSJ9oLI289jIT8M4Zk5s"
# # "Authorization": f"Bearer AIzaSyD1dO8oRagJkmtkSJ9oLI289jIT8M4Zk5s"
# response = requests.post(integrations_url)
# print(response.json,">"*100)