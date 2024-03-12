import os

from app.encrypt_fabric import PNGEncryptionFabric, JPGEncryptionFabric
from app.decryption_fabric import PNGDecryptionFabric, JPGDecryptionFabric


def check_extension(image_path, encryption=True):
    """
        Проверяет расширение файла и возвращает словарь с путем и экземпляром класса
        вместе с путем к файлу.

        :param image_path: Путь до изображения
        :param encryption: Флаг, указывающий на тип операции (шифрование или дешифрование).
        :return: Словарь с путем к изображению и экземпляром класса.
        """

    if os.path.exists(image_path):
        if image_path.endswith(".png"):
            return {
                "image_path": image_path,
                "replica": PNGEncryptionFabric() if encryption else PNGDecryptionFabric()
            }
        if image_path.endswith(".jpg"):
            return {
                "image_path": image_path,
                "replica": JPGEncryptionFabric() if encryption else JPGDecryptionFabric()
            }
    else:
        print("Неверный путь до изображения.\n")


def user_message() -> str:
    massage_user = input("Введите сообщение которое хотите зашифровать: ")
    return check_cyrillic(massage_user)


def user_path() -> str:
    image_path = input("Введите путь до изображения: ")
    return image_path


def check_cyrillic(text: str) -> str:
    """
   Проверяет наличие кириллицы в тексте и предлагает пользователю продолжить или ввести новый текст.

   :param text: Текст для проверки наличия кириллицы.
   :return: Исходный текст, если кириллица отсутствует, или новый текст, введенный пользователем.
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


def menu_help():
    """
    Меню помощи, читает файл menu_help.txt и выводит текст из него
    """
    with open("menu_help.txt", "r", encoding="utf-8") as file:
        help_text = file.read()
    print(help_text)

    while True:
        user = input('Выйти в главное меню Д/Н: ')
        if user == 'Д' or 'д':
            break
