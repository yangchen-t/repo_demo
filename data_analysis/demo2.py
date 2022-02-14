#!/binpython3


import requests

response = requests.get("https://work.weixin.qq.com/")
# 7. 返回CookieJar对象:
cookiejar = response.cookies
# 8. 将CookieJar转为字典：
cookiedict = requests.utils.dict_from_cookiejar(cookiejar)

print(cookiejar)
print(cookiedict)
