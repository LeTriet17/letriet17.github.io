import os

def list_files(directory):
    """
    List all files in the specified directory.
    """
    files = []
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            files.append(os.path.join(directory, filename))
    return files

# Example usage:
directory_path = "love"
files_in_directory = list_files(directory_path)
print(files_in_directory)
