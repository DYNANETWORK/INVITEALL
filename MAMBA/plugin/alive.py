from .. import Mam, SUDO_USERS
from .. import ALIVE_PIC
from telethon import events
from time import time
from datetime import datetime

MAM_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/a8a793a8716bdcc923fd3.jpg"
  

          
mamba = "β§ ππ΄ππ΅π΄ πππ΄π πΌππ π΄πΏπΌππΈπΈ β§\n\n"

mamba += f"ββββββββββββββββββββ\n"

mamba += f"β£β£ **α΄Κα΄Κα΄Ι΄ ** : `3.9.6`\n"

mamba += f"β£β£ **DEVELOPER** : `{π²π¦π²π§π¦}`\n"

mamba += f"β£β£ **π΄πΌπ³πͺπ·**  : `[BLACK MAMBA]{https://t.me/BLACKMAMBA_OFFICIAL}`\n"
    
mamba += f"β£β£ **sα΄α΄α΄α΄Κα΄** : [JOIN](https://t.me/MAMBA_X_SUPPORT)\n"

mamba += f"β£β£ **α΄Κα΄Ι΄Ι΄α΄Κ** : [JOIN](https://t.me/MAMBA_NETWORK)\n"

mamba += f"ββββββββββββββββββββ\n\n"

mamba += f"π€ [ππππ](https://github.com/SUKHPAL443/INVITEALL) π€"            
                                    
@Mam.on(events.NewMessage(pattern=r"\.alive"))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Mam.send_file(event.chat_id,
                                  MAM_PIC,
                                  caption=mamba)
    
