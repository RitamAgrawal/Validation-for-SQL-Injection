from unittest import TestCase
from api.utils.error import error_message


class TestErrorMessage(TestCase):
    def test_error_message_bad_request(self):
        expected = "Bad Request. Please verify your Input", 400
        actual = error_message("BAD_REQUEST")
        self.assertEqual(actual, expected)

    def test_error_message_missing_payload(self):
        expected = "Invalid Input. Request is missing \"payload\".", 400
        actual = error_message("MISSING_PAYLOAD")
        self.assertEqual(actual, expected)

    def test_error_message_invalid_input(self):
        expected = "Invalid Input. Please verify your Input", 400
        actual = error_message("")
        self.assertEqual(actual, expected)
