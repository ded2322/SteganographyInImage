from oop_app.mixins import FilePathCrypt,FilePathDecrypt
from oop_app.mixins import user_input,check_cyrillic


class Steganography:
    """

    """

    def encrypt(self):
        """

        """
        file_extension_crypt = FilePathCrypt.check_extension()

        message = user_input()
        message = check_cyrillic(message)
        file_extension_crypt["replica"].encryption(file_extension_crypt["image_path"], message=message)
    def decrypt(self):
        file_extension_decrypt = FilePathDecrypt.check_extension()

        file_extension_decrypt["replica"].decryption(file_extension_decrypt["image_path"])
