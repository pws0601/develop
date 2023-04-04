import turtle as t
import random as r
import time

class Brick():
    def __init__(self):
        self.y=0
        self.x=6
        self.color=r.randint(1,6)

def draw_grid(block, grid):
    block.clear()
    top=250
    left=-150
    colors=['black','red','blue','orange','yellow','green','purple','white']
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            sc_x=left+(x*22)
            sc_y=top-(y*22)
            block.goto(sc_x, sc_y)
            block.color(colors[grid[y][x]])
            block.stamp()

if __name__=="__main__":
    sc = t.Screen()
    sc.tracer(False)
    sc.bgcolor("black")
    sc.setup(width=600, height=700)
    #게임판 초기화
    grid = [[0]*12 for _ in range(24)]

    #게임판 벽 초기화
    for i in range(24):
        grid[i].insert(0, 7)
        grid[i].append(7)
    grid.append([7]*14)
    # 맨 아래 3줄 랜덤으로 블록 채우기
    for y in range(23, 20, -1):
        for x in range(1, 13):
            grid[y][x]=r.randint(1,6)

    block=t.Turtle()
    block.penup()
    block.speed(0)
    block.shape("square")
    block.color("red")
    block.setundobuffer(None)

    brick = Brick()
    grid[brick.y][brick.x] = brick.color
    draw_grid(block, grid)

    while True:
        sc.update()
        if grid[brick.y+1][brick.x]==0:
            grid[brick.y][brick.x]=0
            brick.y+=1
            grid[brick.y][brick.x]=brick.color
        for x in grid:
            print(x)
        print()
        draw_grid(block, grid)
        time.sleep(0.5)


    


    for x in grid:
        print(x)

    



    sc.mainloop()