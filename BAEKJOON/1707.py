from collections import deque
import sys

input = sys.stdin.readline


def bfs(v):
    q = deque()
    # 양방향 큐
    q.append(v)
    # append : 오른쪽 끝에 항목 추가
    visited[v] = 1

    while q:
        n = q.popleft()
        # popleft : 왼쪽에서 값 빼기 (순서)
        for i in graph[n]:
            if visited[i] == 0:
                # 방문한 적이 없으면
                q.append(i)
                visited[i] = -visited[n]
                # 다른 색 칠하기

            elif visited[i] == visited[n]:
                # 가봤는데 색이 같다면
                return False
    return True


k = int(input())
# input은 입력된 값을 문자열로 인식해서 int로 숫자로 변환

for _ in range(k):
    # for _ in range : 인덱스가 필요하지 않을 때 사용
    v, e = map(int, input().split())
    # input().split() : 띄어쓰기 기준으로 2개 이상의 입력값을 구분하기 위해
    # map(적용할 함수, 반복 가능한 자료형)
    graph = [[] for _ in range(v + 1)]
    visited = [0] * (v + 1)
    # 정점의 개수 v+1 만큼
    result = True

    for _ in range(e):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    for i in range(1, v + 1):
        if visited[i] == 0:
            if not bfs(i):
                result = False
                break

    print("YES" if result else "NO")
