import os
from datetime import datetime


def setup_test_environment():
    os.makedirs("test_dir/sub_dir", exist_ok=True)
    with open("test_dir/test_file.txt", "w") as f:
        f.write("Hello, World!")
    with open("test_dir/sub_dir/test_file_2.txt", "w") as f:
        f.write("Another file.")


setup_test_environment()
