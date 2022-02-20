import os

class Var(object):
    APP_ID = int(os.environ.get("APP_ID", 6))
    API_HASH = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
    ALIVE_PIC = os.environ.get("ALIVE_PIC", "https://telegra.ph/file/a8a793a8716bdcc923fd3.jpg")
    STRING = os.environ.get("STRING", None)
    STRING2 = os.environ.get("STRING2", None)
    STRING3 = os.environ.get("STRING3", None)
    STRING4 = os.environ.get("STRING4", None)
    STRING5 = os.environ.get("STRING5", None)
    STRING6 = os.environ.get("STRING6", None)
    STRING7 = os.environ.get("STRING7", None)
    STRING8 = os.environ.get("STRING8", None)
    STRING9 = os.environ.get("STRING9", None)
    STRING10 = os.environ.get("STRING10", None)
    STRING11 = os.environ.get("STRING11", None)
    STRING12 = os.environ.get("STRING12", None)
    STRING13 = os.environ.get("STRING13", None)
    STRING14 = os.environ.get("STRING14", None)
    STRING15 = os.environ.get("STRING15", None)
    STRING16 = os.environ.get("STRING16", None)
    STRING17 = os.environ.get("STRING17", None)
    STRING18 = os.environ.get("STRING18", None)
    STRING19 = os.environ.get("STRING19", None)
    STRING20 = os.environ.get("STRING20", None)
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "1234567890").split())
    

class Development(Var):
    LOGGER = True
