from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.model_evaluation import ModelEvaluation
from src.textSummarizer import logger

class ModelEvaluationPipeline:
    def __init__(self):
        logger.info("Inside ModelEvaluationPipeline class")
        pass

    def initiate_model_evaluation(self):
        logger.info("inside initiate_model_evaluation method")
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(model_evaluation_config)
        logger.info("initiating model evaluation")
        model_evaluation.evaluate()
        logger.info("model evaluation completed")

        