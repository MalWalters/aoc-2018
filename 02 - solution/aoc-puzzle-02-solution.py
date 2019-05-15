import os
from pathlib import Path
import csv
from collections import Counter

#open file
data_directory = os.path.dirname(os.path.abspath(__file__))
data_file = 'source-file/aoc-2018-02-input.txt'
source_file = os.path.join(data_directory,data_file)

two_count = 0
three_count = 0

with open(source_file) as f:
    data = f.read().splitlines()
    for rows in data:
        counter = Counter(rows)
        elements = counter.values()
        if 3 in elements:
            three_count += 1
        if 2 in elements:
            two_count +=1

print(two_count*three_count)