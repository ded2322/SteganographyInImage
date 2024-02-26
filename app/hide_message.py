import os
from stegano import lsb, exifHeader

from utils import check_extension,file_path,user_message


def encryption_png():
    """

    :return:
    """

    secret_image = input("Введите какое название вы хотите у зашифрованного изображения: ")
    secret_image = check_extension(secret_image,".png")


    try:
        #Прячем сообщения в изображении
        secret = lsb.hide(file_path(), user_message(True))
        #Сохранения изображения в файлах
        secret.save(secret_image)
        #Путь где лежит сохраненный файл
        filePath = os.getcwd()
        print(f'\nСообщение успешно зашифровано в {secret_image}.',
              f'\nПуть до файла: {filePath}')
    except Exception as e:
        print(f'Произошла ошибка: {str(e)}')

