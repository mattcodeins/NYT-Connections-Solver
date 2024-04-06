# -*- coding: utf-8 -*-
import csv
from random import shuffle

with open("answers.txt", 'r') as f:
    lines = f.readlines()

puzzles = []
allwords = []
for i, l in enumerate(lines):
    if i % 5 != 0:
        l = l.strip("    ◦ ").strip('\n')
        _, words = l.split(" - ")
        words = words.split(", ")
        allwords.extend(words)
    elif i > 0:
        shuffle(allwords)
        puzzles.append(allwords)
        allwords = []
shuffle(allwords)
puzzles.append(allwords)

with open('questions.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(puzzles)