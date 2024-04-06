# -*- coding: utf-8 -*-
import csv

with open("answers.txt", 'r') as f:
    lines = f.readlines()

puzzles = []
groups = []
for i, l in enumerate(lines):
    if i % 5 != 0:
        l = l.strip("    ◦ ").strip('\n')
        cat, words = l.split(" - ")
        words = words.split(", ")
        groups.append((cat, words))
    elif i > 0:
        puzzles.append(groups)
        groups = []
puzzles.append(groups)

with open('answers.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(puzzles)