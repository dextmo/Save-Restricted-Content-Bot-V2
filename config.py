# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "21727017"))
API_HASH = getenv("API_HASH", "8c9ff17d8d1f6fbe228e5133b011fa99")
BOT_TOKEN = getenv("BOT_TOKEN", "8144843821:AAGXDakJmHJ_1WResbvk1Khoks7ivKpoCYw")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7523868885").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://dexmoer:dex23@dex.nm2sl.mongodb.net/?retryWrites=true&w=majority&appName=dex")
LOG_GROUP = getenv("LOG_GROUP", "-1002343059720")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002343059720"))
