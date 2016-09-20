#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
import os
from flask import make_response
import requests

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

app = Flask(__name__)

app_path = os.getcwd()
os.chdir(app_path)



@app.route('/')
def hello_world():

	#return "Hello World"
	return render_template('main.html')

@app.route('/artesanatos')
def artesanatos():
	return "ok show Artesanatos"


@app.route('/kits')
def kits():
	return "ok show kits"

@app.route('/contatos')
def contatos():
	return "ok show Contatos"

@app.route('/about')
def about():
	return "ok show about Me"


if __name__ == '__main__':
	app.secret_key = 'super_secret_key'
	#app.debug = True
	app.run(host='localhost', port=4567)