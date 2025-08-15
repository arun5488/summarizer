import os
import yaml
from box.exceptions import BoxValueError
from pathlib import Path
from box import ConfigBox
from ensure import ensure_annotations
from src.textSummarizer import logger
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    logger.info("Inside read_yaml method")

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Yaml file loaded successfully from : {path_to_yaml}")
            
            return ConfigBox(content)
    except BoxValueError as e:
        logger.info(f"Error occurred while reading the YAML file: {e}")
        raise e
    except Exception as e:
        logger.info(f"Error occurred while reading the YAML file: {e}")
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    logger.info("Inside create_directories method")
    try:
        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"Directories created successfully at: {path_to_directories}")
        
    except Exception as e:
        logger.info(f"Error occurred while creating directories: {e}")
        raise e