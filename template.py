import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "mlproject"

list_of_files = [
    r"src\mlproject\__init__.py",
    r"src\mlproject\components\__init__.py",
    r"src\mlproject\utils\__init__.py",
    r"src\mlproject\entity\common.py",
    r"src\mlproject\config\__init__.py",
    r"src\mlproject\config\configuration.py",
    r"src\mlproject\pipeline\__init__.py",
    r"src\mlproject\entity\__init__.py",
    r"src\mlproject\entity\config_entity.py",
    r"src\mlproject\constants\__init__.py",
    "config\config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirement.txt",
    "setup.py",
    r"research\trails.ipynb",
    r"templates\index.html"


]


for filepath in list_of_files:
    filepath = Path(filepath)

    filedir,filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")