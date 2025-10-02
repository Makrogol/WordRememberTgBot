from pathlib import Path

from src.core.file_manager.config import TMP_PATH


class TmpFileManager:
    def __init__(self, tmp_path: Path | None = None):
        if tmp_path is None:
            tmp_path = TMP_PATH

        self.tmp_path = tmp_path
        self.tmp_path.mkdir(parents=True, exist_ok=True)

    def create_tmp_file(self, file_name: str, file_data: str | list[str]) -> Path | None:
        if isinstance(file_data, list):
            file_data = '\n'.join(file_data)

        try:
            file_path = self.tmp_path / file_name
            file_path.touch()

            file = open(str(file_path), 'w')
            file.write(file_data)
            file.close()
        except:
            # TODO обрабатывать возможные исключения тут (закончилась память, файл уже существует и тп)
            return None

        return file_path

    def clear_tmp_directory(self) -> None:
        for path in self.tmp_path.iterdir():
            if path.is_file():
                path.unlink()
            elif path.is_dir():
                path.rmdir()
            else:
                # TODO это невозможная ситуация и ее можно как-то отдельно обработать (каким-нибудь эксепшеном)
                print('error')


tmp_file_manager = TmpFileManager()
