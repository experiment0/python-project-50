from typing import Literal

from gendiff.models.calc_diff import DiffsType
from gendiff.views.json.view import get_json_view
from gendiff.views.plain.view import get_plain_view
from gendiff.views.stylish.view import get_stylish_view

DiffViewType = Literal["stylish", "json", "plain"]


def get_diffs_view(
    diffs: DiffsType, 
    view_type: DiffViewType = "stylish"
) -> str:
    match view_type:
        case "stylish":
            return get_stylish_view(diffs)
        case "json":
            return get_json_view(diffs)
        case "plain":
            return get_plain_view(diffs)
        case _:
            raise ValueError("Unknown name for format output.")