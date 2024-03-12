import pytest
@pytest.mark.parametrize("decrypt_fabric, image_path",
                         [("png","png"),
                         ("jpg","jpg"),]
    ,indirect=True)
def test_decrypt(decrypt_fabric,image_path, message):
        # тест для проверки шифрования
        message_image = decrypt_fabric.decryption(image_path)
        assert message_image == message