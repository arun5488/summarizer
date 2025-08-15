import os
import zipfile
from src.textSummarizer import logger
from src.textSummarizer.config.configuration import DataIngestionConfig
class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config
    
    def extract_zip_file(self):
        logger.info("Inside extract_zip_file method")
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        
        logger.info(f"Files unzipped at {unzip_path}")
