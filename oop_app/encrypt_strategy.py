import os

from abc import ABC, abstractmethod
from stegano import lsb, exifHeader


class EncryptionFabric(ABC):
    @abstractmethod
    def encryption(self, image_path, message):
        pass

    @abstractmethod
    def decryption(self,image_path):
        pass

class PNGEncryptionFabric(EncryptionFabric):

    def encryption(self, image_path, message):

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

    def encryption(self, image_path, message):
        try:
            # Прячем сообщения в изображении
            exifHeader.hide(image_path, image_path, message)
            filePath = os.getcwd()
            print(f'\nПуть до файла: {filePath}')
        except Exception as e:
            print(f'Произошла ошибка: {str(e)}')
