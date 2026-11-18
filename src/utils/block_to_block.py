from enum import Enum

class BlockType(Enum):
    PARAGRAPH = 1
    HEADING = 2
    CODE = 3
    QUOTE = 4
    UNORDERED_LIST = 5
    ORDERED_LIST = 6


def block_to_block_type(block: str) -> BlockType:
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    for i in range(1, 7):
        prefix = "#" * i + " "
        if block.startswith(prefix):
            return BlockType.HEADING

    split_blocks = block.split("\n")
    is_quote_block = True
    for split_block in split_blocks:
        if not split_block.startswith(">"):
            is_quote_block = False
            break
    if is_quote_block:
        return BlockType.QUOTE
    
    is_unordered_list_block = True
    for split_block in split_blocks:
        if not split_block.startswith("- "):
            is_unordered_list_block = False
            break
    if is_unordered_list_block:
        return BlockType.UNORDERED_LIST

    is_ordered_list_block = True
    for i in range(len(split_blocks)):
        list_number = i + 1
        if not split_blocks[i].startswith(f"{list_number}. "):
            is_ordered_list_block = False
            break
    if is_ordered_list_block:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

