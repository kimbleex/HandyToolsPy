import os

def dir_tree(path: str, indent: str = ''):
    """
    Print the directory tree of the specified path.

    :param path: The directory path to print the tree for.
    :param indent: The indentation used for subdirectories.
    """
    if indent == '':
        print(path)
    try:
        items = os.listdir(path)
    except OSError as e:
        print(f"Error accessing {path}: {e}")
        return
    for index, item in enumerate(items):
        is_last = index == len(items) - 1
        
        prefix = '└── ' if is_last else '├── '
        print(indent + prefix + item)
        full_path = os.path.join(path, item)

        if os.path.isdir(full_path):
            new_indent = indent + ('    ' if is_last else '│   ')
            dir_tree(full_path, new_indent)
            