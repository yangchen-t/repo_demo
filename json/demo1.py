#!/bin/python3

import json


with open('test.json',encoding='utf-8') as f:
    f.write(json.dumps(dict,indent=4))
