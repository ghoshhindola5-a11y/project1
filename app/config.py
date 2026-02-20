import os
from dotenv import load_dotenv

load_dotenv()

SCALEDOWN_API_KEY = os.getenv("SCALEDOWN_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")
FRONTEND_URL = os.getenv("FRONTEND_URL")

