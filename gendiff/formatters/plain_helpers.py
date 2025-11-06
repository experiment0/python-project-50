from gendiff.diffs_model import DictValueType


def dict_value_to_str(value: DictValueType) -> str:
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if isinstance(value, str):
        return f"'{value}'"
    if isinstance(value, (int, float)):
        return str(value)
    return "[complex value]"
