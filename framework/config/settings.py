import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv('BASE_URL')

if not BASE_URL:
    raise RuntimeError("BASE_URL is not set")