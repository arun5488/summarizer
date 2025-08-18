from src.textSummarizer import constants as const
from src.textSummarizer.utils.common import *
from src.textSummarizer.entity import (DataIngestionConfig,
                                       DataTransformationConfig,
                                       ModelTrainerConfig,
                                       ModelEvaluationConfig)


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
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        logger.info("Inside get_model_trainer_config method")
        config = self.config.model_trainer
        params = self.param.TrainingArguments

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir = config.root_dir,
            data_path = config.data_path,
            model_ckpt = config.model_ckpt,
            num_train_epochs = params.num_train_epochs,
            warmup_steps = params.warmup_steps,
            per_device_train_batch_size= params.per_device_train_batch_size,
            weight_decay = params.weight_decay,
            logging_steps = params.logging_steps,
            evaluation_strategy = params.evaluation_strategy,
            eval_steps = params.eval_steps,
            save_steps = params.save_steps,
            gradient_accumulation_steps = params.gradient_accumulation_steps
        )

        return model_trainer_config
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        logger.info("Inside get_model_evaluation_config method")
        config = self.config.model_evaluation

        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_ckpt=config.model_ckpt,
            model_path=config.model_path,
            tokenizer_path=config.tokenizer_path,
            metric_file_name=config.metric_file_name
        
        )

        return model_evaluation_config
