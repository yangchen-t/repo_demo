import base64


# 编码： 字符串 -> 二进制 -> base64编码
#b64_name = base64.b64encode(name.encode())
b64_name = b'Z2F0ZUB3ZXN0Iw=='
#print(b64_name)
# b'546L5aSn6ZSk'

# 解码：base64编码 -> 二进制 -> 字符串
print(base64.b64decode(b64_name).decode())
