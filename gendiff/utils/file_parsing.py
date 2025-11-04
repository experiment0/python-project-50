import json
from enum import Enum
from pathlib import Path

import yaml


class FileType(Enum):
    JSON = "json"
    YAML = "yaml"
    

JSON_EXTS = [".json"]
YAML_EXTS = [".yaml", ".yml"]


def get_file_type(file_path: str) -> FileType:
    file_ext = Path(file_path).suffix.lower()
    
    if file_ext in JSON_EXTS:
        return FileType.JSON
    elif file_ext in YAML_EXTS:
        return FileType.YAML
    
    raise ValueError(
        "Unknown file extension. " + 
        f"Use files {', '.join(JSON_EXTS)}, {', '.join(YAML_EXTS)}"
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
        