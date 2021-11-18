import requests , json
from userge import userge, Message

@userge.on_cmd("coin", about={
    'header': "Provides coin info",
    'usage': "!coin <symbol>"})
async def coin(message: Message):
                    send = message.input_str
                    symbol = send.lower()
                    try:
                        resp = ((requests.get(f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&symbols={symbol}")).json())[0]
                        await message.edit( f"<b>[Crypto Check]<b>\n<b>Coin Rank: <b><i>#{resp['market_cap_rank']}<i>\n<b>Coin Name: <b><i>{resp['name']}<i>\n<b>Coin Symbol: <b><i>{symbol.upper()}<i>\n<b>Current Price: <b><i>{resp['current_price']}<i>\n<b>Price Change 24hr: <b><i>{resp['price_change_percentage_24h']}%<i>\n<b>Market Cap Change 24hr: <b><i>{resp['market_cap_change_percentage_24h']}%<i>")
                    except IndexError:
                        await message.edit("Sorry we couldn't find the coin")
