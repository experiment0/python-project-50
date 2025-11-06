from typing import Dict, Optional, Union

from gendiff.diffs_model import (
    DictValueType,
    ResultType,
)
from gendiff.utils.colored import colored

INDENT_SYMBOL = " "
INDENT_LENGTH = 4
INDENT = INDENT_SYMBOL * INDENT_LENGTH


result_to_symbol_map: Dict[ResultType, str] = {
    "equal":  " ",
    "add":    "+",
    "remove": "-",
}


def get_multilines_value_with_indent(value: str, indent: str) -> str:
    lines = value.split("\n")
    lines_with_indent = [
        (indent + line if index > 0 else line) 
        for index, line in enumerate(lines) 
    ]
    return "\n".join(lines_with_indent)


def primitive_value_to_str(
    value: Optional[Union[bool, str, int, float, list]]
) -> str:
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if isinstance(value, str):
        return value
    return str(value)


def dict_value_to_str(data: DictValueType) -> str:
    if not isinstance(data, dict):
        return str(primitive_value_to_str(data))
    
    lines = ["{"]
    
    def walk(current_data, current_level):
        current_indent = INDENT * current_level
        
        for key, value in current_data.items(): 
            if not isinstance(value, dict):
                lines.append(
                    f"{current_indent}{key}: {primitive_value_to_str(value)}"
                )
            else:
                lines.append(
                    f"{current_indent}{key}: {{"
                )
                walk(value, current_level + 1)
                lines.append(
                    f"{current_indent}}}"
                )
    
    walk(data, 1)
    
    lines.append("}")
    
    return "\n".join(lines)


def get_indent_before_symbol(level: int) -> str:
    # Убираем 2 символа с конца, 
    # чтобы вписать знак ("+" / "-" / " ") и пробел перед именем ключа
    return (INDENT * level)[:-2]


def get_diff_line(level: int, result: ResultType, key, value, is_colored):
    value_str = dict_value_to_str(value)
    
    if isinstance(value, dict):        
        value_str = get_multilines_value_with_indent(value_str, INDENT * level)
    
    symbol = result_to_symbol_map[result]
    
    if is_colored:
        if result == "add":
            symbol = colored(symbol, "green")
        elif result == "remove":
            symbol = colored(symbol, "red")
   
    return f"{get_indent_before_symbol(level)}{symbol} {key}: {value_str}"
