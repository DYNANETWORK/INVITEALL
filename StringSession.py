from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print(
    """
╔═╗╔═╦═══╦═╗╔═╦══╗╔═══╦═══╦═══╦═══╦═╗╔═╗
║║╚╝║║╔═╗║║╚╝║║╔╗║║╔═╗║╔═╗║╔═╗║╔═╗║║╚╝║║
║╔╗╔╗║║─║║╔╗╔╗║╚╝╚╣║─║║╚══╣╚═╝║║─║║╔╗╔╗║
║║║║║║╚═╝║║║║║║╔═╗║╚═╝╠══╗║╔══╣╚═╝║║║║║║
║║║║║║╔═╗║║║║║║╚═╝║╔═╗║╚═╝║║──║╔═╗║║║║║║
╚╝╚╝╚╩╝─╚╩╝╚╝╚╩═══╩╝─╚╩═══╩╝──╚╝─╚╩╝╚╝╚╝"""
)

print("\n • Telethon Session •")

print("""\nTHIS SESSION FILE MADE BY @SUKHPAL_KHERERA WITH LOT'S OF 💖\n""")

MAMBAX = input("Enter 'y' Or 'yes' To Continue: ")

if MAMBAX == "y" or "yes": 
    print("\n• Please go to my.telegram.org and get your API Id and API Hash to proceed")
    print("""\n• Enter Your Valid Details To Continue!\n\n""")

api_id = int(input("Enter API ID: "))

api_hash = input("Enter API HASH: ")

try:
    with TelegramClient(StringSession(), api_id, api_hash) as client:
        MAMBAXSPAM = client.session.save()
        client.send_message("me", f"**MAMBA XSPAM Session Given Below :**\n\n`{MAMBAXSPAM}` \n\n__Do not share this anywhere!!__")
        print(
             f"\n\nSTRING SESSION GENERATE SUCCESSFULLY CHECK SAVED MASSAGE IF ANY PROBLEM CONTACT @MAMBA_X_SUPPORT")
except Exception as e:
    print(f"{e}")
