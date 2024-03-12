from app.steganography import Steganography
from app.tools import menu_help, user_message, check_cyrillic, user_path, check_extension


class Menu:
    """
   Класс Menu представляет меню выбора пользователя.
   """

    def user_choice(self):
        """
       Метод user_choice() обрабатывает выбор пользователя из меню.
       Используется бесконечный цикл для повторного отображения меню после каждого выбора.
       """
        while True:
            user_input = int(input(
                "Выберете подходящий режим:\n"
                "1. Шифровка сообщения в изображении\n"
                "2. Дешифровка сообщения из изображения\n"
                "3. Меню помощи\n"
                "4. Выйти из программы\n"
                "Ваш выбор: "
            ))
            steganography = Steganography()
            match user_input:
                case 1:
                    steganography.encrypt()
                case 2:
                    steganography.decrypt()
                case 3:
                    menu_help()
                case 4:
                    break
