from unittest import TestCase
import api.utils.input as input_utils


class TestIsValidInput(TestCase):
    def test_is_valid_input_empty_string(self):
        self.assertFalse(input_utils.is_valid_input(""))

    def test_is_valid_input_number(self):
        self.assertFalse(input_utils.is_valid_input(9))

    def test_is_valid_input_None(self):
        self.assertFalse(input_utils.is_valid_input(None))

    def test_is_valid_input_string(self):
        self.assertTrue(input_utils.is_valid_input("Foo"))


class TestCompareInput(TestCase):
    def test_compare_input_space(self):
        self.assertFalse(input_utils.compare_input(" "))

    def test_compare_input_None(self):
        self.assertFalse(input_utils.compare_input(None))

    def test_compare_input_string(self):
        self.assertFalse(input_utils.compare_input("Foo"))

    def test_compare_input_with_null(self):
        self.assertTrue(input_utils.compare_input("Foo" + chr(0)))

    def test_compare_input_with_newline(self):
        self.assertTrue(input_utils.compare_input("\n"))


class TestKeyExists(TestCase):
    def test_key_exists_second_argument_missing(self):
        self.assertFalse(input_utils.key_exists("foo"))

    def test_key_exists_valid(self):
        self.assertTrue(input_utils.key_exists("foo", {"foo": "bar"}))

    def test_key_exists_invalid(self):
        self.assertFalse(input_utils.key_exists("foo", {"bar": "foo"}))
