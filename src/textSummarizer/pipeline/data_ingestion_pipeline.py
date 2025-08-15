from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.data_ingestion import DataIngestion
from src.textSummarizer import logger

class DataIngestionPipeline:
    def __init__(self):
        logger.info("Inside DataIngestionPipeline class")
        pass

    def initiate_data_ingestion(self):
        logger.info("inside initiate_data_ingestion method")
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        logger.info("initiating data extraction from zip file")
        data_ingestion.extract_zip_file()
        logger.info("data extraction completed")

        