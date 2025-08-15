from src.textSummarizer.components.model_trainer import ModelTrainer
from src.textSummarizer import logger
from src.textSummarizer.config.configuration import ConfigurationManager

class ModelTrainerPipeline:
    def __init__(self):
        logger.info("Inside ModelTrainerPipeline class")
        pass

    def initiate_model_training(self):
        logger.info("inside initiate_model_training method")
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(model_trainer_config)
        logger.info("initiating model training")
        model_trainer.train()
        logger.info("model training completed")
