from dotenv import load_dotenv
import os


load_dotenv()

HOST = '0.0.0.0'
PORT = 6262
SERVER_IP = os.getenv('SERVER_IP')