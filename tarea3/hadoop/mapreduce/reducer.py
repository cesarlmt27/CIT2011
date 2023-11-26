#!/usr/bin/env python
import sys
from collections import defaultdict
import re

current_word = None
current_list = defaultdict(int)

for line in sys.stdin:
    line = line.strip()
    word, filename, count = line.split('\t')
    count = int(count)

    doc_number = re.search(r'\d+', filename).group()

    if current_word == word:
        current_list[doc_number] += count
    else:
        if current_word:
            print(f'{current_word}\t' + ', '.join(f'({k}, {v})' for k, v in current_list.items()))
        current_word = word
        current_list = defaultdict(int)
        current_list[doc_number] += count

if current_word == word:
    print(f'{current_word}\t' + ', '.join(f'({k}, {v})' for k, v in current_list.items()))