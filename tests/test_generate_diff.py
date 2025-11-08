import pytest

from gendiff import generate_diff


test_params = [
    ("deep", "file_1_1.json", "file_1_2.json", "stylish", "diffs_format_stylish.txt"),
    ("deep", "file_1_1.json", "file_1_2.json", "stylish_colored", "diffs_format_stylish_colored.txt"),    
    ("deep", "file_1_1.json", "file_1_2.json", "plain", "diffs_format_plain.txt"),
    ("deep", "file_1_1.json", "file_1_2.json", "json", "diffs_format_json.json"),
    
    ("deep", "file_2_1.yml", "file_2_2.yml", "stylish", "diffs_format_stylish.txt"),
    ("deep", "file_2_1.yml", "file_2_2.yml", "stylish_colored", "diffs_format_stylish_colored.txt"),
    ("deep", "file_2_1.yml", "file_2_2.yml", "plain", "diffs_format_plain.txt"),
    ("deep", "file_2_1.yml", "file_2_2.yml", "json", "diffs_format_json.json"),
    
    ("flat", "file_1_1.json", "file_1_2.json", "stylish", "diffs_format_stylish.txt"),
    
    ("flat", "file_2_1.yml", "file_2_2.yml", "stylish", "diffs_format_stylish.txt"),
]

@pytest.mark.parametrize("folder, file1, file2, format_name, diffs_file", test_params)
def test_generate_diff(folder, file1, file2, format_name, diffs_file, test_data_path):
    FILES_PATH = f"{test_data_path}/{folder}"
    
    file1_path = f"{FILES_PATH}/{file1}"
    file2_path = f"{FILES_PATH}/{file2}" 
    diffs_path = f"{FILES_PATH}/{diffs_file}"
    
    with open(diffs_path) as file:
        diffs_str = file.read()
        
        if (format_name == "stylish_colored"):            
            diffs_str = diffs_str.replace("\\x1b", "\x1b")
        
        assert generate_diff(
            file1_path, file2_path, view_type=format_name
        ) == diffs_str
