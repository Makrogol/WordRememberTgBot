import unittest

from core.word.word import Word
from core.word.word_parser import try_parse_word


class WordParserTestCase(unittest.TestCase):
    def test_word_parser(self):
        expected_result = Word(left_part="gh", right_part="hj", sentence="")
        result = try_parse_word(["gh", "-", "hj"])

        self.assertEqual(expected_result, result)

    def test_word_parser_some_left_part_word(self):
        expected_result = Word(left_part="gh, fds,fjd ut;", right_part="hj", sentence="")
        result = try_parse_word(["gh,", "fds,fjd", "ut;", "-", "hj"])

        self.assertEqual(expected_result, result)

    def test_word_parser_some_right_part_word(self):
        expected_result = Word(left_part="hj", right_part="gh, fds,fjd ut;", sentence="")
        result = try_parse_word(["hj", "-", "gh,", "fds,fjd", "ut;"])

        self.assertEqual(expected_result, result)

    def test_word_parser_sentence(self):
        expected_result = Word(left_part="hj", right_part="gh", sentence="qwerty")
        result = try_parse_word(["hj", "-", "gh", "-", "qwerty"])

        self.assertEqual(expected_result, result)

    def test_word_parser_some_sentence(self):
        expected_result = Word(left_part="hj", right_part="gh", sentence="qwerty? fhasdjk* 78419 asda%")
        result = try_parse_word(["hj", "-", "gh", "-", "qwerty?", "fhasdjk*", "78419", "asda%"])

        self.assertEqual(expected_result, result)

    def test_word_parser_replace_point_to_space(self):
        expected_result = Word(left_part="hj ", right_part="gh", sentence="qwe rty? fhasdjk* 78419 asda%")
        result = try_parse_word(["hj.", "-", "gh", "-", "qwe.rty?", "fhasdjk*", "78419", "asda%"])

        self.assertEqual(expected_result, result)

    def test_word_parser_separator_with_left_part_and_sentence(self):
        expected_result = Word(left_part="hj- gh", right_part="qwerty", sentence="")
        result = try_parse_word(["hj-", "gh", "-", "qwerty"])

        self.assertEqual(expected_result, result)

    def test_word_parser_separator_with_right_part_and_sentence(self):
        expected_result = Word(left_part="hj -gh", right_part="qwerty", sentence="")
        result = try_parse_word(["hj", "-gh", "-", "qwerty"])

        self.assertEqual(expected_result, result)

    def test_word_parser_separator_with_right_part(self):
        result = try_parse_word(["hj", "-gh"])

        self.assertIsNone(result)

    def test_word_parser_separator_with_left_part(self):
        result = try_parse_word(["hj-", "gh"])

        self.assertIsNone(result)

    def test_word_parser_separator_with_both_part(self):
        result = try_parse_word(["hj-fs", "gh"])

        self.assertIsNone(result)

    def test_word_parser_separator_with_both_part_and_sentence(self):
        expected_result = Word(left_part="hj-gfs gh", right_part="qwerty", sentence="")
        result = try_parse_word(["hj-gfs", "gh", "-", "qwerty"])

        self.assertEqual(expected_result, result)

    def test_word_parser_sentence_separator_with_sentence(self):
        expected_result = Word(left_part="gf", right_part="gh -qwerty", sentence="")
        result = try_parse_word(["gf", "-", "gh", "-qwerty"])

        self.assertEqual(expected_result, result)

    def test_word_parser_sentence_separator_with_right_part(self):
        expected_result = Word(left_part="gf", right_part="gh- qwerty", sentence="")
        result = try_parse_word(["gf", "-", "gh-", "qwerty"])

        self.assertEqual(expected_result, result)

    def test_word_parser_empty_left_part(self):
        expected_result = Word(left_part="", right_part="gh", sentence="")
        result = try_parse_word(["-", "gh"])

        self.assertEqual(expected_result, result)

    def test_word_parser_empty_right_part(self):
        expected_result = Word(left_part="gh", right_part="", sentence="")
        result = try_parse_word(["gh", "-"])

        self.assertEqual(expected_result, result)

    def test_word_parser_empty_left_part_with_sentence(self):
        expected_result = Word(left_part="", right_part="gh", sentence="qwerty")
        result = try_parse_word(["-", "gh", "-", "qwerty"])

        self.assertEqual(expected_result, result)

    def test_word_parser_empty_right_part_with_sentence(self):
        expected_result = Word(left_part="gh", right_part="", sentence="qwerty")
        result = try_parse_word(["gh", "-", "-", "qwerty"])

        self.assertEqual(expected_result, result)

    def test_word_parser_empty(self):
        expected_result = Word(left_part="", right_part="", sentence="")
        result = try_parse_word(["-"])

        self.assertEqual(expected_result, result)

    def test_word_parser_empty_args(self):
        result = try_parse_word([])

        self.assertIsNone(result)

    def test_word_parser_empty_with_sentence(self):
        expected_result = Word(left_part="", right_part="", sentence="qwerty")
        result = try_parse_word(["-", "-", "qwerty"])

        self.assertEqual(expected_result, result)

    def test_word_parser_empty_with_empty_sentence(self):
        expected_result = Word(left_part="", right_part="", sentence="")
        result = try_parse_word(["-", "-"])

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
