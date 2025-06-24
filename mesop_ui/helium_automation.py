# helium_automation.py
from helium import start_chrome, click, write, press, kill_browser, go_to, CONTROL, ENTER, TAB

start_chrome()
go_to("https://facebook.com/")
write("lakshmanlucky786")
press(TAB)
write("password")
press(ENTER)

# click('Python.org')
# kill_browser()