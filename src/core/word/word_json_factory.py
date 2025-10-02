from src.core.word.word import Word


class WordJsonFactory:
    @staticmethod
    def create(data: dict) -> Word:
        word = Word()
        word.left_part = data['left_part']
        word.right_part = data['right_part']
        word.sentence = data['sentence']
        word.counter = data['counter']
        # TODO refactor
        word.output_sentence = f'\n{word.sentence}' if word.sentence != '' else ''
        word.full_word = f'{word.left_part} - {word.right_part}{word.output_sentence}\n'
        word.left_spoiler_part_word = f'||{word.left_part}|| \- {word.right_part}{word.output_sentence}'
        word.right_spoiler_part_word = f'{word.left_part} \- ||{word.right_part}||{word.output_sentence}'
        return word
