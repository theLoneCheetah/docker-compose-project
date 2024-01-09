#!/usr/bin/env python3

import http.server
import socketserver

with http.server.HTTPServer(("", 1200), http.server.SimpleHTTPRequestHandler) as serv:
    serv.serve_forever()
