import requests
from bs4 import BeautifulSoup
from userge import userge, Message

@userge.on_cmd("td", about={
    'header': "Tell present nepali date",
    'usage': "!td"})
async def nepdate(message: Message):
                 nefoli = []
                 URL = "https://english.hamropatro.com/"
                 page = requests.get(URL)
                 soup = BeautifulSoup(page.content, "html.parser")
                 time_div = soup.find_all("div", class_ = "time")
                 date_div = soup.find_all("div", class_ = "logo")
        
                 for date in date_div:
                     request_date = date.findAll("div")
                     datevalue = request_date[0].text.strip()
                     eventvalue = '📄 ' + request_date[1].text.strip() + "\n" +request_date[2].text.strip()           
                     nefoli.append(f"🇳🇵 {datevalue}")
                     nefoli.append(eventvalue)
                     break;
                 for time in time_div:
                     request_time = time.find("span")
                     engdate = time.find("span", class_ = "eng")
                     timevalue = '🕒 ' + request_time.text.strip() + "\n" + '📅 ' +engdate.text.strip()
                     nefoli.append(timevalue)
                     break;
                 todaynefol = '\n'.join(nefoli)
                 await message.edit(todaynefol)
