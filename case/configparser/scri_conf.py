#!/bin/python3

import yaml

f = open(r'/home/westwell/scripts/python/cxy/case/configparser/config.yaml')
y = yaml.load(f)
print(y)