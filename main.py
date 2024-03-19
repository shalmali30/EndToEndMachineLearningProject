'''
from src.mlProject import logger

logger.info("This is our custome logging")


#output : [2024-03-11 11:44:23,460: INFO: main: This is our custome logging]

#same information is stored in "Running_log.log file"

'''

# copy paste code from pipeline 

from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline


STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")    #logging the info
    obj = DataIngestionTrainingPipeline()   
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


# To test the whole modular coding for 01_data_ingestion, once you have copied code from notebook in respective folders,

# delete the artifact folder, delete log file and exceute main.py from terminal 

STAGE_NAME = "Data Validation stage"

try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataValidationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e