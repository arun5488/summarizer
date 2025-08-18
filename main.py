from src.textSummarizer import logger
from src.textSummarizer.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.textSummarizer.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.textSummarizer.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.textSummarizer.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline
# STAGE_NAME = "Data Ingestion stage"

# try:
#     logger.info(f"stage {STAGE_NAME} initiated")
#     data_ingestion_pipeline = DataIngestionPipeline()
#     data_ingestion_pipeline.initiate_data_ingestion()
#     logger.info(f"stage {STAGE_NAME} completed")
# except Exception as e:
#     logger.exception(f"exception {e} ")
#     raise e

# STAGE_NAME = "Data Transformation stage"
# try:
#     logger.info(f"stage {STAGE_NAME} initiated")
#     data_transformation_pipeline = DataTransformationPipeline()
#     data_transformation_pipeline.initiate_data_transformation()
#     logger.info(f"stage {STAGE_NAME} completed")
# except Exception as e:
#     logger.exception(f"exception {e} ")
#     raise e

# STAGE_NAME = "Model Trainer stage"
# try:
#     logger.info(f"stage {STAGE_NAME} initiated")
#     model_trainer_pipeline = ModelTrainerPipeline()
#     model_trainer_pipeline.initiate_model_training()
#     logger.info(f"stage {STAGE_NAME} completed")
# except Exception as e:
#     logger.exception(f"exception {e} ")
#     raise e


STAGE_NAME = "Model Evaluation stage"
try:
    logger.info(f"stage {STAGE_NAME} initiated")
    model_evaluation_pipeline = ModelEvaluationPipeline()
    model_evaluation_pipeline.initiate_model_evaluation()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(f"exception {e} ")
    raise e