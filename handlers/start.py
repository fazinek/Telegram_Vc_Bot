from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command(["start", "start@Ek_Music_play_Bot"]) & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        text="**Hello 👋🏻 {}!**I Am Music Play Bot. I Can Play Musics In Voice Chats.\n\nHit /help For Get Command List\nPlease Add Me To See My Wonderful Features.\n\n\nJOIN @EKBOTZ_UPDATE**".format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("➕ Add To Your Group ➕", url="https://t.me/Ek_Music_play_Bot?startgroup=true")
            ],[
            InlineKeyboardButton("Report Bug ⚜️", url="https://t.me/ekbotz_support"),
            InlineKeyboardButton("Channel 🔰", url="https://t.me/EKBOTZ_UPDATE")
            ],[
            InlineKeyboardButton("Commands 🛠", url="help"),
            ]]
        ),
        disable_web_page_preview=True
    )

@Client.on_message(filters.command(["start", "start@Ek_Music_play_Bot"]) & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text(
          text="**I Am Alive\nJoin @EKBOTZ_UPDATE**",
          reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text="🎙️ Support Group 🎙️", url="https://t.me/EKBOTZ_SUPPORT")
              ]]
          )
      )


@Client.on_message(filters.command(["help", "start@Ek_Music_play_Bot"]) & filters.private & ~filters.channel)
async def cmdlist(_, message: Message):
    await message.reply_text(
        text="""**Ek_Music_play_Bot : Help Menu**

__• First Add Me To Your Group..
• Promote Me As Admin In Your Group With All Permission..__

**🏷 Common Commands.**

• `/play` - Song Name : __Plays Via Youtube__
• `/dplay` - Song Name : __Play Via Deezer__
• `/splay` - Song Name : __Play Via Jio Saavn__
• `/playlist` - __Show current playing list__
• `/current` - __Show current playing__

• `/song` - Song Name : __Get The Song From YouTube__
• `/vid` - Video Name : __Get The Video From YouTube__
• `/deezer` - song name : __download songs you want quickly via deezer__
• `/saavn` - song name : __download songs you want quickly via saavn__
• `/search` - YouTube Title : __(Get YouTube Search Query)__

**🏷 Group Admin Commands.**

• `/skip` : __Skips Music__
• `/pause` : __Pause Playing Music__
• `/resume` : __Resume Playing Music__
• `/end` : __Stops playing Music__
• `/reload` : __Reloads Admin List__
• `/userbotjoin` : __Assistant Joins The Group__
• `/userbotleave` : __Assistant Leaves From The Group.__""",
        reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text="⚜️ CHANNEL", url="https://t.me/EKBOTZ_UPDATE")
              ]]
          )
      )

HELP_TEXT ="""
**Ek_Music_play_Bot : Help Menu**

__• First Add Me To Your Group..
• Promote Me As Admin In Your Group With All Permission..__

**🏷 Common Commands.**

• `/play` - Song Name : __Plays Via Youtube__
• `/dplay` - Song Name : __Play Via Deezer__
• `/splay` - Song Name : __Play Via Jio Saavn__
• `/playlist` - __Show current playing list__
• `/current` - __Show current playing__

• `/song` - Song Name : __Get The Song From YouTube__
• `/vid` - Video Name : __Get The Video From YouTube__
• `/deezer` - song name : __download songs you want quickly via deezer__
• `/saavn` - song name : __download songs you want quickly via saavn__
• `/search` - YouTube Title : __(Get YouTube Search Query)__

**🏷 Group Admin Commands.**

• `/skip` : __Skips Music__
• `/pause` : __Pause Playing Music__
• `/resume` : __Resume Playing Music__
• `/end` : __Stops playing Music__
• `/reload` : __Reloads Admin List__
• `/userbotjoin` : __Assistant Joins The Group__
• `/userbotleave` : __Assistant Leaves From The Group.__
"""
HELP_BUTTON = InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text="⚜️ CHANNEL", url="https://t.me/EKBOTZ_UPDATE")
              ]]
          )
@Client.on_callback_query()
async def cb_handler(bot, update):
    if update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            reply_markup=HELP_BUTTONS,
            disable_web_page_preview=True
        )

