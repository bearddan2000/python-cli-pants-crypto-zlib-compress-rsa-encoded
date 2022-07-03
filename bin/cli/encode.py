from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
from compress import PasswordCompress

class PasswordHash:
    pc = PasswordCompress()
    keyPair = RSA.generate(3072)
    pubKey = keyPair.publickey()
    pubKeyPEM = ''
    privKeyPEM = ''

    def __init__(self):
        self.pubKeyPEM = self.pubKey.exportKey()
        self.privKeyPEM = self.keyPair.exportKey()

    def encrypt(self, password):
        password = bytes(password, encoding='utf-8')
        encryptor = PKCS1_OAEP.new(self.pubKey)
        password = encryptor.encrypt(password)
        return self.pc.compress(password)

    def decrypt(self, password):
        password = self.pc.decompress(password)
        decryptor = PKCS1_OAEP.new(self.keyPair)
        return decryptor.decrypt(password).decode('utf-8')
