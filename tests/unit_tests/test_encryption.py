import os
import pytest


@pytest.mark.parametrize("encryption_fabric, image_path",
                         [("png","png"),
                          ("jpg","jpg")],
                         indirect=True)
def test_encrypt(encryption_fabric, image_path, message):
    # тест для проверки дешифрования
    encryption_fabric.encryption(image_path= image_path, message=message)
    assert os.path.exists(image_path), f"Файл изображения {image_path} не найден"
