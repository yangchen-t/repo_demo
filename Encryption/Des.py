
import binascii
from pyDes import des, CBC, PAD_PKCS5
# 需要安装 pip install pyDes
    
def des_encrypt(secret_key, s):
     iv = secret_key
     k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
     en = k.encrypt(s, padmode=PAD_PKCS5)
     return binascii.b2a_hex(en)
    
def des_decrypt(secret_key, s):
     iv = secret_key
     k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
     de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
     return de
    
secret_str = des_encrypt('12345678', 'I love YOU~')
print(secret_str)
clear_str = des_decrypt('12345678', secret_str)
print(clear_str)