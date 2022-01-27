#!/usr/bin/python
#-*- coding:utf-8 -*-

import requests
from twilio.rest import TwilioRestClient

def getWeather():
    # 设置心知天气的apikey
    # 并构造请求URL
    xinzhi_apikey = "Sgi2-MxGwTEBjPwOp"
    url = "https://api.thinkpage.cn/v3/weather/daily.json?key=%s&location=guangzhou&language=zh-Hans&unit=c&start=0&days=5" % xinzhi_apikey

    # 获取天气预报信息
    # 此处只取今天和明天2天的预报
    r = requests.get(url)
    w = r.json()["results"][0]["daily"]
    today = "今天是%s，白天%s，晚上%s，最高气温%s，最低气温%s" % (w[0]["date"], w[0]["text_day"], w[0]["text_night"], w[0]["high"], w[0]["low"])
    tomorrow = "明天是%s，白天%s，晚上%s，最高气温%s，最低气温%s" % (w[1]["date"], w[1]["text_day"], w[1]["text_night"], w[1]["high"], w[1]["low"])
    message = today + '\n' + tomorrow
    return message

def sendMessage(message):
    '''接收传入的参数做为短信主体——即天气预报内容，发送到目标号码'''

    # 设置twilio账户信息
    twilio_account_sid = "2876355007@qq.com"
    twilio_auth_token = "hu_hHXXqL7nr-Hi-ixAHWqHLHNpOC93nwJDSpE_D"
    client = TwilioRestClient(twilio_account_sid, twilio_auth_token)

    # 注意to和from_两个参数所代表的手机号，都需要带有国家代码。如中国大陆手机号即+86开头再加上自己的手机号。from_中的号码直接复制twilio提供的号码即可
    client.messages.create(to="接收者的手机号", from_="twilio提供给你的收发信息的手机号", body=message)
    return None

if __name__ == "__main__":
    weather = getWeather()
    sendMessage(weather)