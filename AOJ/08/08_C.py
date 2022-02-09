s = ''
while True:
    try:
        cur = input()
        s += cur
    except:
        break

s = s.lower()
for c in "abcdefghijklmnopqrstuvwxyz":
    countable=s.count(c)
    print('{} : {}'.format(c, countable))