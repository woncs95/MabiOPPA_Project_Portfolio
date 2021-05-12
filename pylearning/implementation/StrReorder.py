data=input()
result=[]
value=0

#문자확인
for x in data:
    #알파벳이면 리스트에 삽입
    if x.isalpha():
        result.append(x)
    else:
        value+=int(x)

result.sort()

if value!=0:
    result.append(str(value))
    
print(''.join(result))