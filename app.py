from core.auto import auto

try:
    bot = auto()
    bot.bot_start()
except KeyboardInterrupt:
    print("使用者停止")
