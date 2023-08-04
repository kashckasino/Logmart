from GPBot import Stark
from telethon import events, Button

PM_START_TEXT = """
**Hi {}**
I am a bot who works for @ceoprincezahir and can detect spammers in groups can protect groups from then

**Click the below button for getting help menu!**
"""

@Stark.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):

    if event.is_private:
       await event.reply(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.inline("Help And Commands", data="help")],
        [Button.url("LogMart", "https://t.me/LogMartbot")]])
       return

    if event.is_group:
       await event.reply("**Welcome To BigFraudsters**")
       return
