import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQAf70YAFIU3HtYDOEB7LB0HxpdrywbHlUgTmAHuRB0VNXSS8rK_d6cqlfT28fivwI5lhWTS90e0TUISzDc4-eTvUJ131SCB6pYAB2xCRaRf3q7wfE_7CojzJVOrmihlZtEh1RvCQn1qrsk2-rUFFvrdOgwz-QJaxKdV770fbslIyAm5nuoUN8E1ifSXhLkPiXVw6yHgPh9K3Yhgrfwp-eKocpDQewygCGqaa4J1k1CjmiJZco5_QNkGgraNcHqylwzAkbeDAkJnzKDC_11CmO3Qw8QT5IeP6hRl1vRJQsiPKXL6_Qdr1q3YtW1wVDzOHYCeiEVfjVRbNQQAn8Nw6P9kflOGGAAAAAGvBT3TAA")
BOT_TOKEN = getenv("7957710052:AAEf5KfaQ22yM_jZj4Vxztj9bbE0lcmMNO0")
BOT_NAME = getenv("BOT_NAME", "ＮＩＣＫ ꭙ ＭＵＳＩＣ 👻")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/6790864f5fe27471bdc8d.png")
THUMB_IMG = getenv("THUMB_IMG", "https://graph.org/file/e645d6cc03374098848c6-85c88511cd33000c96.jpg")
AUD_IMG = getenv("AUD_IMG", "https://graph.org/file/e645d6cc03374098848c6-85c88511cd33000c96.jpg")
QUE_IMG = getenv("QUE_IMG", "https://graph.org/file/e645d6cc03374098848c6-85c88511cd33000c96.jpg")
API_ID = int(getenv("26212996"))
API_HASH = getenv("76221d523a4eff99bcbb43332fe7f8fa")
BOT_USERNAME = getenv("BOT_USERNAME", "NickXmusicBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "⎯᪵⎯꯭꯭᪵̽᪳𐎓⃝꯭꯭꯭💭꯭ ⃪ ⃪꯭𝑫𝑬𝑨𝑻𝑯 𝑵𝑶𝑻𝑬 💸꯭ ꯭͓᪳᪼𝆺꯭꯭꯭𝅥𝆭͢࿐ ...𓆩⃟🦅")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Westbengalnetwork")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Westbengalnetworkchat")
OWNER_NAME = getenv("OWNER_NAME", "ＮＩＣＫ") # isi dengan username kamu tanpa simbol @
PMPERMIT = getenv("PMPERMIT", None)
OWNER_ID = int(os.environ.get("7231323603")) # fill with your id as the owner of the bot
DATABASE_URL = os.environ.get("mongodb+srv://mrnasib21:mrnasib21@cluster0.s4hrn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # fill with your mongodb url
LOG_CHANNEL = int(os.environ.get("-1002332259315")) # make a private channel and get the channel id
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False)) # just fill with True or False (optional)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
LANG = getenv("LANG", "id")
