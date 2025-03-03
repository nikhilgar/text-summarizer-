import os 
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging_module import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
#@ensure_annotations is a decorator that returns a list of annotations that should be used when creating the output file for the output  
def read_yaml(path_to_yaml : Path) -> ConfigBox:
    """reads yaml file and returns
    
    Args:
    path_to_yaml (str): path like input
    
    Raises:
    ValueError: if yaml file is empty 
    e: empty file
    
    Returns:
    ConfigBox: ComfiBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info("yaml file: {path_to_yaml} loaded sucessfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directory(path_to_directory: list, verbose=True):
    """Create list of directories
    
    Args:
    path_to_directory (list): list of directory 
    ignore_log (bool, optional): ignore if multiple dirs is to be created. Default to false.
    """
    for path in path_to_directory:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in kb 
    
    Args:
    path(Path): path of the file
    
    Returns:
    str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"








