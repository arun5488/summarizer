from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.data_transformation import DataTransformation
from src.textSummarizer import logger

class DataTransformationPipeline:
    def __init__(self):
        logger.info("Inside DataTransformationPipeline class")
        pass

    def initiate_data_transformation(self):
        logger.info("inside initiate_data_transformation method")
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(data_transformation_config)
        logger.info("initiating data transformation")
        data_transformation.convert()
        logger.info("data transformation completed")