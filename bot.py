from botcity.web import WebBot, Browser, By
from botcity.maestro import *
from botcity.plugins.files import BotFilesPlugin
from botcity.plugins.excel import BotExcelPlugin

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def setup_bot(bot:WebBot):
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = r"webdrivers\chromedriver.exe"

    return bot

def main():
    files = BotFilesPlugin()
    bot_excel = BotExcelPlugin()

    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()
    bot = setup_bot(bot)
    
    bot.browse("https://www.rpachallenge.com/")

    bot.find_element("//a[text() = 'Input Forms']", By.XPATH).click()
    # bot.find_element("//a[text() = ' Download Excel ']", By.XPATH).click()

    with files.wait_for_file(directory_path=r"D:\projects\botcity-input-forms", file_extension=".xlsx", timeout=300000):
        bot.find_element("//a[text() = ' Download Excel ']", By.XPATH).click()
    file = files.get_last_created_file(directory_path=r"D:\projects\botcity-input-forms", file_extension=".xlsx")
    
    bot_excel.read(file)

    df = bot_excel.as_dataframe()
    df.columns = df.iloc[0]
    df = df[1:]

    bot.find_element("//button[text()='Start']", by=By.XPATH).click()

    for index, row in df.iterrows():
        bot.find_element("//label[text()='First Name']/../input", by=By.XPATH).send_keys(row["First Name"])
        bot.find_element("//label[text()='Last Name']/../input", by=By.XPATH).send_keys(row["Last Name "])
        bot.find_element("//label[text()='Company Name']/../input", by=By.XPATH).send_keys(row["Company Name"])
        bot.find_element("//label[text()='Role in Company']/../input", by=By.XPATH).send_keys(row["Role in Company"])
        bot.find_element("//label[text()='Address']/../input", by=By.XPATH).send_keys(row["Address"])
        bot.find_element("//label[text()='Email']/../input", by=By.XPATH).send_keys(row["Email"])
        bot.find_element("//label[text()='Phone Number']/../input", by=By.XPATH).send_keys(row["Phone Number"])

        bot.find_element("//input[@type='submit']", by=By.XPATH).click()

    bot.wait(3000)


    bot.stop_browser()

    maestro.finish_task(
        task_id=execution.task_id,
        status=AutomationTaskFinishStatus.SUCCESS,
        message="Task Finished OK."
    )


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()



# - SITE
## - MENU
### - FUNÇÃO
#### - GET    -> Capturar informação
#### - DEL    -> Deletar informação
#### - PUT    -> Inserir informação
#### - UPD    -> Atualizar informação 
#### - NAV    -> Navegar no site