from src.datascience import logger
from src.datascience.pipeline.data_ingestion import DataIngestionTrainingPipeline



STAGE_NAME = "DATA INGESTION STEP"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e