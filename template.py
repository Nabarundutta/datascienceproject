import os
import logging
from pathlib import Path
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',filename='app.log')
project_name = "datascience"

list_of_items = [
    "github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py", ## contains the generic functions
    f"src/{project_name}/utils/common.py", ## functions wjich are common
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "research/research.ipynb",
    "setup.py",
    "templates/index.html"
]

for filepath in list_of_items:
    filepath = Path(filepath)
    # print(filepath)
    filedir,filename = os.path.split(filepath)
    # print(f"{filedir} + {filename}")

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file : {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"creating empty path : {filepath}")
    else:
        logging.info(f"{filepath} already exists")