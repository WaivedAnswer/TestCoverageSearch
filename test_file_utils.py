import unittest
from TestCoverageSearch import file_utils


class TestFileUtils(unittest.TestCase):
    def test_is_test_file_test(self):
        test_name = "Test.py"
        self.assertTrue(file_utils.is_test_file(test_name))

    def test_is_test_file_test_lower(self):
        test_name = "test.py"
        self.assertTrue(file_utils.is_test_file(test_name))

    def test_is_test_file_proj_file(self):
        test_name = "test.vcxproj"
        self.assertFalse(file_utils.is_test_file(test_name))

    def test_is_test_file_class(self):
        test_name = "Class.py"
        self.assertFalse(file_utils.is_test_file(test_name))

    def test_is_test_file_class_test(self):
        test_name = "ClassTest.py"
        self.assertTrue(file_utils.is_test_file(test_name))

    def test_passes_search_filterTwoTerm(self):
        test_name = "ClassTest.py"
        self.assertTrue(file_utils.passes_search_filter(test_name, "Class Test"))

    def test_passes_search_filter_MissingTerm(self):
        test_name = "FooTest.py"
        self.assertFalse(file_utils.passes_search_filter(test_name, "Class Test"))

    def test_passes_search_filterBlank(self):
        test_name = "FooTest.py"
        self.assertFalse(file_utils.passes_search_filter(test_name, ""))

    def test_passes_search_filterSpace(self):
        test_name = "FooTest.py"
        self.assertFalse(file_utils.passes_search_filter(test_name, " "))


if __name__ == '__main__':
    unittest.main()
