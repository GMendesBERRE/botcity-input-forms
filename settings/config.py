import os
import shutil


from pydantic_settings import BaseSettings
from pydantic import Field, DirectoryPath, AnyUrl, field_validator

class Settings(BaseSettings):
    """This class contains settings for the project
    """
    process_id: str = Field(..., env="PROCESS_ID")
    rpa_challenge_url: AnyUrl = Field(..., env="RPA_CHALLENGE_URL")
    downloads_folder: DirectoryPath = Field(..., env="DOWNLOADS_FOLDER")
    logs_folder: DirectoryPath = Field(..., env="LOGS_FOLDER")
    screenshot_file: str = Field(..., env="SCREENSHOT_FILE")
 
    @field_validator(*('downloads_folder', 'logs_folder'), mode='before')
    @classmethod
    def folder_must_exist(cls, folder: str) -> str:
        """This function ensures the folder exists

        Args:
            folder (str): Folder that should be created

        Returns:
            str: Full path to the folder
        """
        if not os.path.exists(folder):
            os.makedirs(folder)
        return folder
      
    class Config:
        env_prefix = ""
        case_sentive = False
        env_file = '.env'
        env_file_encoding = 'utf-8'

config = Settings()