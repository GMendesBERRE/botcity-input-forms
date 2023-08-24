from settings.config import config
from botcity.web import WebBot, Browser
from botcity.maestro import BotMaestroSDK
from settings.logger import logger, MaestroLogHandler

def setup_bot(bot: WebBot) -> WebBot:
    """This function defines the default browser and sets downloads folder

    Args:
        bot (WebBot): Bot instance that should be altered

    Returns:
        WebBot: Altered Bot instance
    """
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = r"webdrivers\chromedriver.exe"
    bot.download_folder_path = str(config.downloads_folder)

    return bot

def setup_maestro(maestro: BotMaestroSDK) -> None:
    """This function adds maestro handler to send logs to maestro

    Args:
        maestro (BotMaestroSDK): Bot maestro instance tho be attached to the log handler
    """
    # add maestro handler to send logs to maestro
    logger.addHandler(MaestroLogHandler(maestro))

def setup(maestro: BotMaestroSDK, bot: WebBot) -> WebBot:
    """This function creates all necessary setups for the bot

    Args:
        maestro (BotMaestroSDK): Bot maestro instance tho be attached to the log handler
        bot (WebBot): Bot instance that should be altered

    Returns:
        WebBot: Altered Bot instance
    """
    setup_maestro(maestro)
    return  setup_bot(bot)