import webbrowser as web
import time 
import win32com.client as win



shell = win.Dispatch("WScript.Shell")


url = input("Enter the url\t: ")
wait = int(input("Enter the waiting time\t: "))
delay = int(input("Enter delay\t: "))
repeat = int(input("Enter repeat\t: "))

for i in range(0, repeat) :
    time.sleep(delay)
    web.open(url = url)
    time.sleep(wait)
    shell.SendKeys("^w" , 0)