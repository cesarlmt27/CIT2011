#!/usr/bin/env python
import sys
import os
import re

filename = os.environ["map_input_file"]
filename = os.path.split(filename)[-1]

for line in sys.stdin:
    line = line.strip()
    words = re.findall(r'\b[a-zA-Z]+\b', line)
    for word in words:
        print(f'{word}\t{filename}\t1')