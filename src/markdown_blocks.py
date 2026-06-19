def markdown_to_blocks(markdown):
    new_list = []
    mark = markdown.split('\n\n')
    for i in mark:
        stripped = i.strip()
        if stripped != '':
            new_list.append(stripped)
    return new_list

