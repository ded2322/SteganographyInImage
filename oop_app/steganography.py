from oop_app.mixins import FilePathCrypt
from oop_app.mixins import user_input,check_cyrillic


class Steganography:
    """

    """
    #decryption_strategy
    def __init__(self):
        self.file_extension = FilePathCrypt.check_extension()

    def encrypt(self):
        """

        """
        message = user_input()
        message = check_cyrillic(message)
        self.file_extension["replica"].encryption(self.file_extension["image_path"],message=message)
    #def decrypt(self):
    #    self.encryption_strategy.encryption(self)