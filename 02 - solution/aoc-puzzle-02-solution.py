import os
from pathlib import Path
import csv
from collections import Counter

#open file
data_directory = os.path.dirname(os.path.abspath(__file__))
data_file = 'source-file/aoc-2018-02-input.txt'
source_file = os.path.join(data_directory,data_file)

def countLetters(rows):
    unique_list = ''.join(set(rows))
    return unique_list

def countTwo():
    
    return False

def countThree():
    if countLetters(rows) > 2:
        return True
    else:
        return False

two_count = 0
three_count = 0

with open(source_file) as f:

    data = f.read().splitlines()
    
    for rows in data:
        counter = Counter(rows)
        for char in unique_list:
            if counter[char] > 2:
                three_count += 1
                break
            elif counter[char] > 1:
                 two_count += 1
                 break

print(two_count)
print(three_count)