import os
import sys

def map_directory(root_dir):
    """
    Recursively walks through a directory and prints its structure with indentation.
    
    Args:
        root_dir (str): The absolute or relative path to the directory to map.
    """
    # os.walk() generates the file and directory names in a directory tree
    # by walking the tree either top-down or bottom-up.
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Calculate the depth of the current directory relative to the start
        level = dirpath.replace(root_dir, '').count(os.sep)
        
        # Create indentation based on the depth
        indent = ' ' * 4 * level
        
        # Print the current directory name
        # os.path.basename() gets the final component of the path
        print(f'{indent}└── {os.path.basename(dirpath)}/')
        
        # Create indentation for the files inside this directory
        sub_indent = ' ' * 4 * (level + 1)
        
        # Print all files in the current directory
        for f in filenames:
            print(f'{sub_indent}├── {f}')


if __name__ == "__main__":
    # The script can be run with a command-line argument specifying the directory.
    # If no argument is given, it defaults to the current directory ('.').
    try:
        # Use the directory from the first command-line argument
        start_path = sys.argv[1]
    except IndexError:
        # Or default to the current working directory
        start_path = '.'

    # Check if the provided path is a valid directory
    if not os.path.isdir(start_path):
        print(f"Error: The directory '{start_path}' does not exist.")
        sys.exit(1)

    print(f"Mapping directory: {os.path.abspath(start_path)}")
    print("-" * 40)
    map_directory(start_path)
