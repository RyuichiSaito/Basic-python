from itertools import combinations


def solve(n, x):
    C = list(combinations(range(1, n+1), 3))
    cnt = 0
    for c_ in C:
        if sum(c_) == x:
            cnt += 1
    print(cnt)


while True:
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        break
    solve(n, x)
