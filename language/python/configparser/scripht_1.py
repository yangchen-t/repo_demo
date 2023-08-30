#!/bin/python3

import configparser as config
import os


conf = config.ConfigParser()
# print(conf)

path = os.getcwd()
# print(path)
path = os.path.dirname(path)

path = path+'/configparser/demo_conf1.ini'
print(path)
conf.read(path)
# print(a)
secs = conf.sections()
print(secs)
sections1 = conf.options('section1')
print(sections1)
sections1_item = conf.items('section1')
print(sections1_item)
sections1_get = conf.get('section1','name')
print(sections1_get)
add_config = conf.add_section('section3')
print(add_config)
add_config = conf.set('section3','age','25')
print(conf.items('section3'))
conf.write(open('scripht_1.py','w'))