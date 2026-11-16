
def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    filtered_list : list[str] = []
    for i in range (len(blocks)):
        block = blocks[i]
        stripped_block = block.strip()
        if block == "":
            blocks.pop(i)
            continue
        filtered_list.append(stripped_block)
    return filtered_list
