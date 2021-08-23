import requests
import json
from userge import userge, Message

@userge.on_cmd("memes", about={
    'header': "Get memes ",
    'usage': "!memes"})
async def meme(message:Message):
	      memeget = requests.get('https://meme-api.herokuapp.com/gimme')
	      memeSent = memeget.json()['url']
	      memeMsg = '' + memeSent
	      await message.edit(memeMsg)
