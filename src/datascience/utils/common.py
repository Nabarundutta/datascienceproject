import os
import yaml
from box import ConfigBox
from ensure import ensure_annotations
from pathlib import Path
import joblib
from box.exceptions import BoxValueError
from src.datascience import logger
import json
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
## CREATE DIRECTORIES
@ensure_annotations
def create_directories(path_to_directory:list, verbose: bool = True):
    for path in path_to_directory:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Created directory at {path}")

@ensure_annotations
def save_json(path:Path,data:dict):
    with open(path,"w") as f:
        json.dump(data,f,indent=4)
    logger.info(f"json file saved at : {path}")

@ensure_annotations
def load_json(path:Path):
    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file loaded successfully from {path}")
    return content

@ensure_annotations
def save_bin(data:Any,path:Path):
    joblib.dump(value=data,filename=path)
    logger.info(f"binary file saved at : {path}")

@ensure_annotations
def load_bin(path:Path)-> Any:
    data = joblib.load(path)
    logger.info(f"binary file loaded from {path}")
    return data