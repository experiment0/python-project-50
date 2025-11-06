from gendiff.diffs_model import get_diffs
from gendiff.formatters import DiffViewType, format_diffs
from gendiff.utils.file_reader import get_data_from_file


def generate_diff(
    file_path1: str, 
    file_path2: str, 
    view_type: DiffViewType = "stylish"
) -> str:
    dict1 = get_data_from_file(file_path1)
    dict2 = get_data_from_file(file_path2)
    
    diffs = get_diffs(dict1, dict2)
    formatted_diffs = format_diffs(diffs, view_type)
    
    return formatted_diffs
