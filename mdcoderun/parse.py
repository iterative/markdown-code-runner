import re
from . import CodeBlock


CODE_BLOCK_REGEX = r"""^(```)([\S]+)?
([\s\S]+?)
(```)"""
"Regex to capture code blocks in the document"

INLINE_CODE_REGEX = r"(`)([^`]+)(`)"
"Regex to capture `inline code` within paragraphs"

def search_code_block(md_text, katacoda_tag):
    """Searches md_text with CODE_BLOCK_REGEX + katacoda_tag"""
    if katacoda_tag == "":
        search_regex = CODE_BLOCK_REGEX
    else:
        search_regex = CODE_BLOCK_REGEX + r"\{\{" + katacoda_tag + r"\}\}"
    current_pos = 0
    match = True
    code_blocks = []
    while match:
        match = re.search(search_regex, md_text[current_pos:], re.MULTILINE)
        if match:
            cb = CodeBlock(code = match.group(3),
                           start_pos = current_pos + match.start(0),
                           end_pos = current_pos + match.end(0),
                           delim = match.group(1),
                           language = match.group(2),
                           katacoda_tag = katacoda_tag)
            current_pos += match.end(0)
            code_blocks.append(cb)
    return code_blocks


def search_inline_code(md_text, katacoda_tag):
    """Searches md_text with INLINE_CODE_REGEX + katacoda_tag"""
    if katacoda_tag == "":
        search_regex = INLINE_CODE_REGEX
    else:
        search_regex = INLINE_CODE_REGEX + r"\{\{" + katacoda_tag + r"\}\}"
    current_pos = 0
    match = True
    code_blocks = []
    while match:
        match = re.search(search_regex, md_text[current_pos:])
        if match:
            cb = CodeBlock(code = match.group(2),
                           start_pos = current_pos + match.start(0),
                           end_pos = current_pos + match.end(0),
                           delim = match.group(1),
                           language = "",
                           katacoda_tag = katacoda_tag)
            current_pos += match.end(0)
            code_blocks.append(cb)
    return code_blocks

def parse_text(md_text, parse_blocks=True, parse_inline=True, katacoda_tags=[], language="") :
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

    if len(language) > 0:
        code_blocks = [cb for cb in code_blocks if cb.language == language]

    code_blocks = sorted(code_blocks, key=lambda cb: cb.start_pos)

    return code_blocks



def parse_file(filename, parse_inline=True, parse_blocks=True, katacoda_tags=[], language=""):
    """Reads the file and returns the code blocks"""

    with open(filename) as f:
        code_blocks = parse_text(f.read(), parse_inline=parse_inline, parse_blocks=parse_blocks, katacoda_tags=katacoda_tags, language=language)

    return code_blocks


