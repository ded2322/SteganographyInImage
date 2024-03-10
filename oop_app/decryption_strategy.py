from abc import ABC, abstractmethod
from stegano import lsb, exifHeader

class DecryptionFabric(ABC):
    @abstractmethod
    def decryption(self, file_path):
        pass

class PNGDecryptionFabric(DecryptionFabric):
    """

    """

    def decryption(self,file_path):
        try:
            print("Зашифрованное сообщение: " + lsb.reveal(file_path), "\n")
        except (FileNotFoundError, Exception) as e:
            if isinstance(e, FileNotFoundError):
                print("Файл не найден.")
            elif isinstance(e, Exception):
                print(f"Произошла ошибка: {str(e)}")
class JPGDecryptionFabric(DecryptionFabric):
    """

    """
    def decryption(self,file_path):
        try:
            print("Зашифрованное сообщение: " + exifHeader.reveal(file_path).decode(), "\n")
        except (FileNotFoundError, Exception) as e:
            if isinstance(e, FileNotFoundError):
                print("Файл не найден.")
            elif isinstance(e, Exception):
                print(f"Произошла ошибка: {str(e)}")
