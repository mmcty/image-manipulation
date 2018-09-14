import os, sys
from PIL import Image

sizes = [1024, 180, 167, 152, 120, 87, 80, 76, 60, 58, 40, 29, 20]

def _get_out_path(in_path, dim):
	directory, filename = os.path.split(in_path)
	filenames = filename.split('_')
	filename = "{0}_{1}.png".format(filenames[0], dim)
	out_path = os.path.join(directory, filename)
	return out_path

def _resize(in_path, dim):
	out_path = _get_out_path(in_path, dim)
	in_image = Image.open(in_path)
	out_image = in_image.resize((dim, dim), Image.LANCZOS)
	print(out_path)
	out_image.save(out_path, 'png') 

in_path = sys.argv[1]
[_resize(in_path, s) for s in sizes]