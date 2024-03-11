# First import everything which is needed 

from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_ingestion import DataIngestion
from mlProject import logger 

STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:   
    def __init__(self):
        pass   #I do not want to create anything in constructor so Pass

    def main(self):   #copy code from notebook
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == '__main__':  #the use of this : whenever this file will run , it will start running from this line
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")    #logging the info
        obj = DataIngestionTrainingPipeline()   #initialise
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    
    #now call from main.py