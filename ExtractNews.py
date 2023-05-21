import requests
import smtplib
import datetime

from bs4 import BeautifulSoup 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



TimeNow = datetime.datetime.now()

Content = ''


def Extract_News(url) :
    print("Extracting News")
    PlaceHolder = '<b>Hacker News Top Stories : </b> \n <bR>' + '-'*50 + '<br>'
    response = requests.get(url = url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for i, tag in enumerate(soup.find_all('td', attrs = {'class' : 'title' , 'valign' : ''}), start = 1) :
        PlaceHolder += ((str(i) + ' :: ' + tag.text + '\n <br>') if tag.text != 'More' else '')
    return PlaceHolder

NewContent = Extract_News('https://news.ycombinator.com/')
Content += NewContent + '<br>------<br> <br><br> End of Message'


print("Composing Email")


ServerName = 'smtp.gmail.com'
Port = 587
From = ''
To = ''
Password = ''

Message = MIMEMultipart()

Message['Subject'] = 'Top Stories today ' + str(TimeNow.day) + '-' + str(TimeNow.month) + '-' + str(TimeNow.year)
Message['From'] = From
Message['To'] = To
print(Password)

Message.attach(MIMEText(Content, 'html'))

print("Initializing server")

Server = smtplib.SMTP(ServerName, Port)

try :
    Server.set_debuglevel(0)
    Server.ehlo()
    Server.starttls()
    Server.login(From, Password)
    Server.sendmail(From , To , Message.as_string())
    print("Email Sent")
except : 
    print("Error")
    print("Email not sent")

Server.quit()