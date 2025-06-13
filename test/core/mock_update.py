from test.config import DEFAULT_CHAT_ID, DEFAULT_USER_ID
from test.core.mock_effective_chat import MockEffectiveChat
from test.core.mock_effective_user import MockEffectiveUser


class MockUpdate:
    def __init__(self, chat_id: int = DEFAULT_CHAT_ID, user_id: int = DEFAULT_USER_ID):
        self.effective_chat = MockEffectiveChat(chat_id)
        self.effective_user = MockEffectiveUser(user_id)
