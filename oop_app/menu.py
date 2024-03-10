from oop_app.mixins import FilePathCrypt
from oop_app.steganography import Steganography
class Menu:

    def user_choice(self):
        while True:
            user_input = int(input(
                "Выберете подходящий режим:\n"
                "1. Шифровка сообщения в изображении\n"
                "2. Дешифровка сообщения из изображения\n"
                "3. Меню помощи\n"
                "4. Выйти из программы\n"
                "Ваш выбор: "
            ))

            match user_input:
                case 1:
                    encryptor = Steganography()
                    encryptor.encrypt()
                case 2:
                    ...
                case 3:
                    ...
                case 4:
                    ...
