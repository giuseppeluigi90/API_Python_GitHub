#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

client_id = 'a3c5228f989faca0eccb'
client_secret = 'def2bcdde7aa19f45ccd196d31df171f3235e544'
code = '79bb951cefc1b0621210'

a_token_test = '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'


# https://github.com/login/oauth/authorize?client_id=a3c5228f989faca0eccb&scope=respo

if __name__ == '__main__':
	url = 'http://api.github.com/user/repos'
	headers = {'Authorization' : 'token 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'}

	response = requests.get(url, headers=headers)

	if response.status_code == 200:
		payload = response.json()

		for project in payload:
			name = project['name']
			full_name = project['full_name']
			html_url = project['html_url']
			description = project['description']
			print("*****************")
			print({name})
			print(full_name)
			print(html_url)
			print(description)


	else:
		print(response.content)

	