#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess
from typing import List 

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dir: str) -> List[str]:
  filenames = os.listdir(dir)
  paths = []
  for file in filenames:
    if re.search(r'.*__\w+__.*', file):
      paths.append(os.path.abspath(os.path.join(dir, file)))
  return paths

def copy_to(paths: List[str], dir: str) -> None:
  '''Copies files into given location'''
  if not os.path.exists(dir):
    os.makedirs(dir)
  try:
    for path in paths:
      shutil.copy(path, dir)
  except IOError:
    print('Cannot copy the files.')

def zip_to(paths: List[str], zippath: str) -> None:
  '''Zips files into given zipfile'''
  cmd = f'zip -j {zippath} ' + ' '.join(paths)
  (status, output) = subprocess.getstatusoutput(cmd)
  if status:
    print(output)
  return

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print('usage: [--todir dir][--tozip zipfile] dir [dir ...]')
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if not args: # A zero length array evaluates to "False".
    print('error: must specify one or more dirs')
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  paths = get_special_paths(args[0])
  if not todir and not tozip:
    print(*paths, sep='\n')
  elif todir:
    copy_to(paths, todir)
  elif tozip:
    zip_to(paths,tozip)

if __name__ == '__main__':
  main()
