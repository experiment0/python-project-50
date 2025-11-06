import json

from gendiff.diffs_model import DiffsType

INDENT_SYMBOL = " "
INDENT_LENGTH = 4
INDENT = INDENT_SYMBOL * INDENT_LENGTH


def format_to_json(diffs: DiffsType) -> str:
    diffs_for_json = [d.model_dump(exclude_none=True) for d in diffs]
    dict_for_json = {"diffs": diffs_for_json}
    
    return json.dumps(dict_for_json, indent=INDENT)
