from botcity.web import WebBot
from botcity.maestro import *

from pages.rpa_challenge import RpaChallengePage

from settings.setup import setup
from settings.config import config

import sys

from settings.logger import logger


# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main() -> None:
    try: 
        maestro = BotMaestroSDK.from_sys_args()
        execution = maestro.get_execution()

        logger.info(f"Task ID is: {execution.task_id}")
        logger.info(f"Task Parameters are: {execution.parameters}")

        bot = WebBot()
    
        bot = setup(maestro, bot)
        process(maestro, bot, execution)

    except Exception as e:
        logger.critical(e, exc_info=True)

        exception_message, _, _ = sys.exc_info()

        maestro.error(task_id=execution.task_id, exception=e)
        maestro.finish_task(
            task_id=execution.task_id,
            status=AutomationTaskFinishStatus.FAILED,
            message=str(exception_message)
        )


    else:
        logger.info("Bot finished successfully!")
        maestro.finish_task(
            task_id=execution.task_id,
            status=AutomationTaskFinishStatus.SUCCESS,
            message="Task Finished OK."
        )


def process(maestro: BotMaestroSDK, bot: WebBot, execution: BotExecution) -> None:
    """This function defines the steps to run the bot

    Args:
        maestro (BotMaestroSDK): Maestro instance
        bot (WebBot): Bot instance
        execution (BotExecution): Execution instance
    """

    rpa_challenge = RpaChallengePage(bot)

    rpa_challenge.select_challenge()
    data = rpa_challenge.download_file()
    rpa_challenge.start_challenge()

    for _, row in data.iterrows():
        rpa_challenge.fill_in_user(row)

    bot.screenshot(filepath=config.screenshot_file)
    maestro.post_artifact(
        task_id=execution.task_id,
        artifact_name="Resultado",
        filepath=config.screenshot_file
    )

    bot.stop_browser()

if __name__ == '__main__':
    main()
