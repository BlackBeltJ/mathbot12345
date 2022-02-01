import os
import discord
import random 
import json
import time
import requests
# import math 
from dotenv import load_dotenv


load_dotenv()
token = os.getenv('TOKEN')

#print(token)
#print("Hello")


client = discord.Client()


@client.event
 async def on_ready():
     print("We have logged in as {0.user}".format(client))


client.run(token)