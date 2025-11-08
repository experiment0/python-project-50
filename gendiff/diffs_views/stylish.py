from gendiff.diffs_model import DiffsType
from gendiff.diffs_views.stylish_helpers import (
    INDENT,
    get_diff_line,
    get_multilines_value_with_indent,
)


def get_stylish_view(diffs: DiffsType, is_colored: bool = False) -> str:
    level = 1
    diffs_lines = []
    diffs_lines.append("{")
    
    for d in diffs:
        diff_line_params = {
            "key": d.key, "level": level, "is_colored": is_colored,
        }
        
        match d.result:
            case "equal":
                if d.children is not None:
                    children_view = get_stylish_view(d.children, is_colored)
                    children_view = get_multilines_value_with_indent(
                        children_view,
                        INDENT * level
                    )
                    diffs_lines.append(get_diff_line(
                        result="equal", value=children_view, **diff_line_params
                    ))
                else:
                    diffs_lines.append(get_diff_line(
                        result="equal", value=d.old_value, **diff_line_params
                    ))
            case "add":
                diffs_lines.append(get_diff_line(
                    result="add", value=d.new_value, **diff_line_params
                ))
            case "remove":
                diffs_lines.append(get_diff_line(
                    result="remove", value=d.old_value, **diff_line_params
                ))
            case "change":
                diffs_lines.append(get_diff_line(
                    result="remove", value=d.old_value, **diff_line_params
                ))
                diffs_lines.append(get_diff_line(
                    result="add", value=d.new_value, **diff_line_params
                ))                
       
    diffs_lines.append("}")
    
    return "\n".join(diffs_lines)