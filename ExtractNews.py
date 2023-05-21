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
    cnt = response.content
    soup = BeautifulSoup(cnt, 'html.parser')
    print(soup)
    for i, tag in enumerate(soup.find_all('td', attrs = {'class' : 'title' , 'valign' : ''})) :
        PlaceHolder += ((str(i + 1) + ' :: ' + tag.text + '\n <br>') if tag.text != 'More' else '')
    return PlaceHolder

NewContent = Extract_News('https://news.ycombiantor.com/')
Content += NewContent + '<br>------<br> <br><br> End of Message'
print(Content)