from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block):
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    if block.startswith("#"):
        hashes, _, rest = block.partition(" ")
        if 1 <= len(hashes) <= 6 and rest.strip():
            return BlockType.HEADING
    lines = block.split("\n")
    if all(line.strip().startswith(">") for line in lines):
        return BlockType.QUOTE
    if all(line.strip().startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    if all(line.strip().startswith(f"{i+1}. ") for i, line in enumerate(lines)):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
