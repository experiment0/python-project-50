from gendiff import generate_diff


def test_deep_json_diff_with_json_format(test_data_path):
    FILES_PATH = f"{test_data_path}/deep_json"
    
    file1_path = f"{FILES_PATH}/file1.json"
    file2_path = f"{FILES_PATH}/file2.json" 
    diff_json_path = f"{FILES_PATH}/diff_json.json"
    
    with open(diff_json_path) as file:
        diff_json = file.read()
        assert generate_diff(
            file1_path, file2_path, view_type="json"
        ) == diff_json


def test_deep_yml_diff_with_json_format(test_data_path):
    FILES_PATH = f"{test_data_path}/deep_yml"
    
    file1_path = f"{FILES_PATH}/file1.yml"
    file2_path = f"{FILES_PATH}/file2.yml" 
    diff_json_path = f"{FILES_PATH}/diff_json.json"
    
    with open(diff_json_path) as file:
        diff_json = file.read()
        assert generate_diff(
            file1_path, file2_path, view_type="json"
        ) == diff_json