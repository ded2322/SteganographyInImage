import pytest
from app.encrypt_fabric import PNGEncryptionFabric, JPGEncryptionFabric
from app.decryption_fabric import PNGDecryptionFabric, JPGDecryptionFabric
import os


def create_encryption_fabric(fabric_type):
    fabrics = {
        'png': PNGEncryptionFabric,
        'jpg': JPGEncryptionFabric
    }
    return fabrics[fabric_type]()


def create_decrypt_fabric(fabric_type):
    fabrics = {
        "png": PNGDecryptionFabric,
        "jpg": JPGDecryptionFabric
    }
    return fabrics[fabric_type]()


@pytest.fixture
def decrypt_fabric(request):
    return create_decrypt_fabric(request.param)


@pytest.fixture
def encryption_fabric(request):
    return create_encryption_fabric(request.param)


@pytest.fixture
def image_path(request):
    image_paths= {
        "png":"C:\\Users\\mdebc_nwrashl\\PycharmProjects\\stegonagrafy\\tests\\загружено.png",
        "jpg": "C:\\Users\\mdebc_nwrashl\\PycharmProjects\\stegonagrafy\\tests\\2.jpg"
    }
    return image_paths[request.param]


@pytest.fixture
def message():
    return "Test message"
