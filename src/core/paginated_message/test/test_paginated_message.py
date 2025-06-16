import unittest
from src.core.paginated_message.config import MAX_MESSAGE_LENGTH_TEST
from src.core.paginated_message.paginated_message import PaginatedMessages


class PaginatedMessageTestCase(unittest.TestCase):
    def test_paginated_message_message_len_is_max_message_len(self):
        expected_result = ["1234567890", "1234567890"]
        paginated_message = PaginatedMessages(MAX_MESSAGE_LENGTH_TEST)
        paginated_message.add(["1234567890", "1234567890"])

        self.assertEqual(expected_result, paginated_message.get())

    def test_paginated_message_first_message_len_is_more_than_max_message_len(self):
        expected_result = ["1234567890", "1", "1234567890"]
        paginated_message = PaginatedMessages(MAX_MESSAGE_LENGTH_TEST)
        paginated_message.add(["12345678901", "1234567890"])

        self.assertEqual(expected_result, paginated_message.get())

    def test_paginated_message_last_message_len_is_more_than_max_message_len(self):
        expected_result = ["1234567890", "1234567890", "1"]
        paginated_message = PaginatedMessages(MAX_MESSAGE_LENGTH_TEST)
        paginated_message.add(["1234567890", "12345678901"])

        self.assertEqual(expected_result, paginated_message.get())

    def test_paginated_message_message_len_is_less_than_max_message_len(self):
        expected_result = ["123451234"]
        paginated_message = PaginatedMessages(MAX_MESSAGE_LENGTH_TEST)
        paginated_message.add(["12345", "1234"])

        self.assertEqual(expected_result, paginated_message.get())

    def test_paginated_message_many_messages_len_is_less_than_max_message_len(self):
        expected_result = ["12345123", "123"]
        paginated_message = PaginatedMessages(MAX_MESSAGE_LENGTH_TEST)
        paginated_message.add(["12345", "123", "123"])

        self.assertEqual(expected_result, paginated_message.get())

    def test_paginated_message_append(self):
        expected_result = ["12345123", "123"]
        paginated_message = PaginatedMessages(MAX_MESSAGE_LENGTH_TEST)
        for message in ["12345", "123", "123"]:
            paginated_message.append(message)

        self.assertEqual(expected_result, paginated_message.get())


if __name__ == '__main__':
    unittest.main()
