house = [[[0 for _ in range(10)] for _ in range(3)] for _ in range(4)]
for _ in range(int(input())):
    t, x, y, n = map(lambda x:int(x)-1, input().split())
    house[t][x][y] += (n+1)

for i in range(4):
    for j in range(3):
        out = ""
        for k in range(10):
            out += " " + str(house[i][j][k])
        print(out)
    if i == 3:
        break
    print("####################")