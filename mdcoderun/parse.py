import re


CODE_BLOCK_REGEX = r"^(```)([\S]+)?\n([\s\S]+?)\n(```)"
INLINE_CODE_REGEX = r"(`)(.+?)(`)"

def search_code_block(md_text, katacoda_tag):
    """Searches md_text with CODE_BLOCK_REGEX + katacoda_tag"""
    search_regex = CODE_BLOCK_REGEX + katacoda_tag
    current_pos = 0
    match = True
    code_blocks = []
    while match:
        match = re.search(md_text[current_pos:], search_regex, re.MULTILINE | re.UNICODE)
        if match:
            cb = CodeBlock(code = match.group(3),
                           start_pos = match.start(0),
                           end_pos = match.end(0),
                           delim = match.group(1),
                           language = match.group(2),
                           katacoda_tag = katacoda_tag)
            current_pos += match.start(0)
            code_blocks.append(cb)
    return code_blocks


def search_inline_code(md_text, katacoda_tag):
    """Searches md_text with INLINE_CODE_REGEX + katacoda_tag"""
    search_regex = INLINE_CODE_REGEX + katacoda_tag
    current_pos = 0
    match = True
    code_blocks = []
    while match:
        match = re.search(md_text[current_pos:], search_regex, re.MULTILINE | re.UNICODE)
        if match:
            cb = CodeBlock(code = match.group(2),
                           start_pos = match.start(0),
                           end_pos = match.end(0),
                           delim = match.group(1),
                           language = "",
                           katacoda_tag = katacoda_tag)
            current_pos += match.start(0)
            code_blocks.append(cb)
    return code_blocks

def parse_text(md_text, parse_blocks=True, parse_inline=True, katacoda_tags=[]) :
    """Parses the given text and returns the code blocks delimited by
    ```
    code
    ```

    or

    `code`

    The code block may have katacoda tags like:

    ```
    code
    ```{{execute}}

    or 

    `file`{{open}}

    These should be listed in the argument as:

    `katacoda_tags=['{{execute}}']`

    The result is list of CodeBlock objects.

    """

    code_blocks = []

    if parse_blocks:
        if len(katacoda_tags) == 0:
            code_blocks += search_code_block(md_text, "")
        else:
            for kt in katacoda_tags:
                code_blocks += search_code_block(md_text, kt)

    if parse_inline:
        if len(katacoda_tags) == 0:
            code_blocks += search_inline_code(md_text, "")
        else:
            for kt in katacoda_tags:
                code_blocks += search_inline_code(md_text, kt)

    code_blocks = sorted(code_blocks, key=lambda cb: cb.start_pos)

    return code_blocks



def parse_file(filename, katacoda_tags=[]):
    """Reads the file and returns the code blocks"""
    pass


