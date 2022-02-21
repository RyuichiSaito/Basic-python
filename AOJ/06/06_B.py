tranp = [[] for _ in range(4)]
idxs = ['S', 'H', 'C', 'D']
for _ in range(int(input())):
    a, x = map(str, input().split())
    idx = idxs.index(a)
    tranp[idx].append(int(x))

for i in range(4):
    tranp[i].sort()
    for j in range(1, 14):
        if j not in tranp[i]:
            print('{} {}'.format(idxs[i], j))
