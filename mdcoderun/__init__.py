
import re
from dataclasses import dataclass

@dataclass
class CodeBlock:
    "Contains the data of a code block extracted from a markdown file"
    code: str
    start_pos: int
    end_pos: int
    delim: str   # can be either ``` or `
    language: str = ""
    katacoda_tag: str = ""
