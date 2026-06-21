from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    OLIST = "ordered_list"
    ULIST = "unordered_list"

def markdown_to_blocks(markdown):
    new_list = []
    mark = markdown.split('\n\n')
    for i in mark:
        stripped = i.strip()
        if stripped != '':
            new_list.append(stripped)
    return new_list


def block_to_block_type(block): 
    if re.match(r'^#{1,6} .+', block):
        return BlockType.HEADING
    elif re.match(r'^```\n.*\n```$', block):
        return BlockType.CODE
    elif re.fullmatch(r'(?m)(>.*\n?)+', block):
        return BlockType.QUOTE
    elif re.fullmatch(r'(?m)(- .*\n?)+', block):
        return BlockType.ULIST
    elif block.startswith("1. "):
        lines = block.split("\n")
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    else:
        return BlockType.PARAGRAPH