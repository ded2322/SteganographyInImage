def menu_help():
    with open("menu_help.txt", "r", encoding="utf-8") as file:
        help_text = file.read()
    print(help_text)

    while True:
        user = input('Выйти в главное меню Д/Н: ')
        if user == 'Д' or 'д':
            break
