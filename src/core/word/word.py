from random import randint
from typing import List


class Word:
    def __init__(self, left_part: str = None, right_part: str = None, sentence: str = None):
        if left_part is None:
            left_part = ''
        if right_part is None:
            right_part = ''
        if sentence is None:
            sentence = ''

        self.left_part: str = left_part
        self.right_part: str = right_part
        self.sentence: str = sentence
        self.counter: int = 0
        self.output_sentence: str = f'\n{self.sentence}' if self.sentence != '' else ''
        self.full_word: str = f'{self.left_part} - {self.right_part}{self.output_sentence}\n'
        self.left_spoiler_part_word: str = f'||{self.left_part}|| \- {self.right_part}{self.output_sentence}'
        self.right_spoiler_part_word: str = f'{self.left_part} \- ||{self.right_part}||{self.output_sentence}'

    def to_json(self) -> dict:
        return {
            'left_part': self.left_part,
            'right_part': self.right_part,
            'sentence': self.sentence,
            'counter': self.counter,
        }

    def get_full_word(self):
        return self.full_word

    def update_counter(self):
        self.counter += 1

    def get_full_numerated_word(self, number: int):
        return str(number) + '. ' + self.full_word + '\n'

    def get_random_spoiler_word(self):
        if randint(0, 1) == 1:
            return self.get_left_spoiler_part_word()
        else:
            return self.get_right_spoiler_part_word()

    def get_left_spoiler_part_word(self):
        return self.left_spoiler_part_word

    def get_right_spoiler_part_word(self):
        return self.right_spoiler_part_word

    def __eq__(self, other: 'Word'):
        return (
                self.left_part == other.left_part and
                self.right_part == other.right_part and
                self.sentence == other.sentence and
                self.full_word == other.full_word and
                self.output_sentence == other.output_sentence and
                self.left_spoiler_part_word == other.left_spoiler_part_word and
                self.right_spoiler_part_word == other.right_spoiler_part_word
        )


Words = List[Word]
