import os
import shutil
from textnode import TextNode, TextType
from page_generator import generate_page, generate_pages_recursive


def copy_static(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copy_static(s, d)
        else:
            shutil.copy(s, d)
            print(f"Copied: {d}")


def main():
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(node)
    copy_static("static", "public")
    generate_pages_recursive("content", "template.html", "public")


if __name__ == "__main__":
    main()
