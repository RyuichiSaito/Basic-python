class Cube:
    def __init__(self, ls) -> None:
        self.top = ls[0]
        self.front = ls[1]
        self.right = ls[2]
        self.left = ls[3]
        self.back = ls[4]
        self.bottom = ls[5]
    
    def rot_S(self):
        self.top, self.front, self.bottom, self.back = self.back, self.top, self.front, self.bottom
    
    def rot_N(self):
        self.top, self.front, self.bottom, self.back = self.front, self.bottom, self.back, self.top
    
    def rot_W(self):
        self.top, self.right, self.bottom, self.left = self.right, self.bottom, self.left, self.top
    
    def rot_E(self):
        self.top, self.left, self.bottom, self.right = self.left, self.bottom, self.right, self.top

    def rotate(self, coms):
        for com in coms:
            if com == "S":
                self.rot_S()
            elif com == "N":
                self.rot_N()
            elif com == "E":
                self.rot_E()
            elif com == "W":
                self.rot_W()
    
    def stasus(self):
        return [self.top, self.front, self.right, self.left, self.back, self.bottom]


def LI(): return list(map(int, input().split()))

A = LI()
B = LI()

for com in ['', 'N', 'W', 'E', 'S', 'NN']:
    cube = Cube(A)
    cube.rotate(com)
    for _ in range(4):
        cube.rotate('NES')
        A_cur = cube.stasus()
        if A_cur == B:
            print("Yes")
            exit()
print("No")