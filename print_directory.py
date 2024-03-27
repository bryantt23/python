import os


def print_directory():
    indent = "  "
    startpath = "./stories"
    for root, dirs, files in os.walk(startpath):
        depth = root.replace(startpath, "").count(os.sep)
        indent_str = indent*depth
        print(f"{indent_str}{os.path.basename(root)}")
        subindent_str = indent*(depth+1)
        for file in files:
            print(f"{subindent_str}"+file)


print_directory()
