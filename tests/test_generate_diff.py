from gendiff import generate_diff


def test_flat_json_diff_with_stylish_format(test_data_path):
    FILES_PATH = f"{test_data_path}/flat_json"
    
    file1_path = f"{FILES_PATH}/file1.json"
    file2_path = f"{FILES_PATH}/file2.json" 
    diff_stylish_path = f"{FILES_PATH}/diff_stylish.txt"
    
    with open(diff_stylish_path) as file:
        diff_stylish = file.read()
        assert generate_diff(
            file1_path, file2_path, view_type="stylish"
        ) == diff_stylish
    

def test_flat_yml_diff_with_stylish_format(test_data_path):
    FILES_PATH = f"{test_data_path}/flat_yml"
    
    file1_path = f"{FILES_PATH}/file1.yml"
    file2_path = f"{FILES_PATH}/file2.yml" 
    diff_stylish_path = f"{FILES_PATH}/diff_stylish.txt"
    
    with open(diff_stylish_path) as file:
        diff_stylish = file.read()
        assert generate_diff(
            file1_path, file2_path, view_type="stylish"
        ) == diff_stylish


def test_deep_json_diff_with_stylish_format(test_data_path):
    FILES_PATH = f"{test_data_path}/deep_json"
    
    file1_path = f"{FILES_PATH}/file1.json"
    file2_path = f"{FILES_PATH}/file2.json" 
    diff_stylish_path = f"{FILES_PATH}/diff_stylish.txt"
    
    with open(diff_stylish_path) as file:
        diff_stylish = file.read()
        assert generate_diff(
            file1_path, file2_path, view_type="stylish"
        ) == diff_stylish


def test_deep_yml_diff_with_stylish_format(test_data_path):
    FILES_PATH = f"{test_data_path}/deep_yml"
    
    file1_path = f"{FILES_PATH}/file1.yml"
    file2_path = f"{FILES_PATH}/file2.yml" 
    diff_stylish_path = f"{FILES_PATH}/diff_stylish.txt"
    
    with open(diff_stylish_path) as file:
        diff_stylish = file.read()
        assert generate_diff(
            file1_path, file2_path, view_type="stylish"
        ) == diff_stylish


def test_deep_json_diff_with_plain_format(test_data_path):
    FILES_PATH = f"{test_data_path}/deep_json"
    
    file1_path = f"{FILES_PATH}/file1.json"
    file2_path = f"{FILES_PATH}/file2.json" 
    diff_plain_path = f"{FILES_PATH}/diff_plain.txt"
    
    with open(diff_plain_path) as file:
        diff_plain = file.read()
        assert generate_diff(
            file1_path, file2_path, view_type="plain"
        ) == diff_plain


def test_deep_yml_diff_with_plain_format(test_data_path):
    FILES_PATH = f"{test_data_path}/deep_yml"
    
    file1_path = f"{FILES_PATH}/file1.yml"
    file2_path = f"{FILES_PATH}/file2.yml" 
    diff_plain_path = f"{FILES_PATH}/diff_plain.txt"
    
    with open(diff_plain_path) as file:
        diff_plain = file.read()
        assert generate_diff(
            file1_path, file2_path, view_type="plain"
        ) == diff_plain