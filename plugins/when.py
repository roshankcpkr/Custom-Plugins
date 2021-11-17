import requests
from bs4 import BeautifulSoup
import re
from userge import userge, Message

@userge.on_cmd("when", about={
    'header': "Tell when event is",
    'usage': "!when "})
async def nepevent(message: Message):
          event = message.input_str
          if event == 'tihar':
            event = "bhaai"
          if event == 'exam':
            await message.edit(" Mangsir 28 gatey ho vai padna ja")
          if event == 'iit':
            await message.edit("2078-08-28")
          if event == 'C':
            await message.edit("2078-09-02")
          if event == 'dl':
            await message.edit("2078-09-05")
          if event == 'maths':
            await message.edit("2078-09-08")
          if event == "physics":
            await message.edit("2079-09-11")
          if event == "study":
            await message.edit("Ta pakka fail ho vai. Padna ja Gay")
          URL = "https://english.hamropatro.com/"
          page = requests.get(URL)
          soup = BeautifulSoup(page.content, "html.parser")
          event_div = soup.find_all("div", class_="holidaysWrapper")
          dates = []
          event_limk = []
          for div in event_div:
              links = div.findAll('a')
              for a in links:
                    om = "http://english.hamropatro.com" + a['href'] + ' = ' + a.text 
                    dates.append(om)
                    limk = "http://english.hamropatro.com" + a['href']
                    event_limk.append(limk)
          text = event.title()
          for txt in dates:
            if text in txt:
                var = re.findall("^http.*\w", txt)
                URLL = var[0]
                pages = requests.get(URLL)
                soups = BeautifulSoup(pages.content, "html.parser")
                ourevent = soups.find_all('div', class_="daySectionWrapper")
                ourvalue = []
                for ev in ourevent:
                    even_date = ev.find("span", class_="newDateText").text.strip()
                    request_event = ev.find("spam")
                    event_value = request_event.text.strip()
                    eng_date = ev.find("div", class_="allignCenter").text.strip()

          
                    ourvalue.append('🇳🇵'+ eng_date)
                await message.edit('\n'.join(ourvalue))


   
