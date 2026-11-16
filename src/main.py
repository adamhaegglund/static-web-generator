from create_site import get_static_files, PROJECT_ROOT
from generate_page import generate_pages_recursive


def main():
    get_static_files()
    generate_pages_recursive(
        PROJECT_ROOT / "content",
        PROJECT_ROOT / "template.html",
        PROJECT_ROOT / "public",
    )


if __name__ == "__main__":
    main()
