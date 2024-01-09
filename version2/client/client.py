#!/usr/bin/env python3

import requests
import os
import time

response = requests.get(os.environ['SERVER_URL'])
print(response.text)
while True:
    True
