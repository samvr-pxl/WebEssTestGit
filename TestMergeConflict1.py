import sys
import os
import string

if len(sys.argv) < 2:
	print('not enough arguments')
	sys.exit()
	
infilename = sys.argv[1];

name, ext = os.path.splitext(infilename)
outfilename = "{name}_{app}{ext}".format(name=name, app='filtered', ext=ext)
out = open(outfilename, 'w')
	
for line in open(infilename, 'r'):
	if not line:
		break
	else:
		parts = line.split("	")
		newline = "changed locally"
		out.write(newline)
