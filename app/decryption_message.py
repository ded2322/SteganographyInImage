from stegano import lsb, exifHeader
from utils import file_path


def decryption_png():
    try:
        print("Зашифрованное сообщение: " + lsb.reveal(file_path()), "\n")
    except (FileNotFoundError, Exception) as e:
        if isinstance(e, FileNotFoundError):
            print("Файл не найден.")
        elif isinstance(e, Exception):
            print(f"Произошла ошибка: {str(e)}")


def decryption_jpg():
    try:
        print("Зашифрованное сообщение: " + exifHeader.reveal(file_path()).decode(), "\n")
    except (FileNotFoundError, Exception) as e:
        if isinstance(e, FileNotFoundError):
            print("Файл не найден.")
        elif isinstance(e, Exception):
            print(f"Произошла ошибка: {str(e)}")
