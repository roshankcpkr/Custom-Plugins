import re
import requests
from datetime import datetime  
from datetime import timedelta  
from userge import userge, Message
import nepali_datetime

@userge.on_cmd("date", about={
    'header': "Get date of today, tomorrow or any time",
    'usage': "!t+1 where 1 is date, you can also use t-1 for yesterday"})
async def rashi(message: Message):
         ok = message.input_str
         if (ok.startswith('t+') or ok.startswith('t-'))and len(ok.split(' '))==1:
            if '+' in ok:
                giben=ok.split('+')[1]
                if not giben.isnumeric():
                    await message.edit('invalid argument')
                    return
                try:
                    engdate=(datetime.now() + timedelta(days=int(giben))).strftime("%b %d, %Y")
                    urldate='{d.year}-{d.month}-{d.day}'.format(d=nepali_datetime.datetime.now()+ timedelta(days=int(giben)))
                    nepdate=(nepali_datetime.datetime.now() + timedelta(days=int(giben))).strftime("%D %N %K, %G")
                except:
                    await message.edit('large argument')
                    return     
            else:
                giben=ok.split('-')[1]
                if not giben.isnumeric():
                    await message.edit('invalid argument')
                    return
                try:
                    engdate=(datetime.now() - timedelta(days=int(giben))).strftime("%b %d, %Y")
                    urldate='{d.year}-{d.month}-{d.day}'.format(d=nepali_datetime.datetime.now()- timedelta(days=int(giben)))
                    nepdate=(nepali_datetime.datetime.now() - timedelta(days=int(giben))).strftime("%D %N %K, %G")
                except:
                    await message.edit('large argument')
                    return
            rws=requests.get('https://www.hamropatro.com/date/'+urldate).text
            rawtit=rws[rws.find('<title>') + 7 : rws.find('</title>')]
            if rawtit.split(' | ')[1]=='  ':
                await message.edit('Mind your argument!')
                return
            if 'Nepali Calender' in rawtit:
                await message.edit(f"{nepdate}\n{engdate}")
                return
            titis=rawtit.split(' | ')[0]+' | '+rawtit.split(' | ')[1]
            await message.edit(f"🇳🇵{nepdate}\n📄{titis}\n📅{engdate}")
