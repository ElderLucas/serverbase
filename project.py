#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
print "im ok"
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!'

if __name__ == '__main__':
	app.secret_key = 'super_secret_key'
	#app.debug = True
	app.run(host='localhost', port=4567)