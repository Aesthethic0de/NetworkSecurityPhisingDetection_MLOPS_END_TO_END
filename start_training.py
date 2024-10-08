from exception.exception import NetworkSecurityException
from logger.logger import logging
import os
import sys
from pipeline.training_pipeline import TrainingPipeline

def start_training():
    try:
        logging.info("training has started!!")
        model_training = TrainingPipeline()
        model_training.run_pipeline()

    except Exception as e:
        logging.error(f"training has not started due to {str(e)}")
        raise NetworkSecurityException(e, sys)
    
if __name__ == "__main__":
    start_training()