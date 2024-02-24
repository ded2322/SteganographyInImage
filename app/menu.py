from menu_help import menu_help
from hide_message import encryption_png

def user_chose():
    while True:
        user_input = int(input(
            "Выберете подходящий режим:\n"
            "1.Шифровка сообщения в изображении (формат png)\n"
            "2.Дешифровка сообщения из изображения (формат png)\n"
            "3.Шифровка сообщения в изображении (формат jpg)\n"
            "4.Дешифровка сообщения из изображения (формат jpg)\n"
            "5.Меню помощи\n"
            "6.Выйти из программы\n"
            "Ваш выбор: "))
        match user_input:
            case 1:
                encryption_png()
            case 2:
                break
            case 3:
                break
            case 4:
                break
            case 5:
                menu_help()
            case 6:
                print('Выход из программы')
                break
