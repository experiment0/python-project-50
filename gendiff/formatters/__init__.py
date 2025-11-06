from typing import Literal

from gendiff.diffs_model import DiffsType
from gendiff.formatters.json import format_to_json
from gendiff.formatters.plain import format_to_plain
from gendiff.formatters.stylish import format_to_stylish

DiffViewType = Literal["stylish", "stylish_colored", "json", "plain"]


def format_diffs(
    diffs: DiffsType, 
    view_type: DiffViewType = "stylish"
) -> str:
    match view_type:
        case "stylish":
            return format_to_stylish(diffs)
        case "stylish_colored":
            return format_to_stylish(diffs, is_colored=True)
        case "json":
            return format_to_json(diffs)
        case "plain":
            return format_to_plain(diffs)
        case _:
            raise ValueError("Unknown name for format output.")


__all__ = [
    "DiffViewType",
    "format_diffs",
]
