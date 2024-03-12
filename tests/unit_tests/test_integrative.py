import pytest


@pytest.mark.parametrize(
    "encryption_fabric, decrypt_fabric, image_path",
    [("png", "png", "png"), ("jpg", "jpg", "jpg")],
    indirect=True,
)
def test_encrypt_decrypt(encryption_fabric, decrypt_fabric, image_path, message):
    # Тест шифрования и дешифрования сообщения
    encryption_fabric.encryption(image_path, message)
    decrypted_message = decrypt_fabric.decryption(image_path)
    assert decrypted_message == message
