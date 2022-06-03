import datetime
import logging
import os

from dotenv import load_dotenv

load_dotenv()

# Logging
if not os.getenv("DEBUG", default=False):
    formatter = '[%(asctime)s] %(levelname)8s --- %(message)s (%(filename)s:%(lineno)s)'
    logging.basicConfig(
        filename=f'logs/bot-from-{datetime.datetime.now().date()}.log',
        filemode='w',
        format=formatter,
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.WARNING
    )

# Telegram client configs
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
api_tg_session_name = os.getenv("TG_CLIENT_SESSION_NAME", default='anon')

# DB configs
MONGO_URL = os.getenv("MONGO_URL", default="mongodb://localhost:27017/tgparser")
