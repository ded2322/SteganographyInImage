from abc import ABC, abstractmethod
from stegano import lsb, exifHeader


class DecryptionFabric(ABC):
    """
    Абстрактный базовый класс для фабрики дешифрования.
    """

    @abstractmethod
    def decryption(self, file_path):
        """
        Абстрактный метод для дешифрования изображения.

        :param file_path: Путь к файлу изображения.
        """
        pass


class PNGDecryptionFabric(DecryptionFabric):
    """
    Класс фабрики дешифрования для изображений в формате PNG.
    """

    def decryption(self, file_path):
        """
        Метод для дешифрования сообщения из изображения в формате PNG.

        :param file_path: Путь к файлу изображения.
        """
        try:
            decrypted_message = lsb.reveal(file_path)
            print("Зашифрованное сообщение: " + decrypted_message + "\n")
        except FileNotFoundError:
            print("Файл не найден.")
        except Exception as e:
            print(f"Произошла ошибка: {str(e)}")


class JPGDecryptionFabric(DecryptionFabric):
    """
    Класс фабрики дешифрования для изображений в формате JPG.
    """

    def decryption(self, file_path):
        """
        Метод для дешифрования сообщения из изображения в формате JPG.

        :param file_path: Путь к файлу изображения.
        """
        try:
            decrypted_message = exifHeader.reveal(file_path).decode()
            print("Зашифрованное сообщение: " + decrypted_message + "\n")
        except FileNotFoundError:
            print("Файл не найден.")
        except Exception as e:
            print(f"Произошла ошибка: {str(e)}")
