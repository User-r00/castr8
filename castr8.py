#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import progressbar
import requests

base_url = 'https://cstr-vod.castr.io/videos/vd06d793709dee11eabec4/fvs27LRyIhAclk15.mp4/tracks-v1a1/'

with open('output.mov', 'ab') as f:
	for segment_count in progressbar.progressbar(range(740)):
		segment_count += 1
		with requests.Session() as session:
			try:
				data = session.get(f'{base_url}segment{segment_count}.ts', stream=True)
				f.write(data.content)
			except requests.exceptions.RequestException as e:
				raise e