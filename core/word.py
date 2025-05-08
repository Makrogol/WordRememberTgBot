from random import randint


class Word:
    def __init__(self, left_part: str, right_part: str):
        self.__left_part = left_part
        self.__right_part = right_part

    def get_full_word(self):
        return f'{self.__left_part} - {self.__right_part}'

    def get_random_spoiler_word(self):
        if randint(0, 1) == 1:
            return f'||{self.__left_part}|| \- {self.__right_part}'
        else:
            return f'{self.__left_part} \- ||{self.__right_part}||'


def try_create_from_args(args: list[str]) -> Word | None:
    if not check_args_to_word_creating(args):
        return None
    try:
        index_separate = args.index('-')
        left_part = ' '.join(args[:index_separate])
        right_part = ' '.join(args[index_separate + 1:])
        return Word(left_part, right_part)
    except:
        return None


def check_args_to_word_creating(args: list[str]) -> bool:
    def __check_not_empty_part_of_word(index_range: range) -> bool:
        has_not_empty_part_of_word = False
        for index in index_range:
            if args[index] != '':
                has_not_empty_part_of_word = True
                break
        if not has_not_empty_part_of_word:
            return False
        return True

    try:
        index_separate = args.index('-')
        # That mean no left or no right part of word
        if index_separate == 0 or index_separate == len(args) - 1:
            return False

        if (not __check_not_empty_part_of_word(range(0, index_separate)) or
                not __check_not_empty_part_of_word(range(index_separate, len(args)))):
            return False
    except ValueError:
        return False
    return True
