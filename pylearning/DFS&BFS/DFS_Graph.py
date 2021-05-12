
import re

def dfs(graph,v,visited):
    visited[v]=True
    print(v,end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)





'''def decodeMessage(buffer, packages):
    for b in packages:
        for i in range(len(b)):
            if i == len(b) - i:
                a[i] = b[i]
            elif i != len(b) - i:
                a[i] = b[i] + b[len(b) - i]
            char[i] = re.sub(r"[^a-zA-Z0-9]", "", chr(a[i]))  ##without nonletter&unlock
            lst.append(char[i])'''


def decodeMessage(buffer, packages):
    a = []
    char = []
    lst = []
    new_a = []
    for b in packages:
        for i in range(len(b)):
            if i == len(b)-i:
                a[i]=b[i]
            elif i != len(b)-i:
                a[i]=b[i]+b[len(b)-i]
            char[i]=re.sub(r"[^a-zA-Z0-9]","",chr(a[i]))##without nonletter&unlock
            new_a.append(list(map(ord,char)))
            lst+=new_a
        ##search repeated from lst
    for j in range(2,len(lst)):
        if lst[j-2]==lst[j-1]==lst[j]:
            pass
        else: continue
t='ab'
print(t[0])