#!/usr/bin/env python3

import flask
import os

name = 'server'
app = flask.Flask(name)

@app.route('/')
def hello():
  return flask.render_template('hello.html')

if name == 'server':
  app.run(host='0.0.0.0', port=os.environ['SELF_PORT'])
