from typing import List

from gendiff.diffs_model import DiffsType
from gendiff.formatters.plain_helpers import dict_value_to_str
    

def format_to_plain(diffs: DiffsType, property_path: List[str] = []) -> str:
    diffs_lines = []
    
    for d in diffs:
        current_property_path = property_path + [d.key]
        property_name = ".".join(current_property_path)
        
        match d.result:
            case "equal":
                if d.children is not None:
                    children_view = format_to_plain(
                        d.children,
                        current_property_path,
                    )
                    diffs_lines.append(children_view)
            case "add":
                new_value_str = dict_value_to_str(d.new_value)
                diffs_lines.append(
                    f"Property '{property_name}' was added " + 
                    f"with value: {new_value_str}"
                )
            case "remove":
                diffs_lines.append(
                    f"Property '{property_name}' was removed"
                )
            case "change":
                old_value_str = dict_value_to_str(d.old_value)
                new_value_str = dict_value_to_str(d.new_value)
                diffs_lines.append(
                    f"Property '{property_name}' was updated. " + 
                    f"From {old_value_str} to {new_value_str}"
                )
    
    return "\n".join(diffs_lines)
