from core.auto import auto
bot = auto()
try:
    bot.bot_start()
except KeyboardInterrupt:
    print("使用者停止")
