import discord
import time
import os
import requests
import json
import random
import math 


# my_secret = os.environ['TOKEN']

def read_token():
  with open("token.env", "r") as f:
    lines = f.readlines()
    return lines[0].strip()

token = read_token()
client = discord.Client()



def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]["q"] + " -" + json_data[0]["a"]
  return(quote)


@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith("$calc"):
      await message.channel.send('calcualting...')

    if msg.startswith('$hello'):
        await message.channel.send('Hello!')

    if msg.startswith('$inspire'):
      quote = get_quote()
      await message.channel.send(quote)


client.run(token)