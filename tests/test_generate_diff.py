import pytest

from gendiff import generate_diff

file_json_1 = "file_1_1.json"
file_json_2 = "file_1_2.json"

file_yml_1 = "file_2_1.yml"
file_yml_2 = "file_2_2.yml"

diffs_files = {
    "stylish": "diffs_format_stylish.txt",
    "stylish_colored": "diffs_format_stylish_colored.txt",
    "plain": "diffs_format_plain.txt",
    "json": "diffs_format_json.json",
}

test_params = [
    ("deep", file_json_1, file_json_2, "stylish", diffs_files["stylish"]),
    (
        "deep", file_json_1, file_json_2, 
        "stylish_colored", diffs_files["stylish_colored"]
    ), 
    ("deep", file_json_1, file_json_2, "plain", diffs_files["plain"]),
    ("deep", file_json_1, file_json_2, "json", diffs_files["json"]),
    
    ("deep", file_yml_1, file_yml_2, "stylish", diffs_files["stylish"]),
    (
        "deep", file_yml_1, file_yml_2, 
        "stylish_colored", diffs_files["stylish_colored"]
    ),
    ("deep", file_yml_1, file_yml_2, "plain", diffs_files["plain"]),
    ("deep", file_yml_1, file_yml_2, "json", diffs_files["json"]),
    
    ("flat", file_json_1, file_json_2, "stylish", diffs_files["stylish"]), 
    ("flat", file_yml_1, file_yml_2, "stylish", diffs_files["stylish"]),
]


@pytest.mark.parametrize(
    "folder, file1, file2, format_name, diffs_file", test_params
)
def test_generate_diff(
    folder, file1, file2, format_name, diffs_file, test_data_path
):
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
