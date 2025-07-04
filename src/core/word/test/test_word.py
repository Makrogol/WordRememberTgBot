import unittest

from src.core.word.word import Word


class WordTestCase(unittest.TestCase):
    def test_get_full_word_empty_sentence(self):
        expected_result = "qwe - rty\n"
        result = Word(left_part="qwe", right_part="rty", sentence="").get_full_word()

        self.assertEqual(expected_result, result)

    def test_get_full_word(self):
        expected_result = "qwe - rty\n123\n"
        result = Word(left_part="qwe", right_part="rty", sentence="123").get_full_word()

        self.assertEqual(expected_result, result)

    def test_get_full_word_empty_left_part(self):
        expected_result = " - rty\n123\n"
        result = Word(left_part="", right_part="rty", sentence="123").get_full_word()

        self.assertEqual(expected_result, result)

    def test_get_full_word_empty_right_part(self):
        expected_result = "qwe - \n123\n"
        result = Word(left_part="qwe", right_part="", sentence="123").get_full_word()

        self.assertEqual(expected_result, result)

    def test_get_full_word_empty(self):
        expected_result = " - \n"
        result = Word(left_part="", right_part="", sentence="").get_full_word()

        self.assertEqual(expected_result, result)

    def test_get_full_word_empty_both_part(self):
        expected_result = " - \n123\n"
        result = Word(left_part="", right_part="", sentence="123").get_full_word()

        self.assertEqual(expected_result, result)

    def test_get_random_spoiler_word(self):
        expected_result = ["||qwe|| \- rty\n123", "qwe \- ||rty||\n123"]
        result = Word(left_part="qwe", right_part="rty", sentence="123").get_random_spoiler_word()

        self.assertTrue(result in expected_result)

    def test_get_random_spoiler_word_empty_sentence(self):
        expected_result = ["||qwe|| \- rty", "qwe \- ||rty||"]
        result = Word(left_part="qwe", right_part="rty", sentence="").get_random_spoiler_word()

        self.assertTrue(result in expected_result)

    def test_get_random_spoiler_word_empty_left_part(self):
        expected_result = ["|||| \- rty", " \- ||rty||"]
        result = Word(left_part="", right_part="rty", sentence="").get_random_spoiler_word()

        self.assertTrue(result in expected_result)

    def test_get_random_spoiler_word_empty_right_part(self):
        expected_result = ["||qwe|| \- ", "qwe \- ||||"]
        result = Word(left_part="qwe", right_part="", sentence="").get_random_spoiler_word()

        self.assertTrue(result in expected_result)

    def test_get_random_spoiler_word_empty(self):
        expected_result = ["|||| \- ", " \- ||||"]
        result = Word(left_part="", right_part="", sentence="").get_random_spoiler_word()

        self.assertTrue(result in expected_result)

    def test_get_random_spoiler_word_empty_both_part(self):
        expected_result = ["|||| \- \n123", " \- ||||\n123"]
        result = Word(left_part="", right_part="", sentence="123").get_random_spoiler_word()

        self.assertTrue(result in expected_result)

    def test_left_spoiler_part_word(self):
        expected_result = "||123|| \- 456"
        result = Word(left_part="123", right_part="456", sentence="").get_left_spoiler_part_word()

        self.assertTrue(result in expected_result)

    def test_right_spoiler_part_word(self):
        expected_result = "123 \- ||456||"
        result = Word(left_part="123", right_part="456", sentence="").get_right_spoiler_part_word()

        self.assertTrue(result in expected_result)

    def test_get_full_numerated_word(self):
        expected_result = "1\. 123 \- ||456||\n"
        result = Word(left_part="123", right_part="456", sentence="").get_right_spoiler_part_word()

        self.assertTrue(result in expected_result)


if __name__ == '__main__':
    unittest.main()
