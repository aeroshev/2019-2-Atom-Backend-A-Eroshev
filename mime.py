#!/usr/bin/env python3.7

import magic

def get_mime(file_descr):
	mime = magic.from_buffer(file_descr.read(), mime=True)
	return mime

if __name__ = "__main__"
	with open('image.jpg', 'r') as finput:
		
