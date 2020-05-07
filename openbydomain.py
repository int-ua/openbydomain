#!/usr/bin/env python3

import csv
import os
import subprocess
import sys

from urllib.parse import urlparse


if len(sys.argv) < 2:
    exit()

os.chdir(os.path.dirname(sys.argv[0]))

parsed_url = urlparse(sys.argv[1])
domain = parsed_url.netloc

with open('openbydomain.csv') as csvfile:
    reader = csv.reader(csvfile)
    dispatch_dict = {row[0]: row[1] for row in reader}

if 'default' not in dispatch_dict:
    print('No default executable in config', file=sys.stderr)
    exit(1)

executable = dispatch_dict.get(domain, dispatch_dict['default'])
subprocess.Popen([executable, sys.argv[1]])
