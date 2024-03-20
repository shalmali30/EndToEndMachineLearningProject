from dataclasses import dataclass  #creating entity using dataclasses
from pathlib import Path

@dataclass(frozen=True)  # Frozen:true mean besides these variables , no other variable will be used
class DataIngestionConfig:   # This is entity and this is return type of class this is custom return type can be created with the help of dataclass. (unlike CustomBox)
    root_dir: Path    #root_dir is variable and Path is datatype
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict   # Yaml file always return dictionary format , so datatype is Dict

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    alpha: float
    l1_ratio: float
    target_column: str

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    all_params: dict
    metric_file_name: Path
    target_column: str