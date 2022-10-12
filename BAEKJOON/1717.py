import  sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
parents = [i for i in range(n+1)]

def find(n) :
    if parents[n] != n :
        parents[n] = find(parents[n])
    return parents[n]

def union(x,y) :
    x = find(x)
    y = find(y)

    if x < y :
        parents[y] = x
    else :
        parents[x] = y

for _ in range(m) :
    a,b,c = map(int, input().split())

    if a == 0 :
        union(b,c)

    else :
        # b와 c가 같은 집합에 포함되어 있을 때
        if find(b) == find(c) :
            print("YES")
        else :
            print("NO")