def timeCount():
    N=int(input())
    hour=str(range(N + 1))
    h=hour.count('3')
    m=15
    s=m
    print(h+N*m+N*s)

timeCount()

