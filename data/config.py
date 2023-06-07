import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

admins = [
    444980141
]

ip = os.getenv('ip')
PGUSER = str(os.getenv('PGUSER'))
PGPASS = str(os.getenv('PGPASS'))
DATABASE = str(os.getenv('DATABASE'))

POSTGRES_URI = f'postgresql://{PGUSER}:{PGPASS}@{ip}/{DATABASE}'
