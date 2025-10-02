from .word import Word
from itertools import repeat

REPLACE_CHARS = '.'


# Парсим так:
# Все, что до первого дефиса, разделенного пробелами - левая часть слова
# Все, что от первого дефиса с пробелами до второго дефиса с пробелами - правая часть слова
# Все, что после второго дефиса с пробелами - предложение
# Все точки заменяются на пробелы, потому что точка это спец символ в тг сообщениях

def clear_part_of_word(part_of_word: str) -> str:
    # Первый этап - трим
    part_of_word = part_of_word.strip()

    # Второй этап - экранируем точки
    return part_of_word.replace(REPLACE_CHARS, '\.')


def try_parse_word(args: list[str]) -> Word | None:
    try:
        index_first_separate = args.index('-')
        index_second_separate = args.index('-', index_first_separate + 1) \
            if '-' in args[index_first_separate + 1:] \
            else len(args)

        left_part = ' '.join(args[:index_first_separate])
        left_part = clear_part_of_word(left_part)

        right_part = ' '.join(args[index_first_separate + 1:index_second_separate])
        right_part = clear_part_of_word(right_part)

        sentence = ' '.join(args[index_second_separate + 1:])
        sentence = clear_part_of_word(sentence)
        return Word(left_part, right_part, sentence)
    except:
        return None

# TODO унести в какой-то другой парсер
def try_parse_number(args: list[str]) -> int | None:
    try:
        number = int(args[0])
        return number
    except:
        return None


def try_parse_number_and_word(args: list[str]) -> (int | None, Word | None):
    number = try_parse_number(args)
    word = try_parse_word(args[1:])
    return number, word
