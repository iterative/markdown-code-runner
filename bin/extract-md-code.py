#!/usr/bin/env python3

import argparse
import sys
from pprint import pprint

from mdcoderun import parse

def main():

    argparser = argparse.ArgumentParser(
        description="Extracts code blocks and inline code from .md files, optionally tagged with {{katacoda}} style elements"
    )

    argparser.add_argument("files", nargs="+", metavar="nfiles", help="markdown files to be processed")
    argparser.add_argument("--katacoda-tag", "-k", default="", help="The Katacoda tag that will be searched in .md code blocks, e.g., for {{execute}}, specify 'execute'")
    argparser.add_argument("--no-inline", action="store_true", default = False, help="Skip `inline code elements` while parsing")
    argparser.add_argument("--no-block", action="store_true", default = False, help="Skip ```\ncode\nblocks\n``` while parsing")
    argparser.add_argument("--language", "-l", default="", help="Filter the blocks by ```language\ncode\ncode\n```. Implies --no-inline, as inline code elements cannot specify language")
    argparser.add_argument("--debug", default=False, action="store_true", help="Show debug output")
    
    args = argparser.parse_args()

    katacoda_tag = args.katacoda_tag
    inline = not args.no_inline
    block = not args.no_block
    language = args.language
    debug = args.debug

    if debug:
        pprint(args)

    for md_filename in args.files:
        code_blocks = parse.parse_file(
            md_filename,
            parse_inline = inline,
            parse_blocks = block,
            katacoda_tags = [katacoda_tag],
            language = language
        )
        if debug:
            pprint(code_blocks)
        else:
            print("\n".join([cb.code for cb in code_blocks]))


if __name__ == "__main__":
    main()