import os
import shutil


def copy_to_dir(source: str, destination: str):
    if source == "" or destination == "":
        raise ValueError("ERROR: source or destination can not be empty")

    if os.path.exists(destination):
        shutil.rmtree(destination)

    os.mkdir(destination)

    for entry in os.listdir(source):
        entry_path = os.path.join(source, entry)
        if os.path.isdir(entry_path):
            copy_to_dir(entry_path, os.path.join(destination, entry))
        else:
            shutil.copy(entry_path, destination)
            print(f"copying {entry} from {source} to {destination}")
