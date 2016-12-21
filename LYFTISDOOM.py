#!/usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals
import urllib
import urllib.request
from bs4 import BeautifulSoup
import json
import os
import requests
import sys


def get_google_auth_session(username, password, galx, gxf):
	session = requests.Session()
	google_accounts_url = 'http://accounts.google.com'
	authentication_url = 'https://accounts.google.com/ServiceLoginAuth'

	r = session.get(google_accounts_url)
	#galx = r.cookies['GALX']

	session.headers['User-Agent'] = \
		'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'
		
	session.headers['Content-Type'] = \
		'application/x-www-form-urlencoded'
		
	session.headers['Accept-Language'] = \
		'en-US,en;q=0.5'

	payload = {'Page': 'PasswordSeparationSignIn',
			   'GALX': galx,
			   'gxf': gxf,
			   'continue': 'https://www.google.com/voice',
			   'followup': 'https://www.google.com/voice',
               '_utf8': '%E2%98%83',
			   'service': 'grandcentral',
			   'ltmpl': 'open',
			   'ProfileInformation': '',
			   'SessionState': '',
			   # This is normally in the request.
			   # bgresponse: this is a js function on post gaia_onLoginSubmit()
			   'bgresponse': 'js_disabled',
			   'pstMsg': 1,
			   'checkConnection': '',
			   'checkedDomains': 'youtube',
			   'identifiertoken': '',
			   'identifiertoken_audio': '',
			   'identifier-captcha-input': '',
			   'Email': username,
			   'Passwd': password,
			   'PersistentCookie': 'yes',
			   'rmShown': '1'}

	r = session.post(authentication_url, data=payload)

	if r.url != authentication_url:
		print(str(r.url))
		print("Logged in")
	else:
		print("login failed")
		sys.exit(1)

	return session


def writeFile(content):
	with open("file.txt", "w") as att_file:
		att_file.write(content)

def initPage():
	page = urllib.request.urlopen('https://accounts.google.com/ServiceLogin?service=grandcentral&passive=1209600&continue=https%3A%2F%2Fwww.google.com%2Fvoice&followup=https%3A%2F%2Fwww.google.com%2Fvoice&ltmpl=open')
	return(page.read())
	
def findVar(soup):
	try:
		galx = soup.find('input', {'name': 'GALX'}).get('value')
		gxf = soup.find('input', {'name': 'gxf'}).get('value')
		return galx, gxf
	except:
		pass
		
if __name__ == '__main__':
	body = initPage()
	soup = BeautifulSoup(body, 'html.parser')
	ret_var = findVar(soup)
	name = 'dasneko13@gmail.com'
	pswd = 'concac12'
	galx = str(ret_var[0])
	gfx = str(ret_var[1])
	g_session = get_google_auth_session(name, pswd, galx, gfx)
	voice_url = 'https://www.google.com/voice/b/0#inbox'
	r = g_session.get(voice_url)
	if r.status_code != 200:
		print(r.status_code)
	else:
		soup = BeautifulSoup(r.text, 'html.parser')
		print(soup.prettify())
		print("\n\n\n" + str(g_session))