import os
import sys
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
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    if os.path.exists("docs"):
        shutil.rmtree("docs")
    copy_static("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)


if __name__ == "__main__":
    main()
