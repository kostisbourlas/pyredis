import unittest

from app.resp import RespHandler, InvalidFormatError


class RespTestCase(unittest.TestCase):
    def test_determine_first_byte_is_a_simple_string(self):
        input: bytes = b"+OK\r\n"
        first_byte: str = RespHandler.determine_first_byte(input)
        self.assertEqual(first_byte, "SIMPLE_STRING")

    def test_determine_first_byte_is_an_error(self):
        input: bytes = b"-Error message\r\n"
        first_byte: str = RespHandler.determine_first_byte(input)
        self.assertEqual(first_byte, "ERROR")

    def test_determine_first_byte_is_an_integer(self):
        input: bytes = b":42\r\n"
        first_byte: str = RespHandler.determine_first_byte(input)
        self.assertEqual(first_byte, "INTEGER")

    def test_determine_first_byte_is_a_bulk_string(self):
        input: bytes = b"$0\r\n\r\n"
        first_byte: str = RespHandler.determine_first_byte(input)
        self.assertEqual(first_byte, "BULK_STRING")

    def test_determine_first_byte_is_an_array(self):
        input: bytes = b"*2\r\n$4\r\necho\r\n$11\r\nhello world\r\n"
        first_byte: str = RespHandler.determine_first_byte(input)
        self.assertEqual(first_byte, "ARRAY")

    def test_determine_invalid_prefix_should_raise_error(self):
        input: bytes = b"&2\r\n$4\r\necho\r\n$11\r\nhello world\r\n"
        with self.assertRaises(InvalidFormatError) as error:
            RespHandler.determine_first_byte(input)

        self.assertEqual(
            str(error.exception), "Byte array should start by +, -, :, $ or *."
        )
