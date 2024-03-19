# before adding anything here, we will first test it in notebook : 01_data_ingestion.ipynb

from mlProject.constants import *  # first calling the path of yaml files which are in the constants folder
from mlProject.utils.common import read_yaml, create_directories  # then call the other functions created for reading the yamlfile (read_yaml), and creating dir etc from utils
from mlProject.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig
class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,  #we store the imported variable in one variable
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath) #read the yaml imported files
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

# using self as it is a class variable
        
        #create a directory using following function
        create_directories([self.config.artifacts_root])

    # 
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion  #DataIngestionConfig is the return type. whatever written in dataingestionconfig function ,it will return .You can call this function or entity       config = self.config.data_ingestion

        create_directories([config.root_dir])  #data_ingestion folder should be created inside artifacts. This is code is for that

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,    #one by one we rae returning all the variables 
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:  # return type : DataValidationConfig
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir = config.unzip_data_dir,
            all_schema=schema,
        )

        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
        )

        return data_transformation_config