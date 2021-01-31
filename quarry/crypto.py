import hashlib
import os


from cryptography.hazmat.primitives import ciphers, serialization
from cryptography.hazmat.primitives.ciphers import algorithms, modes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend


backend = default_backend()


def make_server_id():
    return b""


def make_verify_token():
    return os.urandom(4)


def make_shared_secret():
    return os.urandom(16)


def make_digest(*data):
    sha1 = hashlib.sha1()
    for d in data:
        sha1.update(d)

    digest = int(sha1.hexdigest(), 16)
    if digest >> 39*4 & 0x8:
        return"-%x" % ((-digest) & (2**(40*4)-1))
    else:
        return "%x" % digest


def make_cipher(key):
    return ciphers.Cipher(algorithms.AES(key), modes.CFB8(key), backend=backend)


def make_keypair():
    return rsa.generate_private_key(
        public_exponent=65537,
        key_size=1024,
        backend=default_backend())


def pack_public_key(keypair):
    return keypair.public_key().public_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PublicFormat.SubjectPublicKeyInfo)


def unpack_public_key(data):
    return serialization.load_der_public_key(
        data=data,
        backend=default_backend())


def encrypt_secret(public_key, shared_secret):
    return public_key.encrypt(
        plaintext=shared_secret,
        padding=padding.PKCS1v15())


def decrypt_secret(keypair, data):
    return keypair.decrypt(
        ciphertext=data,
        padding=padding.PKCS1v15())
