from gendiff import generate_diff


def test_plain_json_diff(test_data_path):
    FILES_PATH = f"{test_data_path}/plain_json"
    
    file1_path = f"{FILES_PATH}/file1.json"
    file2_path = f"{FILES_PATH}/file2.json" 
    diff_path = f"{FILES_PATH}/diff.txt"
    
    with open(diff_path) as file:
        diff = file.read()
        assert generate_diff(file1_path, file2_path) == diff
