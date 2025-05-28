from src.datascience import logger
from src.datascience.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transformation import DataTransformationTrainingPipeline
from src.datascience.pipeline.model_training import ModelTrainerTrainingPipeline
from src.datascience.pipeline.model_evaluation import ModelEvaluationTrainingPipeline


STAGE_NAME = "DATA INGESTION STEP"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataValidationTrainingPipeline()
   data_ingestion.initiate_data_validation()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "DATA TRANSFORMATION STAGE"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
    data_transform = DataTransformationTrainingPipeline()
    data_transform.initiate_data_transformation()
    logger.info(f">>>>> stage {STAGE_NAME} completed<<<<<<\n\nx==========x")
except Exception as e:
     logger.exception(e)
     raise e

STAGE_NAME = "Model Trainer stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = ModelTrainerTrainingPipeline()
   data_ingestion.initiate_model_training()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model evaluation stage"
try:
     logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
     model_eval = ModelEvaluationTrainingPipeline()
     model_eval.initiate_model_evaluation()
     logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
     logger.exception(e)
     raise e