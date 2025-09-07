
'''
DGA란 그래프 여결 방향이 있고 한 곳에서 순환이 발생하지 않는 그래프를 의미합니다.

Edge Relaxtion 개념
가중치가 있는 그래프에서 각 edge에 배정되어 있는 만큼의 가중치를 더해가며 탐색할 때
더 나은 (작은) 경로의 가중치가 있다면 그 값으로 업데이트하는 것을 뜻한다.


'''


'''
문제 정의
n개의 노드와 m개의 간선을 가진 방향 비순환 그래프 DAG가 있습니다.

1. 각 노드는 파란색 혹은 빨간색입니다.
2. 각 쿼리에 대해 노드를 빨간색으로 바꾸거나 현재 상태에서 cry가 이길 수 있는지 판별합니다.
3. 전체 쿼리 수와 노드 수, 간선 수가 많으므로 효율적으로 처리해야하며, 동적 프로그래밍(DP)
+ 위상정렬로 각 노드별 cry별 최적으로 시작해서 승리 할 수 있는지를 관리합니다.
-> 빨간색이 되면 해당 노드 값을 즉시 업데이트 합니다.

'''

#위상정렬이란?
#순서가 정해져 있는 작업을 차례로 수행할 때 그 순서를 결정해주기 위해 사용하는 알고리즘

import sys #입출력
import threading #멀티스레딩

def main():
    import sys
    sys.setrecursionlimit(1 << 25) #재귀 깊이 제한을 크게 설정을 한다. 
    T = int(sys.stdin.readline())
    for _ in range(T):
        n, m, q = map(int, sys.stdin.readline().split()) #노드, 간선, 쿼리 입력받음
        G = [[] for _ in range(n)] #인접 리스트 방식의 그래프 저장공간
        in_deg = [0]*n #각 노드의 진입차수를 저장하는 리스트
        for _ in range(m):
            u, v = map(int, sys.stdin.readline().split())
            u -= 1
            v -= 1
            G[u].append(v)
            in_deg[v] += 1
        
        is_red = [False]*n

        # 위상 정렬
        from collections import deque
        order = []
        dq = deque()
        for i in range(n):
            if in_deg[i] == 0:
                dq.append(i)
        while dq:
            x = dq.popleft()
            order.append(x)
            for y in G[x]:
                in_deg[y] -= 1
                if in_deg[y] == 0:
                    dq.append(y)
        
        # 답 memoization: 0=River win, 1=Cry win
        win = [0]*n
        # 리프 노드 판별
        out_deg = [len(G[i]) for i in range(n)]
        for x in reversed(order): #위상정렬 순서를 역순으로 돌면서 DP를 계산한다.
            if is_red[x]:
                win[x] = 0  # 빨간색이면 River win
            elif out_deg[x] == 0:
                win[x] = 1  # 출구 없음 -> Cry win
            else:
                can_cry_win = False
                for y in G[x]:
                    if win[y] == 0:
                        can_cry_win = True
                win[x] = 1 if can_cry_win else 0

        for _ in range(q):
            parts = sys.stdin.readline().split()
            typ, u = int(parts[0]), int(parts[1]) - 1
            if typ == 1:
                is_red[u] = True
                # 해당 노드가 빨간색이 되었다면, 위상정렬 역순으로 영향 반영
                for x in reversed(order):
                    if is_red[x]:
                        win[x] = 0
                    elif out_deg[x] == 0:
                        win[x] = 1
                    else:
                        can_cry_win = False
                        for y in G[x]:
                            if win[y] == 0:
                                can_cry_win = True
                        win[x] = 1 if can_cry_win else 0
            else:
                print('YES' if win[u] else 'NO')

threading.Thread(target=main).start()

