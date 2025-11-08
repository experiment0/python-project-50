from gendiff.diffs_model import get_diffs
from gendiff.diffs_views import DiffViewType, get_diffs_view
from gendiff.utils.file_reader import get_data_from_file


def generate_diff(
    file_path1: str, 
    file_path2: str, 
    view_type: DiffViewType = "stylish"
) -> str:
    dict1 = get_data_from_file(file_path1)
    dict2 = get_data_from_file(file_path2)
    
    diffs = get_diffs(dict1, dict2)
    diffs_view = get_diffs_view(diffs, view_type)
    
    return diffs_view
