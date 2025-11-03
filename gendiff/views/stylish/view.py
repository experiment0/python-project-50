from gendiff.models.calc_diff import DiffsType
from gendiff.views.stylish.utils import (
    INDENT,
    get_diff_line,
    get_multilines_value_with_indent,
)


def get_stylish_view(diffs: DiffsType, level=1) -> str:
    diffs_lines = []
    diffs_lines.append("{")
    
    for d in diffs:
        match d.result:
            case "equal":
                if d.children is not None:
                    children_view = get_stylish_view(d.children, 1)
                    children_view = get_multilines_value_with_indent(
                        children_view,
                        INDENT * level
                    )
                    diffs_lines.append(
                        get_diff_line(level, "equal", d.key, children_view)
                    )
                else:
                    diffs_lines.append(
                        get_diff_line(level, "equal", d.key, d.old_value)
                    )
            case "add":
                diffs_lines.append(
                    get_diff_line(level, "add", d.key, d.new_value)
                )
            case "remove":
                diffs_lines.append(
                    get_diff_line(level, "remove", d.key, d.old_value)
                )
            case "change":
                diffs_lines.append(
                    get_diff_line(level, "remove", d.key, d.old_value)
                )
                diffs_lines.append(
                    get_diff_line(level, "add", d.key, d.new_value)
                )                
       
    diffs_lines.append("}")
    
    return "\n".join(diffs_lines)