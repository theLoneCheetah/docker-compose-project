#!/usr/bin/env python3

import urllib.request

with urllib.request.urlopen("http://server:1200/") as url:
	encoded = url.read()
	decoded = encoded.decode("utf8")
	print(decoded)
