import sys

A_SIZE = 500
B_SIZE = 100
C_SIZE = 50

def get_lines():
    lines = []
    for line in sys.stdin:
        lines.append(line.strip("\n"))
    return lines

def count(a, b, c, x):
    l = [(a_c, b_c, c_c) for a_c in range(0, a+1) for b_c in range(0, b+1) for c_c in range(0, c+1) if A_SIZE * a_c + B_SIZE * b_c + C_SIZE * c_c == x]
    return len(l)

lines = get_lines()
a, b, c, x = [int(s) for s in lines]
print(count(a, b, c, x))
