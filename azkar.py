from telethon import TelegramClient, events, Button
import random
import asyncio
import os

# بيانات البوت
API_ID = 22696039
API_HASH = "00f9cc1d3419e879013f7a9d2d9432e2"
BOT_TOKEN = "7732686950:AAFxYdmBxV7XGu5wUfasxqyjWUKchbVKXg8"

# أيدي الجروبات المستهدفة
CHAT_IDS = [-1002457023914, -1002414213451]  # الجروب الأول + الجروب الثاني

# تأكيد بداية التشغيل
print("✅ البوت بدأ التشغيل...")

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

# تشغيل البوت
bot = TelegramClient("bot", API_ID, API_HASH).start(bot_token=BOT_TOKEN)

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

# وظيفة Vercel لتشغيل البوت
def handler(request):
    loop = asyncio.get_event_loop()
    loop.create_task(send_zekr())  # تنفيذ send_zekr بشكل غير متزامن

    return {
        "statusCode": 200,
        "body": "الوظيفة تعمل بشكل صحيح!"
    }

# تشغيل البوت في بيئة Vercel
if __name__ == "__main__":
    handler("test")
