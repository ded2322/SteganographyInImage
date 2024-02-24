import os
from stegano import lsb, exifHeader

from utils import check_image, check_cyrillic, check_extension


def encryption_png():
    #todo заставить работать путь до изображения
    #todo сделать отображение куда сохраняется путь
    image_path = input("Введите путь до изображения: ")
    if check_image(image_path):
        return ("Неверный путь до изображения")
    secret_image = input("Введите какое название вы хотите у зашифрованного изображения: ")
    secret_image = check_extension(secret_image,".png")

    massage_user = input("Введите сообщение которое хотите зашифровать: ")
    massage_user = check_cyrillic(massage_user)

    try:
        #Прячем сообщения в изображении
        secret = lsb.hide(image_path, massage_user)
        #Сохранения изображения в файлах
        secret.save(secret_image)
        #Путь где лежит сохраненный файл

        print('\n'+f'Сообщение успешно зашифровано в {secret_image}')
    except Exception as e:
        print(f'Произошла ошибка: {str(e)}')