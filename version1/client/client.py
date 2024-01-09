#!/usr/bin/env python3

import requests

response = requests.get("http://server:1200/")
print(response.text)
