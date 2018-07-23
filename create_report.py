import os
import sys
import collections

with open('courses.txt') as infile:
    counts = collections.Counter(line.rstrip().strip() for line in infile)
for line, count in counts.most_common():
    print(line, count)

