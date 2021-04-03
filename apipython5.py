#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

if __name__ == '__main__':
	url = 'https://api.github.com/user'

	session = requests.session()
	session.auth = ('giuseppeluigi90@outlook.com', 'restuccia2702')

	response = session.get(url)

	if response.status_code == 200:
		print(response.content)
	else:
		print(response.content)

	
