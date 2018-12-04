#AoC Puzzle 01 Solution
import os
from pathlib import Path

startingFrequency = 0

data_directory = os.path.dirname(os.path.abspath(__file__))
data_file = 'source-file/input-01.txt'

source_file = os.path.join(data_directory,data_file)

with open(source_file) as f:
    data = f.readlines()
    for rows in data:
        operand = rows[:1]
        if operand == '+':
            startingFrequency = startingFrequency + int(rows[1:])
        else:
            startingFrequency = startingFrequency - int(rows[1:])
    print(startingFrequency)