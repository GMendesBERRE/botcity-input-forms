from botcity.web import By
from botcity.web import WebBot
from typing import Tuple

class BasePage():
    """The BasePage class holds all common functionality across the website.
    Also provides a nice wrapper when dealing with selenium functions that may
    not be easy to understand.
    """

    def __init__(self, bot: WebBot):
        """ This function is called every time a new object of the base class is created"""
        self.bot = bot
    
    def click(self, by_locator: Tuple[str, By]) -> None:
        """ Performs click on web element whose locator is passed to it"""
        self.bot.find_element(*by_locator).click()
    
    def send_keys(self, by_locator: Tuple[str, By], text: str) -> None:
        """ Performs text entry of the passed in text, in a web element whose locator is passed to it"""
        self.bot.find_element(*by_locator).send_keys(text)