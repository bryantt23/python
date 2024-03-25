import datetime
import os
import shutil
from pathlib import Path


def read_file(file_path):
    with open(file_path) as f:
        content = f.read()
    return content


def write_to_file(file_path, content):
    with open(file_path, "a") as f:
        f.write(content)


def list_directory_contents(dir_path):
    dir = os.listdir(dir_path)
    return dir


def walk_directory(dir_path):
    res = set()
    for root, dirs, files in os.walk(dir_path):
        res.add(root)
        for file in files:
            res.add(os.path.join(root, file))
    return res


def check_file_exists(file_path):
    return os.path.isfile(file_path)


def get_file_properties(file_path):
    return {"size": os.path.getsize(file_path),
            "mod_date": os.path.getmtime(file_path)}

# Tests


def run_tests():
    # # Test reading from a file
    # assert read_file(
    #     "test_dir/test_file.txt") == "Hello, World!", "Should read file contents."

    # # Test writing to a file
    # write_to_file("test_dir/test_file.txt", "\nGoodbye, World!")
    # with open("test_dir/test_file.txt", "r") as f:
    #     content = f.read()
    # print('content')
    # print(content)
    # assert "Goodbye, World!" in content, "Should append content to the file."

    # # Test listing directory contents
    contents = list_directory_contents("test_dir")
    assert "sub_dir" in contents and "test_file.txt" in contents, "Should list all directory contents."

    # Test walking a directory
    expected_paths = {
        os.path.normpath("test_dir"),
        os.path.normpath("test_dir/sub_dir"),
        os.path.normpath("test_dir/test_file.txt"),
        os.path.normpath("test_dir/sub_dir/test_file_2.txt")
    }
    assert set(walk_directory(
        "test_dir")) == expected_paths, "Should list all files and directories in the tree."

    # Test file existence
    assert check_file_exists(
        "test_dir/test_file.txt") == True, "File should exist."

    # Test file properties
    properties = get_file_properties("test_dir/test_file.txt")
    assert properties["size"] > 0, "File size should be greater than 0."
    assert type(properties["mod_date"]
                ) is float, "Modification date should be a timestamp."

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
