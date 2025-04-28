# Coded by: @Mavdiii

from telethon import TelegramClient, events, Button
import random
import asyncio
import time
import os

# بيانات البوت
API_ID = 22696039
API_HASH = "00f9cc1d3419e879013f7a9d2d9432e2"
BOT_TOKEN = "7732686950:AAFxYdmBxV7XGu5wUfasxqyjWUKchbVKXg8"

# أيدي الجروبات المستهدفة
CHAT_IDS = [-1002457023914, -1002414213451]  # الجروب الأول + الجروب الثاني

# تأكيد بداية التشغيل
print("✅ البوت بدأ التشغيل...")

# تشغيل البوت
bot = TelegramClient("bot", API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# تحميل الأذكار من ملف التكست
def load_azkar(file_path):
    if not os.path.exists(file_path):
        print("⚠ ملف الأذكار مش موجود! اتأكد إنه معمول باسم 'azkar.txt'.")
        return []
    
    with open(file_path, "r", encoding="utf-8") as file:
        azkar = file.read().splitlines()
    
    if not azkar:
        print("⚠ ملف الأذكار موجود لكنه **فارغ**، لازم تضيف الأذكار علشان يشتغل البوت.")
    
    return azkar

azkar_list = load_azkar("azkar.txt")

# تأكيد تعريف البوت قبل الحدث
print("🔹 البوت متصل بالتليجرام بنجاح!")

# كود فحص استقبال الرسائل
@bot.on(events.NewMessage)
async def check_messages(event):
    print(f"📌 استلم البوت رسالة من: {event.chat_id} - محتوى الرسالة: {event.text}")

@bot.on(events.NewMessage(pattern="/start"))
async def start_handler(event):
    print(f"🚀 استقبل البوت أمر /start من: {event.chat_id}")  # تأكيد استقبال الأمر

    message = """✨ **ذكِّر قلبك بالله، وارتقِ بروحك 📿**  
    في زحمة الحياة، البوت ده هيكون **رفيقك للذكر والدعاء والتسبيح** 🌙  
    خلّي لسانك رطب بذكر الله، وابدأ كل يوم بنور جديد 💛  
    
    ﴿ **فَاذْكُرُونِي أَذْكُرْكُمْ** ﴾ – وعد ربّاني لا يُخلف!  
    
    💻 **مبرمج البوت:** @Mavdiii"""

    keyboard = [[Button.url("📖 تلاوات قرآنية", "https://t.me/Telawat_Quran_0")]]
    await event.respond(message, buttons=keyboard)

# إرسال ذكر عشوائي لكل الجروبات
async def send_zekr():
    while True:
        if azkar_list:
            zekr = random.choice(azkar_list)
            keyboard = [[Button.url("📖 تلاوات قرآنية", "https://t.me/Telawat_Quran_0")]]
            
            for chat_id in CHAT_IDS:
                await bot.send_message(chat_id, zekr, buttons=keyboard)
                print(f"✅ تم إرسال الذكر إلى الجروب {chat_id}")
        else:
            print("⚠ مفيش أذكار! تأكد إنك ضفتها في 'azkar.txt'.")

        await asyncio.sleep(300)  # كل 5 دقائق

# تشغيل البوت والاستجابة للأحداث
with bot:
    bot.loop.run_until_complete(send_zekr())
