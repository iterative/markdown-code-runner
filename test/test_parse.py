
import unittest
import mdcoderun
from mdcoderun import CodeBlock
from mdcoderun import parse

class ParseTestCase(unittest.TestCase):

    def test_search_inline_code(self):
        tests = [("`print`",
                  [CodeBlock(code="print",
                            start_pos=0,
                            end_pos=6,
                            delim="`",
                            language="",
                            katacoda_tag="")]
                  )]

        for i, (md_text, code_block_list) in enumerate(tests):
            self.assertEqual(parse.search_inline_code(md_text, ""),
                             code_block_list,
                             f"Test {i} fails:\n{md_text}\n{code_block_list}")

    def test_parse_code_without_katacoda(self):
        tests = [("`print`",
                  [CodeBlock(code="print",
                            start_pos=0,
                            end_pos=6,
                            delim="`",
                            language="",
                            katacoda_tag="")]
                  )]

        for i, (md_text, code_block_list) in enumerate(tests):
            self.assertEqual(parse.parse_text(md_text),
                             code_block_list,
                             f"Test {i} fails:\n{md_text}\n{code_block_list}")
def suite():
    suite = unittest.TestSuite()
    suite.addTest(ParseTestCase('test_search_inline_code'))
    suite.addTest(ParseTestCase('test_parse_code_without_katacoda'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
