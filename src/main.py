import sys

from create_site import get_static_files, PROJECT_ROOT
from generate_page import generate_pages_recursive


def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    get_static_files()
    generate_pages_recursive(
        PROJECT_ROOT / "content",
        PROJECT_ROOT / "template.html",
        PROJECT_ROOT / "docs",
        basepath,
    )


if __name__ == "__main__":
    main()
