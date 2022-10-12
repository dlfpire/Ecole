import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
visited = [False]*(V+1)
#방문여부를 알기 위해서 V+1만큼의 배열 만들기
Elist = [[] for _ in range(V+1)]
#간선 저장
heap = [[0, 1]]
#힙 생성
for _ in range(E):
    A, B, C = map(int, input().split())
    Elist[A].append([C, B])
    Elist[B].append([C, A])

answer = 0
cnt = 0
while heap:
    if cnt == V:
        break
    C, A = heapq.heappop(heap)
    #가장 작은 원소 삭제
    print(C, A)
    if not visited[A]:
        visited[A] = True
        answer += C
        cnt += 1
        for i in Elist[A]:
            heapq.heappush(heap, i)

print(answer)