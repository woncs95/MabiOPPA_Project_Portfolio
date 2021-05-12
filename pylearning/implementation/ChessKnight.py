input_data=input()
row=int(input_data[1])
column=int(ord(input_data[0]))-int(ord('a'))+1 ##유니코드 오더 위치

#나이트가 이동하는 8가지방향
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,-2),(-2,1)]

#8방향 이동가능?
result=0
for step in steps:
    next_row=row+step[0]
    next_column=column+step[1]
    #되면 카운트 증가
    if 0<next_row <9 and  0<next_column<9:
        result +=1
    else: continue
print(result)