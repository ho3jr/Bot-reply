from pyrogram import Client, filters
from pyrogram.types import Message
import pyromod
from datetime import datetime

api_id = 11111111
api_hash = " "
token= " "

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=token
)

sent = False

@app.on_message(filters.private)
async def ADMINS(c: Client, m: Message):

    if m.text == "/ping" or m.text == "Ping":
        start_t = datetime.now()
        await app.send_message(m.chat.id,"Pong!")
        end_t = datetime.now()
        time_taken_s = (end_t - start_t).microseconds / 1000
        await app.send_message(m.chat.id,f"Ping Pong Speed\n{time_taken_s} milli-seconds")

    async def get_chat_member_status():     #get chat member status in group
        try:
            status_member = await app.get_chat_member("Send_Information_Media",m.from_user.id)
            status_member = str(status_member.status)
            status_member = status_member.split(".")[1]
            return(status_member)
        except:
            status_member = "negative"
            return(status_member)
        
    if m.text == "/start":
       await app.send_message(m.chat.id, "سلام فسقلی شیطون من! خوبی قشنگم؟😂❤️ \nبرای ارتباط با ادمین از دستور /Contact استفاده کن.")


    if m.text == "/Contact":
        Answer = await app.ask(m.chat.id,"هر حرفی بزنی به صورت **کاملا ناشناس** به ادمین منتقل میشه!\nلغو: /cancel",timeout=120)
        if Answer:
            if Answer.text=="/cancel":
                await app.send_message(Answer.from_user.id, "کنسلش کردم مشتی.")
                pass

            else:
                if Answer.media:
                    await app.send_message(6656876248, "پیام ناشناس داری عزیزم:")
                    await app.copy_media_group(6656876248, Answer.from_user.id, Answer.id)
                    await app.send_message(Answer.from_user.id, "عشق داداش پیامت با موفقیت ارسال شد", reply_to_message_id= Answer.id)
                else:
                    await app.send_message(6656876248, "پیام ناشناس داری عزیزم:")
                    await app.copy_message(6656876248, Answer.from_user.id, Answer.id)
                    await app.send_message(Answer.from_user.id, "عشق داداش پیامت با موفقیت ارسال شد", reply_to_message_id= Answer.id)
        if not Answer:
            await app.send_message(Answer.from_user.id, "مشتی پیام ندادی کاسه صبرم لبریز شد کنسلش کردم",)
       
    if m.text != "/Contact" and m.text != "/start":
        status_member = await get_chat_member_status()
        if status_member == "OWNER" or status_member == "ADMINISTRATOR":
            if m.media:
                media_to_reply_and_forward_id = m.id
                chat_id_admin = m.from_user.id
                try:
                    Answer = await app.ask(m.chat.id,"لینک پیامی که قصد ریپلای کردن دارید ارسال نمایید\nزمان انتظار:**20ثانیه**",timeout=20)
                    if Answer:
                        Answer_text= Answer.text
                        reply_to_msg_id= int(Answer_text.split("/")[-1])
                        ChannelOrGRoup = Answer_text.split("/")[-2]
                        try:
                            if ChannelOrGRoup == "Source_Of_Information" :
                                await app.copy_message(ChannelOrGRoup ,from_chat_id= int(chat_id_admin), message_id=int(media_to_reply_and_forward_id), reply_to_message_id=int(reply_to_msg_id) )
                                await app.send_message(int(chat_id_admin), "**ارباب! پیام ارسال شد.**")

                            if ChannelOrGRoup == "1718595276":
                                await app.copy_message(int(ChannelOrGRoup) ,from_chat_id= int(chat_id_admin), message_id=int(media_to_reply_and_forward_id), reply_to_message_id=int(reply_to_msg_id) )
                                await app.send_message(int(chat_id_admin), "**ارباب! پیام ارسال شد.**")
                        except:
                            await app.send_message(chat_id_admin, "**لینکت اشتباهه ارباب!**")
                except:
                    await app.send_message(m.from_user.id, "مشتی پیام ندادی کاسه صبرم لبریز شد کنسلش کردم", reply_to_message_id= Answer.id)

        else:
            if not m.media:
                await app.send_message(m.chat.id, "شما **ادمین** نیستید! \nبرای همین دسترسی به ربات نداری زیباروی من \nبرای ارتباط با ادمین دستور /Contact رو بفرست:)", reply_to_message_id=m.id)

app.run()
