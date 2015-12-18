# -*- coding:utf-8 -*-

import sys
import fileinput
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-e', '--encoding', default=None)
parser.add_argument('search', help="search word")
parser.add_argument('files', nargs="+")


args = parser.parse_args()

search = args.search
def enc_open(filename, mode):
    return open(filename, mode=mode, encoding=args.encoding)

with fileinput.FileInput(files=args.files, 
                         openhook=enc_open) as f:
  for line in f:
      if line.find(search) > -1:
          print("{0:20}:{1:4} {2}".format(
                f.filename(), f.lineno(), line))
