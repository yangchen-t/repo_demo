#!/bin/python3

import yaml

f = open(r'/home/westwell/Desktop/scripts/cxy/configparser/config.yaml')
y = yaml.load(f)
print(y)