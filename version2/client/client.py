#!/usr/bin/env python3

import requests

response = requests.get("http://bridge:1001")
print(response.text)
