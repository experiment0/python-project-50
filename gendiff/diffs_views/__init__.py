from typing import Literal

from gendiff.diffs_model import DiffsType
from gendiff.diffs_views.json import get_json_view
from gendiff.diffs_views.plain import get_plain_view
from gendiff.diffs_views.stylish import get_stylish_view

DiffViewType = Literal["stylish", "stylish_colored", "json", "plain"]


def get_diffs_view(
    diffs: DiffsType, 
    view_type: DiffViewType = "stylish"
) -> str:
    match view_type:
        case "stylish":
            return get_stylish_view(diffs)
        case "stylish_colored":
            return get_stylish_view(diffs, is_colored=True)
        case "json":
            return get_json_view(diffs)
        case "plain":
            return get_plain_view(diffs)
        case _:
            raise ValueError("Unknown name for format output.")


__all__ = [
    "DiffViewType",
    "get_diffs_view",
]
