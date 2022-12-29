import unittest
import main

class TestMain(unittest.TestCase):
    def test_flat_lists(self):
        result = main.flat_lists([1, [2, [3, [4, 5]]]])
        self.assertEqual([1, 2, 3, 4, 5], result)
    
    def test_flat_lists_with_strings(self):
        result = main.flat_lists(['a', ['b', 'c'], [1, [2, 3]], [[4, [5]], 6, [[7, 8], [9, 10]]]])
        self.assertEqual(['a', 'b', 'c', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], result)
    
    def test_flat_lists_with_none(self):
        result = main.flat_lists(0)
        self.assertEqual(None, result)
    
    def test_flat_lists_with_exception(self):
        with self.assertLogs(level='ERROR'):
            main.flat_lists(0)