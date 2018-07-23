import os
import sys

for line in sys.stdin:
    line = line.rstrip().strip()
    if not ("*" in line or ">" in line or "/user/" in line or "++" in line):
        print(line)