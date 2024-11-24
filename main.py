import fileorganizer as fog


def main():
    base_directory = "./example/"
    directory_structure = {
        "raw": {},
        "log": {
            "output": {
                "log1.bin": None,
                "log2.bin": None,
                "log3bin": None  # make a wrong name to check re.search() function
            },
            "log1.txt": "log1\n",
            "log2.txt": "log2\n",
            "log3txt": "log3\n"  # make a wrong name to check re.search() function
        },
        "review": {
            "baseline": {},
            "development": {}
        },
        "readme.txt": "This is a readme file."
    }
    # create directory structure
    fog.create_directory_structure(base_directory, directory_structure)

    # move file
    fog.move_files(source_folder=base_directory, target_folder=base_directory + "raw", pattern=r"\.bin")

    # merge file
    fog.merge_files(source_folder=base_directory, target_file=base_directory + "log/all_log.txt", pattern=r"log.*\.txt")


if __name__ == "__main__":
    main()
