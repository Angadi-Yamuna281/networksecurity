from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys
if __name__=='__main__':
    try:
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config)
        logging.info("Initiate Data Ingestion")
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data Ingestion completed")
        print(data_ingestion_artifact)
        data_validation_config = DataValidationConfig(training_pipeline_config)
        data_validation = DataValidation(data_ingestion_artifact, data_validation_config)
        logging.info("Initiate data Validation")
        data_validation_artifacts = data_validation.initiate_data_validation()
        logging.info("Data Validation completed")
        data_transformation_config = DataTransformationConfig(training_pipeline_config)
        data_transformation = DataTransformation(data_transformation_config, data_validation_artifacts)
        data_transformation_artifacts = data_transformation.inititate_data_transformation()
        logging.info("Data Transformation Completed.")
        print(data_transformation_artifacts)
        
    except Exception as  e:
        raise NetworkSecurityException(e, sys)    