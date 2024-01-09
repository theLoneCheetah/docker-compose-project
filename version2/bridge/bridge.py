#!/usr/bin/env python3

import requests
import flask
import os

name = 'bridge'
app = flask.Flask(name)

@app.route('/')
def hello():
  response = requests.get(os.environ['SERVER_URL'])
  st = response.text + " Have a nice day!"
  return st

if name == 'bridge':
  app.run(host='0.0.0.0', port=os.environ['SELF_PORT'])
