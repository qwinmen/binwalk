#Задача: распаковать указанный zlib файл.
#Src https://unix.stackexchange.com/a/22836
#Example use in CMD: python zlibExpander.py --targetFile=F1826c.zlib

import glob
import zlib
import sys
import argparse

parser = argparse.ArgumentParser(description='Script so useful.')
parser.add_argument("--targetFile")
args = parser.parse_args()

with open(args.targetFile, 'rb') as compressed:
	with open(args.targetFile + '-decompressed', 'wb') as expanded:
		data = zlib.decompress(compressed.read())
		expanded.write(data)
