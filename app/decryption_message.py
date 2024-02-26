from stegano import lsb


def decryption_png(path_secret_image: str):
    try:
        print("Зашифрованное сообщение: " + lsb.reveal(path_secret_image), "\n")
    except (FileNotFoundError, Exception) as e:
        if isinstance(e, FileNotFoundError):
            print("Файл не найден.")
        elif isinstance(e, Exception):
            print(f"Произошла ошибка: {str(e)}")
        