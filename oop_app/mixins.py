import os
from abc import ABC, abstractmethod

from oop_app.encrypt_fabric import PNGEncryptionFabric, JPGEncryptionFabric
from oop_app.decryption_fabric import PNGDecryptionFabric, JPGDecryptionFabric


class FilePath:
    @staticmethod
    def check_extension(encryption=True):
        """
        Проверяет расширение файла и возвращает словарь с путем и экземпляром класса
        вместе с путем к файлу.

        :param encryption: Флаг, указывающий на тип операции (шифрование или дешифрование).
        :return: Словарь с путем к изображению и экземпляром класса.
        """
        image_path = input("Введите путь до изображения: ")

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

import os
from abc import ABC, abstractmethod

from oop_app.encrypt_fabric import PNGEncryptionFabric, JPGEncryptionFabric
from oop_app.decryption_fabric import PNGDecryptionFabric, JPGDecryptionFabric


class FilePathCrypt:
   @staticmethod
   def check_extension():
       """
       Проверяет расширение файла и возвращает словарь с путем и экземпляром класса
       вместе с путем к файлу.
       """
       image_path = input("Введите путь до изображения: ")

       if os.path.exists(image_path):
           if image_path.endswith(".png"):
               return {"image_path": image_path, "replica": PNGEncryptionFabric()}
           if image_path.endswith(".jpg"):
               return {"image_path": image_path, "replica": JPGEncryptionFabric()}
       else:
           print("Неверный путь до изображения.\n")


class FilePathDecrypt:
   @staticmethod
   def check_extension():
       """
       Проверяет расширение файла и возвращает словарь с путем и экземпляром класса
       вместе с путем к файлу.
       """
       image_path = input("Введите путь до изображения: ")

       if os.path.exists(image_path):
           if image_path.endswith(".png"):
               return {"image_path": image_path, "replica": PNGDecryptionFabric()}
           if image_path.endswith(".jpg"):
               return {"image_path": image_path, "replica": JPGDecryptionFabric()}
       else:
           print("Неверный путь до изображения.\n")


def user_input():
   massage_user = input("Введите сообщение которое хотите зашифровать: ")
   return massage_user


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

