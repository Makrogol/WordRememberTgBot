from src.core.file_manager.user_data_manager import UserDataManager
from src.core.user.user_identifier_data import UserIdentifierData


def statistics_command(func):
    def wrapper(*args, **kwargs):
        # В команды бота всегда первым аргументом должен приходить Update, вторым - Context
        # Название команды и функции, которая исполняет эту команду должны быть одинаковыми
        user_identifier_data = UserIdentifierData(args[0].effective_user.id, args[0].effective_user.name)
        user_data_manger = UserDataManager(user_identifier_data)
        user_data = user_data_manger.get_or_create_user_data()
        user_data.statistics.command_statistics[func.__name__] += 1
        user_data_manger.save_to_file(user_data)
        return func(*args, **kwargs)

    return wrapper
