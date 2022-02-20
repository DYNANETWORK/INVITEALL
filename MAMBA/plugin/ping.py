from .. import Mam, Mam2, Mam3, Mam4, Mam5 , Mam6, Mam7, Mam8, Mam9, Mam10, Mam11, Mam12, Mm13, Mam14, Mam15, Mam16, Mam17, Mam18, Mam19, Mam20, SUDO_USERS
from telethon import events
from time import time
from datetime import datetime

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@Mam.on(events.NewMessage(pattern=r"\.ping"))
@Mam2.on(events.NewMessage(pattern=r"\.ping"))
@Mam3.on(events.NewMessage(pattern=r"\.ping"))
@Mam4.on(events.NewMessage(pattern=r"\.ping"))
@Mam5.on(events.NewMessage(pattern=r"\.ping"))
@Mam6.on(events.NewMessage(pattern=r"\.ping"))
@Mam7.on(events.NewMessage(pattern=r"\.ping"))
@Mam8.on(events.NewMessage(pattern=r"\.ping"))
@Mam9.on(events.NewMessage(pattern=r"\.ping"))
@Mam10.on(events.NewMessage(pattern=r"\.ping"))
@Mam11.on(events.NewMessage(pattern=r"\.ping"))
@Mam12.on(events.NewMessage(pattern=r"\.ping"))
@Mam13.on(events.NewMessage(pattern=r"\.ping"))
@Mam14.on(events.NewMessage(pattern=r"\.ping"))
@Mam15.on(events.NewMessage(pattern=r"\.ping"))
@Mam16.on(events.NewMessage(pattern=r"\.ping"))
@Mam17.on(events.NewMessage(pattern=r"\.ping"))
@Mam18.on(events.NewMessage(pattern=r"\.ping"))
@Mam19.on(events.NewMessage(pattern=r"\.ping"))
@Mam20.on(events.NewMessage(pattern=r"\.ping"))
async def ping(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        text = "***Pong!!...***"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"█▀█ █▀█ █▄░█ █▀▀\n█▀▀ █▄█ █░▀█ █▄█\n\nϟ ₘₐₘᵦₐ ₓ ₛₚₐₘ ϟ︎ `{ms}` ᴍs")                       
