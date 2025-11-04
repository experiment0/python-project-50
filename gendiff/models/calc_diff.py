from typing import Dict, List, Literal, Optional, Self, Union

from pydantic import BaseModel

ResultType = Literal[
    "equal",
    "add",
    "remove",
    "change",
]

DictValueType = Optional[Union[str, int, float, bool, list, dict]]
DictType = Dict[str, DictValueType]


class DiffItem(BaseModel):
    result: ResultType
    key: str
    old_value: DictValueType = None
    new_value: DictValueType = None
    children: Optional[List[Self]] = None


DiffsType = List[DiffItem]


def get_diffs(dict1: DictType, dict2: DictType) -> DiffsType:
    # Ключи обоих словарей
    all_keys = sorted(set(dict1.keys()) | set(dict2.keys()))
    # Список различий
    diffs = []

    # Итерируемся по всем ключам
    for key in all_keys:
        value1 = dict1.get(key)
        value2 = dict2.get(key)
            
        # Ключ есть в обоих словарях
        if key in dict1 and key in dict2:            
            # Оба значения - словари
            if isinstance(value1, dict) and isinstance(value2, dict):
                diffs.append(DiffItem(
                    result="equal",
                    key=key,
                    children=get_diffs(value1, value2),
                ))
            # Значения НЕ словари и они равны
            elif value1 is value2 or value1 == value2:
                diffs.append(DiffItem(
                    result="equal", 
                    key=key, 
                    old_value=value1,
                    new_value=value2, 
                ))
            # Одно из значений НЕ словарь и они НЕ равны
            else:
                diffs.append(DiffItem(
                    result="change",
                    key=key,
                    old_value=value1,
                    new_value=value2,
                ))
        # Ключ есть в первом словаре, но его нет во втором (удалили)
        elif key in dict1 and key not in dict2:
            diffs.append(DiffItem(
                result="remove",
                key=key,
                old_value=value1,
            ))
        # Ключа нет в первом словаре и он есть во втором (добавили)
        elif key not in dict1 and key in dict2:
            diffs.append(DiffItem(
                result="add",
                key=key,
                new_value=value2,
            ))
    
    return diffs