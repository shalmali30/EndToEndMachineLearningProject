import os
import urllib.request as request
import zipfile
from mlProject import logger
from mlProject.utils.common import get_size
from mlProject.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:  
    def __init__(self, config: DataIngestionConfig):  #this DataIngestionConfig has to be passed here so that this function (DataIngestion) can start
        self.config = config


    # First download function from url
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):   #if path is not available it will create the path
            filename, headers = request.urlretrieve(   #with the help of request package it will download the data, this will return as a filename and we are storing in local_data_file
                url = self.config.source_URL,
                filename = self.config.local_data_file  
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")



    # extract the zip file with following function
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir  #provide path
        os.makedirs(unzip_path, exist_ok=True)  
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)