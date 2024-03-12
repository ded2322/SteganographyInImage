from app.tools import check_extension, user_message, user_path


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

        file_extension = check_extension(image_path=user_path(), encryption=True)
        file_extension["replica"].encryption(file_extension["image_path"], message=user_message())

    def decrypt(self):
        """
        Метод decrypt() выполняет дешифрование сообщения из изображения.
        Он использует FilePath для проверки расширения файла и получения пути к изображению.
        """
        file_extension = check_extension(image_path=user_path(),encryption=False)

        file_extension["replica"].decryption(file_extension["image_path"])