from random import randint


class Word:
    def __init__(self, left_part: str, right_part: str, sentence: str):
        self.__left_part = left_part
        self.__right_part = right_part
        self.__sentence = sentence
        self.__output_sentence = f"\n{self.__sentence}" if self.__sentence != "" else ""
        self.__full_word = f"{self.__left_part} - {self.__right_part}{self.__output_sentence}"
        self.__left_spoiler_part_word = f"||{self.__left_part}|| \- {self.__right_part}{self.__output_sentence}"
        self.__right_spoiler_part_word = f"{self.__left_part} \- ||{self.__right_part}||{self.__output_sentence}"

    def get_full_word(self):
        return self.__full_word

    def get_random_spoiler_word(self):
        if randint(0, 1) == 1:
            return self.__left_spoiler_part_word
        else:
            return self.__right_spoiler_part_word

    def __eq__(self, other):
        return (
                self.__left_part == other.__left_part and
                self.__right_part == other.__right_part and
                self.__sentence == other.__sentence and
                self.__full_word == other.__full_word and
                self.__output_sentence == other.__output_sentence and
                self.__left_spoiler_part_word == other.__left_spoiler_part_word and
                self.__right_spoiler_part_word == other.__right_spoiler_part_word)
