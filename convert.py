import os, sys
from PIL import Image


def _get_out_path(in_path):
	directory, _ = os.path.split(in_path)
	filename = 'favicon.ico'
	out_path = os.path.join(directory, filename)
	return out_path

in_path = sys.argv[1]
icon_sizes = [(16,16), (32, 32), (48, 48), (64,64)]
img = Image.open(in_path)
img.save(_get_out_path(in_path), sizes=icon_sizes)
