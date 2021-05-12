
#동북서남
dx=[0,-1,0,1]
dy=[1,0,-1,0]

#현위치
x,y=2,2

for i in range(4):
    nx=x+dx[i] #바뀐x위치
    ny=y+dy[i] #바뀐y위치
    
    print(nx,ny)