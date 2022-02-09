while True:
    s = input()
    if s == '0':
        break
    ans = 0
    for i in range(len(s)):
        ans += int(s[i])
    print(ans)