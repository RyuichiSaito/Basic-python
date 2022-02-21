while True:
    s = input()
    if s == '0':
        break
    ans = 0
    for sd in s:
        ans += int(sd)
    print(ans)
