import os
import discord
#import random 
#import json
#import time
#import requests
import dotenv


from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN2')

#print(token)
#print("Hello")



client = discord.Client()

client.run(token)