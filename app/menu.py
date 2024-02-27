from menu_help import menu_help
from hide_message import encryption_png, encryption_jpg
from decryption_message import decryption_png, decryption_jpg


def user_chose():
    while True:
        user_input = int(input(
            "Выберете подходящий режим:\n"
            "1. Шифровка сообщения в изображении (формат png)\n"
            "2. Дешифровка сообщения из изображения (формат png)\n"
            "3. Шифровка сообщения в изображении (формат jpg)\n"
            "4. Дешифровка сообщения из изображения (формат jpg)\n"
            "5. Меню помощи\n"
            "6. Выйти из программы\n"
            "Ваш выбор: "))
        match user_input:
            case 1:
                encryption_png()
            case 2:
                decryption_png()
            case 3:
                encryption_jpg()
            case 4:
                decryption_jpg()
            case 5:
                menu_help()
            case 6:
                print('Выход из программы')
                break
