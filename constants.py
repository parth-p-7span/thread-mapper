import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')
CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')
BEARER_TOKEN = os.environ.get('BEARER_TOKEN')
TWITTER_BOT_ID = int(os.environ.get('TWITTER_BOT_ID'))
BASE_URL = 'https://discordapp.com/api/channels'

DISCORD_HEADER = {
    "Authorization": "Bot {}".format(BOT_TOKEN),
    "User-Agent": "myBotThing (http://some.url, v0.1)",
    "Content-Type": "application/json"
}
DISCORD_CHANNEL = 1030345467554435084
