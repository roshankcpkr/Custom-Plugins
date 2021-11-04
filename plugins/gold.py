import requests
from bs4 import BeautifulSoup
from userge import userge, Message

@userge.on_cmd("gold", about={
      'header': "Gives Gold and silver price",
       'usage': "!gold "})
async def gold(message:Message):
          prices = []
          URL = "https://english.hamropatro.com/gold"
          page = requests.get(URL)
          soup = BeautifulSoup(page.content, "html.parser")
          gold_column = soup.find("div", class_="column6")
          list = gold_column.find_all("li")
          for li in list:
            val = li.text.strip()
            prices.append(val)

          await message.edit(f"🌕[Today's Gold and silver price]⚪️\n{prices[0]} = {prices[1]}\n{prices[2]} = {prices[3]}\n{prices[4]} = {prices[5]}\n{prices[6]} = {prices[7]}\n{prices[8]} = {prices[9]}\n{prices[10]} = {prices[11]}"
          )
