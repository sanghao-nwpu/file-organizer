"""
file-organizer

Author: sanghao_nwpu
Date: [2024.11.24]
Description: A script to manage files and directories, including features for merging files,
             moving files with filtering options, creating directory structures, and detecting file encodings.
"""


import os
import shutil
import chardet
import re


def get_file_encoding(file_path: str) -> str:
    """
    get file encoding
    :param file_path: file path
    :return: file encoding
    """
    with open(file_path, 'rb') as file:
        encoding = chardet.detect(file.read())['encoding']
    return encoding


def create_directory_structure(base_dir: str, structure: dict) -> None:
    """
    create directory structure recursively
    :param base_dir: the base directory
    :param structure: the directory structure, include directories and files
    :return: none
    """
    for name, sub_structure in structure.items():
        path = os.path.join(base_dir, name)
        if isinstance(sub_structure, dict):
            # create directory
            os.makedirs(path, exist_ok=True)
            print(f"Directory '{name}' created at '{path}'")
            # recursively create sub-directories and files
            create_directory_structure(path, sub_structure)
        else:
            # create file
            with open(path, 'w', encoding='utf-8') as file:
                if isinstance(sub_structure, str):
                    file.write(sub_structure)
                else:
                    file.write("")
                print(f"File '{name}' created at '{path}'")


def move_files(source_folder: str, target_folder: str, pattern: str = None, copy_files: bool = False) -> None:
    """
    move files with specific keyword
    :param source_folder: input folder
    :param target_folder: output folder
    :param pattern: pattern to filter files, if None, move all files
    :param copy_files: copy file flag, default is False
    :return: none
    """
    moved_files_count = 0
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    for subdir, _, files in os.walk(source_folder):
        if os.path.abspath(subdir) == os.path.abspath(target_folder):
            continue
        for file in files:
            if re.search(pattern, file):
                if copy_files:
                    shutil.copy(os.path.join(subdir, file), os.path.join(target_folder, file))
                    print(f"File '{file}' copied to '{target_folder}'")
                else:
                    shutil.move(os.path.join(subdir, file), os.path.join(target_folder, file))
                    print(f"File '{file}' moved to '{target_folder}'")
                moved_files_count += 1
    if copy_files:
        print(f"Copied {moved_files_count} files with keyword '{pattern}' from '{source_folder}' to '{target_folder}'")
    else:
        print(f"Moved {moved_files_count} files with keyword '{pattern}' from '{source_folder}' to '{target_folder}'")


def merge_files(source_folder: str, target_file: str, pattern: str = None) -> None:
    """
    merge files in a folder to a single file
    :param source_folder: folder containing files with keyword
    :param target_file: output file path
    :param pattern: pattern to filter files, if None, merge all files
    :return: none
    """
    try:
        with open(target_file, 'w', encoding='utf-8') as target:
            for subdir, _, files in os.walk(source_folder):
                for file in files:
                    if pattern and not re.search(pattern, file):
                        continue
                    # skip target file
                    if os.path.abspath(target_file) == os.path.abspath(os.path.join(subdir, file)):
                        continue
                    # check file encoding
                    encoding = get_file_encoding(os.path.join(subdir, file))
                    print(f"Encoding of file '{file}' is '{encoding}'")
                    # read file and write to target file
                    with open(os.path.join(subdir, file), 'r', encoding=encoding) as source:
                        target.write(source.read())
                        print(f"File '{file}' merged to '{target_file}'")
    except Exception as e:
        print(f"Error occurred while merging files: {e}")
