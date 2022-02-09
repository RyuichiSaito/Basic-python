while True:
    li = list(map(int, input().split()))
    if li == [0, 0]:
        break
    print(*sorted(li))
