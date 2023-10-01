import logging
from pythonjsonlogger import jsonlogger
from logging.handlers import TimedRotatingFileHandler
from settings.config import config
from botcity.maestro import BotMaestroSDK, Column
from datetime import datetime

FORMAT = '%(message)%(levelname)%(name)%(asctime)'

# Create logger
logger = logging.getLogger()

# Set log level to debug
logger.setLevel(logging.INFO)

# Create JSON formatter
formatter = jsonlogger.JsonFormatter(FORMAT)

# Set stream handler
handler = logging.StreamHandler()
# handler.setFormatter(formatter)
logger.addHandler(handler)

# Set a rotating file handler
handler = TimedRotatingFileHandler(filename=config.logs_folder / f'{config.process_id}-log.log', backupCount=10, when='midnight')
handler.setFormatter(formatter)
logger.addHandler(handler)

class MaestroLogHandler(logging.StreamHandler):
    """ This class handles the integration between python's logger and maestro logs
    """
    def __init__(self, maestro: BotMaestroSDK):
        """This function initializes the object

        Args:
            maestro (BotMaestroSDK): Bot Maestro that the logs should be sent to
        """
        super().__init__()
        self.maestro = maestro
        self.activity_label = f'{config.process_id} {datetime.now().strftime("%Y-%m-%d_%H-%M")}'

        # If maestro is not connected, exit function
        if self.maestro.access_token is None: return

        self.maestro.new_log(
        self.activity_label,
        [
            Column(name="Message", label="message", width=200)
        ]
        )

    
    on_same_line = False
    def emit(self, record):
        """This function sends a log to maestro

        Args:
            record (LogRecord): The message that should be sent to maestro
        """
        try:
            # If maestro is not connected, exit function
            if self.maestro.access_token is None: return
            
            msg = self.format(record)
            self.maestro.new_log_entry(
                activity_label=self.activity_label,
                values={
                    "message": msg,
                }
            )
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)
