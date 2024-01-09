#!/usr/bin/env python3

import http.server

with http.server.HTTPServer(("", 1200), http.server.SimpleHTTPRequestHandler) as serv:
    serv.serve_forever()
