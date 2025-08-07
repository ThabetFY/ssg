import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node


def generate_pages_recursive(
    dir_path_content: str, template_path: str, dest_dir_path: str
):
    for entry in os.listdir(dir_path_content):
        entry_path = os.path.join(dir_path_content, entry)
        entry_dest_path = os.path.join(dest_dir_path, entry)
        if os.path.isdir(entry_path):
            generate_pages_recursive(entry_path, template_path, entry_dest_path)
        else:
            entry_dest_path = Path(entry_dest_path).with_suffix(".html")
            generate_page(entry_path, template_path, entry_dest_path)


def generate_page(from_path: str, template_path: str, dest_path: Path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as file:
        markdown = file.read()
        file.close()

    with open(template_path, "r") as file:
        template = file.read()
        file.close()

    title = extract_title(markdown)
    content = markdown_to_html_node(markdown).to_html()

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", content)

    dest_path_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_path_dir):
        os.makedirs(dest_path_dir)
    with open(dest_path, "w") as file:
        file.write(template)


def extract_title(markdown: str):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")
