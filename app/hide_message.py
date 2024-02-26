import os
from stegano import lsb, exifHeader

from utils import file_path, user_message, check_extension


def encryption_png():
    """

    :return:
    """
    try:
        # Прячем сообщения в изображении
        secret = lsb.hide(file_path(), user_message(True))
        # Сохранения изображения в файлах
        secret.save(check_extension('.png'))
        # Путь где лежит сохраненный файл
        filePath = os.getcwd()
        print(f'\nПуть до файла: {filePath}')
    except Exception as e:
        print(f'Произошла ошибка: {str(e)}')
