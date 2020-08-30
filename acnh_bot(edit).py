## August 30th - unfinished

from discord.ext.commands import Bot
import json
import requests

BOT_PREFIX = ("?", "!")
TOKEN = XXXXXXXXXXXX # replace with your own discord bot token
client = Bot(command_prefix=BOT_PREFIX)

fish_url = "https://acnhapi.com/v1/fish/"
fish_response = requests.get(fish_url)

bugs_url = "http://acnhapi.com/v1/bugs/"
bugs_response = requests.get(bugs_url)

art_url = "http://acnhapi.com/v1/art/"
art_response = requests.get(art_url)

songs_url = "http://acnhapi.com/v1/songs/"
songs_response = requests.get(songs_url)


# type command !fish 'fish-name' 
@client.command(pass_context=True,
                description = "ACNH fish info")
async def fish(ctx, n):
    name = fish_response.json() [n]["name"]["name-USen"]
    price = fish_response.json() [n]["price"]
    p = str(price)
    #image = response.json() [n]["image_uri"]
    location = fish_response.json() [n]["availability"]["location"]
    rarity = fish_response.json() [n]["availability"]["rarity"]
    
        await ctx.send("Name: " + name.upper() + "\nPrice: " + p + " Bells \nLocation: " + location + " \nRarity: " + rarity)

# type command !bug 'bug-name' 
@client.command(pass_context=True,
                description = "ACNH bug info")
async def bug(ctx, n):
    name = bugs_response.json() [n]["name"]["name-USen"]
    price = bugs_response.json() [n]["price"]
    p = str(price)
    #image = response.json() [n]["image_uri"]
    location = bugs_response.json() [n]["availability"]["location"]
    rarity = bugs_response.json() [n]["availability"]["rarity"]
    
    await ctx.send("Name: " + name.upper() + "\nPrice: " + p + " Bells \nLocation: " + location + " \nRarity: " + rarity)


# type command !art 'art-name' 
@client.command(pass_context=True,
                description = "ACNH art info")
async def art(ctx, n):
    name = art_response.json() [n]["name"]["name-USen"]
    price = art_response.json() [n]["buy-price"]
    p = str(price)
    #image = response.json() [n]["image_uri"]
    hasfake = str(art_response.json() [n]["hasFake"])
    image = art_response.json() [n]["image_uri"]
    
    await ctx.send("Name: " + name.upper() + "\nPrice: " + p + " Bells \nHas Fake?: " + hasfake + " \n " + image)

# type command !play 'song-name' 
@client.command(pass_context=True,
                description = "ACNH songs")
async def play(ctx, n):
    name = songs_response.json() [n]["name"]["name-USen"]
    price = songs_response.json() [n]["buy-price"]
    p = str(price)
    music = songs_response.json() [n]["music_uri"]
    
    await ctx.send("Name: " + name.upper() + "\nPrice: " + p + " Bells \n" + music)


client.run(TOKEN)
