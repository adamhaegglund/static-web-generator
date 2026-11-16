import os
import shutil
from pathlib import Path

# Resolve paths relative to this file, not the current working directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent
PATH_STATIC = PROJECT_ROOT / "static"
PATH_PUBLIC = PROJECT_ROOT / "public"


def get_static_files() -> None:
    # Safety check: never delete anything outside the project
    if PATH_PUBLIC.resolve().parent != PROJECT_ROOT:
        raise ValueError(f"Refusing to delete {PATH_PUBLIC}: not inside {PROJECT_ROOT}")

    if PATH_PUBLIC.exists():
        print(f"Removing {PATH_PUBLIC}")
        shutil.rmtree(PATH_PUBLIC)

    copy_files(PATH_STATIC, PATH_PUBLIC)


def copy_files(static, public) -> None:
    if not os.path.exists(public):
        os.mkdir(public)

    for filename in os.listdir(static):
        if filename == ".DS_Store":
            continue
        from_path = os.path.join(static, filename)
        to_path = os.path.join(public, filename)
        print(f"- From {from_path} -> {to_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, to_path)
        else:
            copy_files(from_path, to_path)


if __name__ == "__main__":
    get_static_files()
