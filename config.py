from os import getenv
from dotenv import load_dotenv

load_dotenv()

# Get it from my.telegram.org
API_ID = int(getenv("API_ID", "34446649"))
API_HASH = getenv("API_HASH", "8dc570c08d8e35e88fb9bfc73c65d7fa")

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "8967429557:AAHxfH8Ea4FmByOUUpiAtsNh5spg6VUWWqk")

# API By TechZBots || https://t.me/TechZBots
WALL_API = "https://wall.alphacoders.com/api2.0/get.php?auth=17900fc9b6f655f9d9e39a96a256fcd2&method=search&term="

UNSPLASH_API = "https://techzbotsapi.onrender.com/unsplash?query="

MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://Anujedit:Anujedit@cluster0.7cs2nhd.mongodb.net/?appName=Cluster0")
