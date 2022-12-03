from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


class EncryptStr(object):
    def __init__(self, key):
        self.key = key
        self.mode = AES.MODE_CBC

    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        length = 16
        count = len(text)
        if (count % length != 0):
            add = length - (count % length)
        else:
            add = 0
        text = text + ('\0' * add)
        self.ciphertext = cryptor.encrypt(text)
        return b2a_hex(self.ciphertext)

    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return plain_text.decode('utf-8').strip('\0')

if __name__ == '__main__':
    pc = EncryptStr('keyskeyskeyskeys')  # 初始化密钥
    e = pc.encrypt("192.168.103.77")
    d = pc.decrypt("0e0dbd0509f9eaaafd420b8a2c72cbde")
    print(e, d)