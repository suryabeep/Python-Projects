# gets the headlines from the New York Times website and writes
# to a file called nyt_titles.txt.
# Also sends the daily titles to my email

import requests
import smtplib
from bs4 import BeautifulSoup
import schedule
import time


def get_titles():
    titles = []
    url = 'http://www.nytimes.com'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    text_file = "nyt_titles.txt"
    for heading in soup.find_all("h2"):
        titles.append(heading.text)
    titles = titles[3: len(titles)-2]
    with open(text_file, 'w') as f:
        for title in titles:
            f.write(title + "\n")
    return titles


def send_mail():
    sender = "suryadippython@gmail.com"
    sender_pw = "pythoniscool@"
    receiver = "sband2000@gmail.com"
    subject = "Today's NYT Headlines"
    body = ''
    titles = get_titles()
    for title in titles:
        body += title + "\n"
    print("Body is: \n{0}".format(body))
    body = "Subject: {}\n\n{}".format(subject, body)
    body = body.encode("utf-8")

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(sender, sender_pw)
    server.sendmail(sender, receiver, body)
    server.close()
    print("\nemail sent!")


schedule.every().day.at("18:17").do(send_mail())

while 1:
    schedule.run_pending()
    time.sleep(86400)



