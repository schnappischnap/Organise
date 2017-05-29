import json
import os
import sys


def get_data(filename):
    """
    Reads a JSON file to get the folder destinations and exclusions
    :param filename: the JSON file path
    :return: a {extension : destination directory} dict and filenames to ignore
    """
    with open(filename) as f:
        data = json.load(f)
        folders = {ext: dst_dir
                   for dst_dir in data["Directories"]
                   for ext in data["Directories"][dst_dir]}
        exclude = [f for f in data["Exclude"]]
        exclude.append(filename)                       # ignore the JSON file
        exclude.append(os.path.basename(sys.argv[0]))  # ignore the script file
    return folders, exclude


def move_files(src_dir, folders, exclude=None):
    """
    Moves all files in the directory to the specified folders based on extension
    :param src_dir: the source directory to organise
    :param folders: a dict of {extension : destination directory}
    :param exclude: a list of files to ignore
    """
    if exclude is None:
        exclude = []

    for filename in os.listdir(src_dir):
        src_path = os.path.join(src_dir, filename)  # full path to file
        if not os.path.isfile(src_path) or filename in exclude:
            continue

        extension = os.path.splitext(filename)[1].lower()  # file extension
        if extension not in folders:
            continue

        dst_dir = os.path.join(src_dir, folders[extension])  # folder to move to
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)

        os.rename(src_path, os.path.join(dst_dir, filename))  # move file
        print("{} \t -> \t {}".format(filename, dst_dir))

if __name__ == '__main__':
    # organise files in the cwd if no other directory specified
    use_cwd = len(sys.argv) == 1 or not os.path.exists(sys.argv[1])
    directory = os.getcwd() if use_cwd else sys.argv[1]

    move_files(directory, *get_data('Organise.json'))
