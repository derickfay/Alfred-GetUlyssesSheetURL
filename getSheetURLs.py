#!/usr/bin/python

# written for Python 2.7.10 as shipped in Mac OS Sierra

import json
import os
import urllib

def my_generator(json_input):
	if isinstance(json_input, dict):
		for k, v in json_input.iteritems():
			if k == 'title':
				ti = v.replace('"', '').replace(',', '').replace(':','')
			elif k == 'identifier':
				arg = v
			elif k == 'type':
				subti = v
			else:
				for child_val in my_generator(v):
					yield child_val
		yield json.dumps({u'title': ti, u'arg': '['+ti+'](ulysses://x-callback-url/open?id='+arg+')', u'subtitle': subti})
	elif isinstance(json_input, list):
		for item in json_input:
			for item_val in my_generator(item):
				yield item_val

tmp = os.popen('/Applications/xcall.app/Contents/MacOS/xcall -url "ulysses://x-callback-url/get-root-items?recursive=YES&access-token=YOURTOKENHERE"').read()

ulyssesLib = json.loads(urllib.unquote(tmp).decode('utf8'))

items = json.loads(urllib.unquote(ulyssesLib['items']))[0]

print('{"items":'+str(list(my_generator(items))).replace('\\\'','').replace('\'','')+'}')
