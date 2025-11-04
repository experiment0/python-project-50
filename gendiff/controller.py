from gendiff.models.calc_diff import get_diffs
from gendiff.utils.file_parsing import get_data_from_file
from gendiff.views.main import DiffViewType, get_diffs_view


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