import webbrowser as web
import time
import win32com.client as win


shell = win.Dispatch("WScript.Shell")


url = "gmail.com"
email = "e08726702@gmail.com"
subject = "Scripting"
content = "Successfully Executed the Script"

web.open(url = url)
time.sleep(10)
shell.SendKeys("c" , 0)
time.sleep(1)
shell.SendKeys(email, 0)
time.sleep(1)
shell.SendKeys("{Tab}" , 0)
time.sleep(1)
shell.SendKeys("{Tab}" , 0)
time.sleep(1)
shell.SendKeys(subject, 0)
time.sleep(1)
shell.SendKeys("{Tab}" , 0)
time.sleep(1)
shell.SendKeys(content, 0)
time.sleep(1)
shell.SendKeys("{Tab}" , 0)
time.sleep(1)
shell.SendKeys("{Enter}" , 0)