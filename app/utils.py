import os


def check_extension(name_secret_image:str,extension:str)->str:
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
