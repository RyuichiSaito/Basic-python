while True:
    a,op,b = map(str, input().split())
    if op == '?':
        break
    print(int(eval(a+op+b)))