from gendiff import generate_diff


def test_deep_json_diff_with_stylish_colored_format(test_data_path):
    FILES_PATH = f"{test_data_path}/deep_json"
    
    file1_path = f"{FILES_PATH}/file1.json"
    file2_path = f"{FILES_PATH}/file2.json"
    # diff_stylish_colored.txt
    diff_stylish_path = f"{FILES_PATH}/diff_stylish_colored.txt"
    
    with open(diff_stylish_path) as file:
        diff_stylish_colored = file.read().replace("\\x1b", "\x1b")
        assert generate_diff(
            file1_path, file2_path, view_type="stylish_colored"
        ) == diff_stylish_colored


def test_deep_yml_diff_with_stylish_colored_format(test_data_path):
    FILES_PATH = f"{test_data_path}/deep_yml"
    
    file1_path = f"{FILES_PATH}/file1.yml"
    file2_path = f"{FILES_PATH}/file2.yml"
    diff_stylish_path = f"{FILES_PATH}/diff_stylish_colored.txt"
    
    with open(diff_stylish_path) as file:
        diff_stylish_colored = file.read().replace("\\x1b", "\x1b")
        assert generate_diff(
            file1_path, file2_path, view_type="stylish_colored"
        ) == diff_stylish_colored