from pyrogram import Client, filters
import importlib
import os

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

app = Client("movie_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

def get_all_sites():
    site_modules = []
    for filename in os.listdir("sites"):
        if filename.endswith(".py"):
            name = filename[:-3]
            mod = importlib.import_module(f"sites.{name}")
            site_modules.append(mod)
    return site_modules

@app.on_message(filters.text & ~filters.edited & ~filters.channel)
def search_all_sites(client, message):
    query = message.text.strip()
    if len(query) < 3:
        return

    message.reply("মুভি খোঁজা হচ্ছে, একটু অপেক্ষা করুন...")

    all_results = []
    for site in get_all_sites():
        try:
            all_results += site.search(query)
        except Exception as e:
            all_results.append(f"❌ `{site.__name__}` failed")

    if all_results:
        message.reply("\n\n".join(all_results))
    else:
        message.reply("দুঃখিত, কিছু পাওয়া যায়নি!")

app.run()
