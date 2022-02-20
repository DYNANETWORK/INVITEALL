#MAMBA_NETWORK

import asyncio
import sys
from sys import argv
import glob
from pathlib import Path
from MAMBA.utils import load_plugins
import logging
from telethon import events
from MAMBA import Mam, Mam2, Mam3, Mam4, Mam5 , Mam6, Mam7, Mam8, Mam9, Mam10, Mam11, Mam12, Mam13, Mam14, Mam15, Mam16, Mam17, Mam18, Mam19, Mam20

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


path = "MAMBA/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("INVITEALL BOT SUCCESSFULLY DEPLOYED-!")
print("ENJOY!!!!! THIS BOT IS FULLY DEVELOPED BY @MAMBA_NETWORK")

if len(argv) not in (1, 3, 4):
    try:
        Mam.disconnect()
    except Exception as e:
        pass
    try:
        Mam2.disconnect()
    except Exception as e:
        pass
    try:
        Mam3.disconnect()
    except Exception as e:
        pass
    try:
        Mam4.disconnect()
    except Exception as e:
        pass
    try:
        Mam5.disconnect()
    except Exception as e:
        pass
    try:
        Mam6.disconnect()
    except Exception as e:
        pass
    try:
        Mam7.disconnect()
    except Exception as e:
        pass
    try:
        Mam8.disconnect()
    except Exception as e:
        pass
    try:
        Mam9.disconnect()
    except Exception as e:
        pass
    try:
        Mam10.disconnect()
    except Exception as e:
        pass
    try:
        Mam11.disconnect()
    except Exception as e:
        pass
    try:
        Mam12.disconnect()
    except Exception as e:
        pass
    try:
        Mam13.disconnect()
    except Exception as e:
        pass
    try:
        Mam14.disconnect()
    except Exception as e:
        pass
    try:
        Mam15.disconnect()
    except Exception as e:
        pass
    try:
        Mam16.disconnect()
    except Exception as e:
        pass
    try:
        Mam17.disconnect()
    except Exception as e:
        pass
    try:
        Mam18.disconnect()
    except Exception as e:
        pass
    try:
        Mam19.disconnect()
    except Exception as e:
        pass
    try:
        Mam20.disconnect()
    except Exception as e:
        pass
else:
    try:
        Mam.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mam2.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mam3.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mam4.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mam5.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mam6.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mam7.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mam8.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mam9.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mam10.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mam11.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mam12.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mam13.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mam14.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mam15.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mam16.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mam17.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mam18.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mam19.run_until_disconnected()
    except Exception as e:
        pass
    try:
        Mam20.run_until_disconnected()
    except Exception as e:
        pass
