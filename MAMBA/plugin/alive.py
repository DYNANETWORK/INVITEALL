from .. import Mam, SUDO_USERS
from .. import ALIVE_PIC
from telethon import events
from time import time
from datetime import datetime

MAM_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/a8a793a8716bdcc923fd3.jpg"
  

          
mamba = "✧ 𝑀𝐴𝑀𝐵𝐴 𝑆𝑃𝐴𝑀 𝐼𝑍𝑍 𝐴𝐿𝐼𝑉𝐸𝐸 ✧\n\n"

mamba += f"┏━━━━━━━━━━━━━━━━━━━\n"

mamba += f"┣➣ **ᴘʏᴛʜᴏɴ ** : `3.9.6`\n"

mamba += f"┣➣ **DEVELOPER** : `{🇲🇦🇲🇧🇦}`\n"

mamba += f"┣➣ **🇴🇼🇳🇪🇷**  : `[BLACK MAMBA]{https://t.me/BLACKMAMBA_OFFICIAL}`\n"
    
mamba += f"┣➣ **sᴜᴘᴘᴏʀᴛ** : [JOIN](https://t.me/MAMBA_X_SUPPORT)\n"

mamba += f"┣➣ **ᴄʜᴀɴɴᴇʟ** : [JOIN](https://t.me/MAMBA_NETWORK)\n"

mamba += f"┗━━━━━━━━━━━━━━━━━━━\n\n"

mamba += f"🖤 [𝐑𝐄𝐏𝐎](https://github.com/SUKHPAL443/INVITEALL) 🖤"            
                                    
@Mam.on(events.NewMessage(pattern=r"\.alive"))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Mam.send_file(event.chat_id,
                                  MAM_PIC,
                                  caption=mamba)
    
