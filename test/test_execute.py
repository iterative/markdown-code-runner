
import unittest
import mdcoderun
from mdcoderun import execute

class ExecuteTestCase(unittest.TestCase):
    def test_get_client(self):
        c = execute.get_client()
        self.assertIsNotNone(c, f"Client is None")

    def test_get_container(self):
        c = execute.get_container("alpine")
        self.assertIsNotNone(c, "Container is None")

    def test_run_in_container(self):
        res = execute.run_in_container("alpine", "echo 'hello world'")
        self.assertEqual(res, b"hello world")


def suite():
    suite = unittest.TestSuite()
    suite.addTest(ExecuteTestCase('test_get_client'))
    suite.addTest(ExecuteTestCase('test_get_container'))
    suite.addTest(ExecuteTestCase('test_run_in_container'))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())