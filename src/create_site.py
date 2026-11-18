import os
import shutil
from pathlib import Path

# Resolve paths relative to this file, not the current working directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent
PATH_STATIC = PROJECT_ROOT / "static"
PATH_DOCS = PROJECT_ROOT / "docs"


def get_static_files() -> None:
    if PATH_DOCS.resolve().parent != PROJECT_ROOT:
        raise ValueError(f"Refusing to delete {PATH_DOCS}: not inside {PROJECT_ROOT}")

    if PATH_DOCS.exists():
        print(f"Removing {PATH_DOCS}")
        shutil.rmtree(PATH_DOCS)

    copy_files(PATH_STATIC, PATH_DOCS)


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

def generate_page(from_path, template_path, dest_path) -> None:
    


    print(f"Generating page from {from_path} to {dest_path} using {template_path}")


if __name__ == "__main__":
    get_static_files()
