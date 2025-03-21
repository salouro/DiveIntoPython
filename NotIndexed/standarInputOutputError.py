import sys
import os

for i in range(3):
    print("Mancuelen")

#stdout é uma Stream, porém apenas-escrita
for i in range(3):
    l = sys.stdout.write(f"Ele é {os.linesep}")

#stderr é uma Stream
for i in range(3):
    l = sys.stderr.write(f"o mancuelen {os.linesep}")
