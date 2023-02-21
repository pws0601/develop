'''전역변수와 지역변수'''

def DFS1():
    cnt=3
    print(cnt)

def DFS2():
    if cnt==5:
        print(cnt)


if __name__=="__main__":
    cnt=5
    DFS1()
    DFS2()
    print(cnt)