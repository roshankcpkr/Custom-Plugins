import requests
from bs4 import BeautifulSoup
from userge import userge, Message

@userge.on_cmd("rashi", about={
    'header': "Get daily fresh rashifal",
    'usage': "!rashi"})
async def rashi(message: Message):
         csymbol = message.input_str
         symbol = csymbol.lower()
         if symbol == True:
            
                 URL = f"https://www.hamropatro.com/rashifal/daily/{symbol}"
                 page = requests.get(URL)
                 soup = BeautifulSoup(page.content, "html.parser")
                 rashi_div = soup.find_all("div", class_="desc")
                for rashifal in rashi_div:
                    request_rashi = rashifal.find("p")
                    rashivalue = request_rashi.text.strip()
                    await message.edit(csymbol.title() + ': '+ '\n' + rashivalue)
          else:
            await message.edit("Enter correct rasifal gay")
            
@userge.on_cmd("allrashi", about={
    'header': "Get list of rashifal name",
    'usage': "!allrashi"})
async def rashinames(message: Message):         
           rashiname = ['mesh','mithun', 'singha', 'tula', 'dhanu', 'kumbha', 'brish', 'karkat', 'kanya', 'brischik', 'makar', 'meen' ]
           rashi_name = '\t'.join(rashiname)
           await message.edit(rashi_name.title())
