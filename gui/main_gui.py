import flet as ft
from PIL import Image
from stegano import lsb, exifHeader


def main(page: ft.Page):

    def hide_massage(e):

        def cryption_png(e):
            # todo проверка на путь, проверка окончания
            def data_user(e):
                if not file_path.value or not name_secret_image or not secret_message:
                    file_path.error_text = "Введите путь до изображения"
                    name_secret_image.error_text = "Введите название зашифрованного изображения"
                    secret_message.error_text = "Введите зашифрованное сообщение"
                    page.update()
                else:

                    file = file_path.value
                    secret_image = name_secret_image.value
                    message = secret_message.value

                    with Image.open(file) as img:
                        if img.mode != 'RGB':
                            img = img.convert('RGB')
                            img.save(file)
                            print("Image converted to RGB")

                    secret = lsb.hide(file, message)
                    secret.save(secret_image)
                    page.clean()
                    page.add(ft.Text(f"Успешно зашифрованно!"))

            file_path = ft.TextField(hint_text="Path: ", width=300)
            name_secret_image = ft.TextField(hint_text=" name_secret_image: ", width=300)
            secret_message = ft.TextField(hint_text="Message: ", width=300)
            page.add(
                ft.Row([file_path, name_secret_image, secret_message, ft.ElevatedButton("Add", on_click=data_user)]))

        def cryption_jpg(e):
            # todo проверка на путь, проверка окончания, сделать более чистым
            def data_user(e):
                if not file_path.value or not name_secret_image or not secret_message:
                    file_path.error_text = "Введите путь до изображения"
                    name_secret_image.error_text = "Введите название зашифрованного изображения"
                    secret_message.error_text = "Введите зашифрованное сообщение"
                    page.update()
                else:

                    file = file_path.value
                    secret_image = name_secret_image.value
                    message = secret_message.value

                    exifHeader.hide(file, secret_image, message)
                    page.add(ft.Text(f"Успешно зашифрованно!"))

            file_path = ft.TextField(hint_text="Path: ", width=300)
            name_secret_image = ft.TextField(hint_text=" name_secret_image: ", width=300)
            secret_message = ft.TextField(hint_text="Message: ", width=300)
            page.add(
                ft.Row([file_path, name_secret_image, secret_message, ft.ElevatedButton("Add", on_click=data_user)]))

        page.add(ft.ElevatedButton(text="Шифровка сообщения в изображении (формат png)", on_click=cryption_png))
        page.add(ft.ElevatedButton(text="Шифровка сообщения в изображении (формат jpg)", on_click=cryption_jpg))

    def decryption(e):
        def decryption_png(e):
            def data_user(e):
                if not file_path.value:
                    file_path.error_text = "Введите путь до изображения"
                    page.update()
                else:
                    file = file_path.value
                    page.add(ft.Text(f"Зашифрованное сообщение: {lsb.reveal(file)}"))

            file_path = ft.TextField(hint_text="Path: ", width=300)
            page.add(ft.Row([file_path, ft.ElevatedButton("Add", on_click=data_user)]))

        def decryption_jpg(e):
            def data_user(e):
                if not file_path.value:
                    file_path.error_text = "Введите путь до изображения"
                    page.update()
                else:
                    file = file_path.value
                    message = exifHeader.reveal(file).decode()
                    page.add(ft.Text(f"Зашифрованное сообщение: {message}"))

            file_path = ft.TextField(hint_text="Path: ", width=300)
            page.add(ft.Row([file_path, ft.ElevatedButton("Add", on_click=data_user)]))

        page.add(ft.ElevatedButton(text="Дешифровка сообщения в изображении (формат png)", on_click=decryption_png))
        page.add(ft.ElevatedButton(text="Дешифровка сообщения в изображении (формат jpg)", on_click=decryption_jpg))

    page.add(ft.ElevatedButton(text="Зашифровать сообщение", on_click=hide_massage))
    page.add(ft.ElevatedButton(text="Дешифровать сообщение", on_click=decryption))


# Стартует приложение
ft.app(target=main)
