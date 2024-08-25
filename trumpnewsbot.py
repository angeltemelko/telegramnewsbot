import requests
import asyncio
from telegram import Bot
from telegram.constants import ParseMode

# Telegram bot token from BotFather
TELEGRAM_BOT_TOKEN = '7252279484:AAEU06DYC5Xsgv3Ms5swkll6mXDh_Vna4eI'
CHANNEL_NAME = '@Trump2024NewsFlash'

# News API key
NEWS_API_KEY = '4be9660c7dee4a80a950e23291ffdde1'
NEWS_API_URL = 'https://newsapi.org/v2/everything?q=Trump&sortBy=popularity&apiKey=' + NEWS_API_KEY

# Function to fetch top Trump news
def get_top_trump_news():
    response = requests.get(NEWS_API_URL)
    articles = response.json().get('articles', [])
    return articles[:5]  # Get top 5 articles

# Async function to send news to the Telegram channel
async def send_news_to_channel(bot, articles):
    for article in articles:
        title = article['title']
        url = article['url']
        await bot.send_message(chat_id=CHANNEL_NAME, text=f"{title}\n{url}", parse_mode=ParseMode.HTML)

async def main():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    
    # Fetch top Trump news
    articles = get_top_trump_news()
    
    # Send news to the Telegram channel
    await send_news_to_channel(bot, articles)

# Run the async main function
if __name__ == "__main__":
    asyncio.run(main())
