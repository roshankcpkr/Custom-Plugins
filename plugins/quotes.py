import requests
import json
from userge import userge, Message

@userge.on_cmd("quotes", about={
      'header': "Give random unnecessary quotes",
       'usage': "!quotes "})
async def quotes(message: Message):
                 quote = requests.get('https://api.quotable.io/random')
                 quoteContent = quote.json()['content']
                 quoteAuthor = quote.json()['author']
                 quotess = '' + quoteContent + ' - ' + quoteAuthor
                 await message.edit(quotess)
