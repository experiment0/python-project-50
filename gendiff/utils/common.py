from enum import Enum
from typing import Union, Optional, List
import json
from pydantic import BaseModel


# R ~ Result
class R(Enum):
    EQUALL = " "
    ADD = "+"
    REMOVE = "-"

class DiffItem(BaseModel):
    result: R
    key: str
    value: Optional[Union[int, float, bool, str, list, dict]]


def get_diffs(dict1: dict, dict2: dict) -> List[DiffItem]:
    all_keys = sorted(list(set(dict1.keys()) | set(dict2.keys())))    
    diffs = []

    for key in all_keys:
        # Ключ есть в обоих файлах
        if key in dict1 and key in dict2:
            if dict1[key] == dict2[key]:
                # Значение не изменилось
                diffs.append(DiffItem(result=R.EQUALL, key=key, value=dict1[key]))
            else:
                # Значение изменилось
                diffs.append(DiffItem(result=R.REMOVE, key=key, value=dict1[key]))
                diffs.append(DiffItem(result=R.ADD, key=key, value=dict2[key]))
        # Ключ удален из первого файла
        elif key in dict1 and key not in dict2:
            diffs.append(DiffItem(result=R.REMOVE, key=key, value=dict1[key]))
        # Остается вариант, что ключа нет в первом файле и он появился во втором
        else:
            diffs.append(DiffItem(result=R.ADD, key=key, value=dict2[key]))
    
    return diffs


def diffs_to_str(diffs: List[DiffItem]) -> str:
    result = "{\n"
    
    for d in diffs:
        formatted_value = d.value if isinstance(d.value, str) else json.dumps(d.value)
        result += f"    {d.result.value} {d.key}: {formatted_value}\n"
    
    result += "}"
    
    return result


def generate_diff(file_path1: str, file_path2: str) -> str:
    dict1 = json.load(open(file_path1))
    dict2 = json.load(open(file_path2))
    
    diffs = get_diffs(dict1, dict2)
    diffs_str = diffs_to_str(diffs)
    
    return diffs_str
