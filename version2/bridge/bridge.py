#!/usr/bin/env python3

import requests
import flask

name = 'main'
app = flask.Flask(name)

@app.route('/')
def hello():
  response = requests.get("http://server:1001")
  st = response.text + " Have a nice day!"
  return st

if name == 'main':
  app.run(host='0.0.0.0', port=1001)
