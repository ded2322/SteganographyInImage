import os


def file_path() -> str | None:
    image_path = input("Введите путь до изображения: ")
    if not check_image(image_path):
        print("Неверный путь до изображения.\n")
        return None
    return image_path


def user_message(png: bool = False) -> str | None:
    massage_user = input("Введите сообщение которое хотите зашифровать: ")
    if png:
        massage_user = check_cyrillic(massage_user)
    return massage_user


def check_extension(extension: str) -> str:
    name_secret_image = input("Введите какое название вы хотите у зашифрованного изображения: ")

    if not name_secret_image.endswith(extension):
        return name_secret_image + extension
    return name_secret_image


def check_image(image_path: str) -> bool:
    """

    """
    if os.path.exists(image_path):
        if '.' in os.path.basename(image_path):
            return True
        else:
            return False
    else:
        return False


def check_cyrillic(text: str) -> str:
    """

    """

    while True:
        if not any(ord('а') <= ord(char.lower()) <= ord('я') for char in text):
            return text
        print("В вашем сообщении находится кириллица.\n"
              "При дешифровке, возможен некорректный вывод.\n")
        loop_input = input("Продолжить Д/Н")
        if loop_input == "Д" or "д":
            return text
        text = input("Введите новый текст")
        return text
