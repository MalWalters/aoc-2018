#AoC Puzzle 01 Solution
import os
from pathlib import Path

frequency = 0
data_directory = os.path.dirname(os.path.abspath(__file__))
data_file = 'source-file/input-01.txt'
frequency_list = []
change_list = []
found_duplicate = False
loop_count = 0

source_file = os.path.join(data_directory,data_file)

with open(source_file) as f:
    data = f.readlines()
    # Populate change list
    for rows in data:
        change_list.append(rows)
    while not found_duplicate:
        loop_count += 1
        for entries in change_list:
            if entries[:1] == '+':
                frequency = frequency + int(entries[1:])
            else:
                frequency = frequency - int(entries[1:])
            if frequency in frequency_list:
                print("Duplicate Frequency is: "+ str(frequency))
                found_duplicate = True
                break
            frequency_list.append(frequency)