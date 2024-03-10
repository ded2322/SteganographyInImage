import os

from abc import ABC, abstractmethod
from stegano import lsb, exifHeader


class EncryptionFabric(ABC):
    """
    Абстрактный базовый класс для фабрики шифрования.
    """

    @abstractmethod
    def encryption(self, image_path, message):
        """
        Абстрактный метод для шифрования сообщения в изображении.

        :param image_path: Путь к файлу изображения.
        :param message: Сообщение для шифрования.
        """
        pass


class PNGEncryptionFabric(EncryptionFabric):
    """
    Класс фабрики шифрования для изображений в формате PNG.
    """

    def encryption(self, image_path, message):
        """
        Метод для шифрования сообщения в изображении в формате PNG.

        :param image_path: Путь к файлу изображения.
        :param message: Сообщение для шифрования.
        """
        try:
            # Прячем сообщения в изображении
            secret = lsb.hide(image_path, message)
            # Сохранения изображения в файлах
            secret.save(image_path)
            # Путь где лежит сохраненный файл
            filePath = os.getcwd()
            print(f'\nПуть до файла: {filePath}')
        except Exception as e:
            print(f'Произошла ошибка: {str(e)}')


class JPGEncryptionFabric(EncryptionFabric):
    """
    Класс фабрики шифрования для изображений в формате JPG.
    """

    def encryption(self, image_path, message):
        """
        Метод для шифрования сообщения в изображении в формате JPG.

        :param image_path: Путь к файлу изображения.
        :param message: Сообщение для шифрования.
        """
        try:
            # Прячем сообщения в изображении
            exifHeader.hide(image_path, image_path, message)
            filePath = os.getcwd()
            print(f'\nПуть до файла: {filePath}')
        except Exception as e:
            print(f'Произошла ошибка: {str(e)}')