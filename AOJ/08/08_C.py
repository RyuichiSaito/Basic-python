import sys

s = sys.stdin.read()
s = s.lower()
for c in "abcdefghijklmnopqrstuvwxyz":
    cnt = s.count(c)
    print(f'{c} : {cnt}')
