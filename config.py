#!/usr/bin/env python3


### Importing
from os import environ

### Getting ENvironment Variables
class Config(object):
    BOT_TOKEN = environ.get("BOT_TOKEN", "7609207287:AAHNsu8KgFmicSN0aPIRcJe0DaeVeluV3hk") # Make a bot from https://t.me/BotFather
    
    APP_ID = int(environ.get("API_ID", "24935727")) # Get this value from https://my.telegram.org/apps
    
    API_HASH = environ.get("API_HASH", "3fd33336629324ecd664e9b6894f0909") # Get this value from https://my.telegram.org/apps
    
    OWNER_ID = int(environ.get("OWNER_ID", "7336971189")) # Your(owner's) telegram id
    
    MONGO_STR = environ.get("MONGO_STR", "mongodb+srv://sujay5372222222:sujay5372222222@cluster0000007.fdufm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0000007") # Get from MongoDB Atlas

