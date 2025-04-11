import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "23864777")

API_HASH = os.environ.get("API_HASH", "1ad9abca4b87cee505e4ed3b1a811665")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7769997460:AAGote37S-jOib2dSDc3PU-FRu0TBYb-YDg") 

FORCE_SUB = os.environ.get("FORCE_SUB", "S_MovieChannel") 

DB_NAME = os.environ.get("DB_NAME","STRenameBot")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://STRenameBot:STRenameBot@cluster0.p7bubb0.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://envs.sh/5vH.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6509218702').split()]

PORT = os.environ.get("PORT", "8080")
