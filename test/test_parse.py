
import unittest
import mdcoderun
from mdcoderun import CodeBlock
from mdcoderun import parse

class ParseTestCase(unittest.TestCase):

    def test_search_inline_code(self):
        tests = [("`print`",
                  [CodeBlock(code="print",
                            start_pos=0,
                            end_pos=7,
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
                            end_pos=7,
                            delim="`",
                            language="",
                            katacoda_tag="")]
                  )]

        for i, (md_text, code_block_list) in enumerate(tests):
            self.assertEqual(parse.parse_text(md_text),
                             code_block_list,
                             f"Test {i} fails:\n{md_text}\n{code_block_list}")

    def test_parse_code_with_katacoda(self):
        tests = [("""
`print`{{execute}}

and also

```python
   print(x, y)
```{{execute}}
""", 
                  ["execute"],
                  [CodeBlock(code="print",
                             start_pos=1,
                             end_pos=19,
                             delim="`",
                             language="",
                             katacoda_tag="execute"),
                   CodeBlock(code="   print(x, y)",
                             start_pos=31,
                             end_pos=70,
                             delim="```",
                             language="python",
                             katacoda_tag="execute")])]


        for i, (md_text, katacoda_tags, code_block_list) in enumerate(tests):
            self.assertEqual(parse.parse_text(md_text, katacoda_tags=katacoda_tags),
                             code_block_list,
                             f"Test {i} fails:\n{md_text}\n{code_block_list}")

    def test_parse_file_with_katacoda(self):
        execute_blocks = {"01-running-experiments.md":
                        ["dvc exp --help",
                         r"""dvc exp run --set-param featurize.max_features=1500 \
            -S featurize.ngrams=2""",
                         "git diff params.yaml",
                         "dvc exp diff"],
                          "05-cleaning-up.md":
                          [r"""dvc exp show --no-timestamp \
             --include-params train.n_est \
             --no-pager""",
                           r"""dvc exp show -n 2 --no-timestamp \
                  --include-params train.n_est \
                  --no-pager""",
                        r"""dvc exp gc  --workspace 
dvc exp show -n 2 --no-timestamp \
                  --include-params train.n_est \ 
                  --no-pager"""]
                          }

        for test_filename in execute_blocks:
            test_filepath = f"test/test-files/{test_filename}"
            # print(f"Testing: {test_filepath}")
            out_cbs = [cb.code for cb in parse.parse_file(test_filepath, 
                                         katacoda_tags=["execute"])]
            self.assertEqual(out_cbs,
                             execute_blocks[test_filename],
                             f"Test for {test_filepath} fails:\nRequired:{execute_blocks[test_filename]}\nGot:\n{out_cbs}\n")



def suite():
    suite = unittest.TestSuite()
    suite.addTest(ParseTestCase('test_search_inline_code'))
    suite.addTest(ParseTestCase('test_parse_code_without_katacoda'))
    suite.addTest(ParseTestCase('test_parse_code_with_katacoda'))
    suite.addTest(ParseTestCase('test_parse_file_with_katacoda'))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
