from parentnode import ParentNode
from leafnode import LeafNode
from markdown_to_blocks import markdown_to_blocks
from block_type import BlockType, block_to_block_type
from text_to_textnodes import text_to_textnodes
from textnode_to_html import text_node_to_html_node


def text_to_children(text):
    nodes = text_to_textnodes(text)
    return [text_node_to_html_node(node) for node in nodes]


def paragraph_to_html(block):
    children = text_to_children(block.replace("\n", " "))
    return ParentNode("p", children)


def heading_to_html(block):
    level = len(block.split(" ")[0])
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def codeblock_to_html(block):
    inner = block.strip()
    if inner.startswith("```") and inner.endswith("```"):
        inner = inner[3:-3]
    code_node = LeafNode("code", inner)
    return ParentNode("pre", [code_node])


def quote_to_html(block):
    stripped = "\n".join([line.lstrip("> ") for line in block.split("\n")])
    joined = " ".join(stripped.split("\n"))
    children = text_to_children(joined)
    return ParentNode("blockquote", children)


def unordered_list_to_html(block):
    items = []
    for line in block.split("\n"):
        text = line.lstrip("- ").strip()
        children = text_to_children(text)
        items.append(ParentNode("li", children))
    return ParentNode("ul", items)


def ordered_list_to_html(block):
    items = []
    for line in block.split("\n"):
        text = line.split(". ", 1)[1]
        children = text_to_children(text)
        items.append(ParentNode("li", children))
    return ParentNode("ol", items)


def block_to_html(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html(block)
    if block_type == BlockType.HEADING:
        return heading_to_html(block)
    if block_type == BlockType.CODE:
        return codeblock_to_html(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html(block)
    if block_type == BlockType.UNORDERED_LIST:
        return unordered_list_to_html(block)
    if block_type == BlockType.ORDERED_LIST:
        return ordered_list_to_html(block)
    raise ValueError("Unknown block type")


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = [block_to_html(block) for block in blocks]
    return ParentNode("div", children)
