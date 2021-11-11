
def repeatedString(s, n): #block caculation
    a1=s.count('a')
    how_many_blocks=n//len(s)
    block_len=(n//len(s))*len(s)
    last_block = s[0:n-block_len] ##n-block_len 바로 전까지임
    print(n-block_len)
    print(last_block)
    if n%len(s)==0:
        result=a1*how_many_blocks
    else:
        a2 = last_block.count('a')
        result = a1 * how_many_blocks + a2


def hourglassSum(arr): #sun of all hourglasses
    lst=[]
    for i in range(2, 6):
        for j in range(2,6):
            sub = [arr[i - 2][j - 2], arr[i - 2][j - 1], arr[i - 2][j]
                , arr[i - 1][j - 1],
                   arr[i][j - 2], arr[i][j - 1], arr[i][j]]
            s = sum(sub)
            lst.append(s)
            print(lst)
        else:
            pass
    return max(lst)

arr=[[-1, 1, -1, 0, 0 ,0],
[0 ,-1 ,0, 0, 0, 0],
[-1 ,-1, -1, 0 ,0, 0],
[0 ,-9 ,2, -4, -4, 0],
[-7, 0, 0 ,-2, 0 ,0],
[0,0 ,-1 ,-2, -4, 0]]
hourglassSum(arr)

def rotLeft(a, d): ##rotate left
    i=0
    while i<d:
        a.append(a[0])
        a.pop(0)
        i+=1
    return a

def sockMerchant(n, ar):
    c=0
    ars=set(ar)
    for i in ars :
        c=c+ar.count(i)//2
    return c


def countingValleys(steps, path):
    lst = list(path)
    lvl = 0
    vc = 0

    for el in lst:
        prev_lvl = lvl
        if el == 'U':
            lvl += 1
        if el == 'D':
            lvl -= 1
        if lvl < 0 and prev_lvl >= 0:
            vc += 1
        else:
            continue
    return vc

def jumpingOnClouds(c):
    goal_index = len(c) - 1
    check_value = 0
    answer = 0
    while(check_value < goal_index):
        if check_value + 2 <= goal_index and c[check_value + 2] == 0:
            check_value += 2
            answer += 1
        elif c[check_value + 1] == 0:
            check_value += 1
            answer += 1
    return answer

