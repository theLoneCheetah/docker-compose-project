#!/usr/bin/env python3

import flask

name = 'main'
app = flask.Flask(name)

@app.route('/')
def hello():
  return flask.render_template('hello.html')

if name == 'main':
  app.run(host='0.0.0.0', port=1001)
