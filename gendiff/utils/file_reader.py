import json
from enum import Enum
from pathlib import Path

import yaml


class FileType(Enum):
    JSON = "json"
    YAML = "yaml"
    

JSON_EXTS = [".json"]
YAML_EXTS = [".yaml", ".yml"]
AVAILABLE_FILE_EXTX = ", ".join(JSON_EXTS + YAML_EXTS)


def get_file_type(file_path: str) -> FileType:
    file_ext = Path(file_path).suffix.lower()
    
    if file_ext in JSON_EXTS:
        return FileType.JSON
    elif file_ext in YAML_EXTS:
        return FileType.YAML
    
    raise ValueError(
        f"Unknown file extension. Use files in {AVAILABLE_FILE_EXTX} format."
    )


def get_data_from_file(file_path: str) -> dict:
    file_type = get_file_type(file_path)
    
    match file_type:
        case FileType.JSON:
            return json.load(open(file_path))
        case FileType.YAML:
            with open(file_path, "r") as file:  
                data = yaml.safe_load(file)  
            return data 
        case _:
            raise ValueError("Failed to retrieve file contents.")
        