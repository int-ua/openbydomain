#!/usr/bin/env python3

import sys
import csv

from urllib.parse import urlparse


if len(sys.argv) < 2:
    exit()

parsed_url = urlparse(sys.argv[1])
domain = parsed_url.netloc

if not domain:
    exit()

with open('openbydomain.csv') as csvfile:
    reader = csv.reader(csvfile)
    dispatch_dict = {row[0]: row[1] for row in reader}

print(dispatch_dict[domain])
