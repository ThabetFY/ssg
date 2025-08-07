import sys
from copy_to_dir import copy_to_dir
from generate_page import generate_pages_recursive


def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    copy_to_dir("static", "docs")
    generate_pages_recursive(basepath, "content", "template.html", "docs")


if __name__ == "__main__":
    main()
