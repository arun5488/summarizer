from src.textSummarizer import constants as const
from src.textSummarizer.utils.common import *
from src.textSummarizer.entity import (DataIngestionConfig,
                                       DataTransformationConfig)


class ConfigurationManager:

    def __init__(self,
                  config_file_path=const.CONFIG_FILE_PATH,                           
                  param_file_path= const.PARAMS_FILE_PATH):
        logger.info("reading config file")
        self.config = read_yaml(config_file_path)
        logger.info("reading params file")
        self.param = read_yaml(param_file_path)
        
        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        logger.info(" inside get_data_ingestion_config")
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config.root_dir),
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        logger.info("Inside get_data_transformation_config method")
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path = config.data_path,
            tokenizer_name = config.tokenizer_name
        )

        return data_transformation_config
