#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

client_id = 'a3c5228f989faca0eccb'
client_secret = 'def2bcdde7aa19f45ccd196d31df171f3235e544'
code = '79bb951cefc1b0621210'

a_token_test = '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'


# https://github.com/login/oauth/authorize?client_id=a3c5228f989faca0eccb&scope=respo

if __name__ == '__main__':


	url = 'https://github.com/login/oauth/access_token'
	payload = {'client_id': client_id, 'client_secret': client_secret, 'code': code}
	header = {'Accept' : 'application/json'}

	response = requests.post(url, json=payload, headers=header)

	if response.status_code == 200:
		response_json = response.json()
		error_descrip = response_json['error_description']
		# access_token = response_json['access_token'] 
		access_token = a_token_test
		print(error_descrip)
		print(access_token)
	


	