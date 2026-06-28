from pathlib import Path

def remove_file(path):

    path_for_remove = Path(path)

    if path_for_remove.exists():
        path_for_remove.unlink()
        return True
    else:
        return False