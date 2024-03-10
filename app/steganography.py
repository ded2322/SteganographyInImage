from app.mixins import FilePath
from app.mixins import user_input, check_cyrillic


class Steganography:
    """
    Класс Steganography предоставляет методы для шифрования и дешифрования сообщений в изображениях.
    """

    def encrypt(self):
        """
        Метод encrypt() выполняет шифрование сообщения в изображении.
        Он использует FilePath для проверки расширения файла и получения пути к изображению,
        а также функции user_input() и check_cyrillic() для получения и проверки вводимого пользователем сообщения.
        """
        file_extension = FilePath.check_extension(encryption=True)

        message = user_input()
        message = check_cyrillic(message)
        file_extension["replica"].encryption(file_extension["image_path"], message=message)

    def decrypt(self):
        """
        Метод decrypt() выполняет дешифрование сообщения из изображения.
        Он использует FilePath для проверки расширения файла и получения пути к изображению.
        """
        file_extension = FilePath.check_extension(encryption=False)

        file_extension["replica"].decryption(file_extension["image_path"])