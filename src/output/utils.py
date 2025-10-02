from src.output.message.text_message import TextMessages, TextMessage
from src.core.word.word import Words


def get_statistics_by_words(words: Words) -> list[str]:
    return [f' - {word.get_full_word()[:-1]} - {word.counter}\n' for word in words]


def create_output_words(words: Words) -> list[str]:
    output_words: list[str] = []
    for i, word in enumerate(words):
        output_words.append(word.get_full_numerated_word(i) + '\n')
    return output_words


def convert_raw_messages_to_text_messages(raw_messages: str | list[str]) -> TextMessages:
    if isinstance(raw_messages, str):
        raw_messages = [raw_messages]
    messages = TextMessages()
    for raw_message in raw_messages:
        messages.append(TextMessage(text=raw_message))
    return messages
