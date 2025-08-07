from copy_to_dir import copy_to_dir
from generate_page import generate_pages_recursive


def main():
    copy_to_dir("static", "public")
    generate_pages_recursive("content", "template.html", "public")


if __name__ == "__main__":
    main()
