import os

class Config(object):
    APP_ID = int(os.environ.get("21424088", 6))
    API_HASH = os.environ.get("ea3f63369a81169bad4ac083f793b756", None)
    TOKEN = os.environ.get("5931097954:AAECg688t-RyGVUrabX7Or8a2taJZaoTcJw", None)
    BOT_US = os.environ.get("BOT_US", None)
    WELCOME_TEXT = os.environ.get("WELCOME_TEXT", None)
    RULES = os.environ.get("RULES", None)
