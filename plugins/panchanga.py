from userge import userge, Message
from bs4 import BeautifulSoup
import requests
from tabulate import tabulate

@userge.on_cmd("panchanga", about={
    'header': "Get panchanga ",
    'usage': "!panchanga"})
def panchanga(message:Message):
            data = []
            titleData=[]
            informationData = []
            i = 0
            col_names = ["Title", "Information"]
            URL = "https://www.ashesh.com.np/panchang/widget.php?"
            r = requests.get(URL)
            html_document = r.content
            soup = BeautifulSoup(html_document, 'html.parser')
            eventDiv = soup.find("div", class_="event")
            titles = eventDiv.find_all("div", class_="ev_left")
            information = eventDiv.find_all("div", class_="ev_right")
            for t in titles:
                titleData.append(t.text)
            for i in information:
                informationData.append(i.text)
            for i in range(len(titleData)):
                data.append([titleData[i], informationData[i]])
            print(tabulate(data, headers=col_names))