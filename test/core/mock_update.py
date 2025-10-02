from test.config import TEST_CHAT_ID, TEST_USER_ID, TEST_USER_NAME
from test.core.mock_effective_chat import MockEffectiveChat
from test.core.mock_effective_user import MockEffectiveUser


class MockUpdate:
    def __init__(self, chat_id: int = TEST_CHAT_ID, user_id: int = TEST_USER_ID, user_name: str = TEST_USER_NAME):
        self.effective_chat = MockEffectiveChat(chat_id)
        self.effective_user = MockEffectiveUser(user_id, user_name)
