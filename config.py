""" Configuration file """
import os
from dotenv import load_dotenv

load_dotenv()

PORT = os.environ.get("PORT", 3000)
BASE_URL = os.environ.get("BASE_URL", 'https://etherscan.io/address')