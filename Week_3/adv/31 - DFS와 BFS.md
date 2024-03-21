# [Silver II] DFS와 BFS - 1260 

[문제 링크](https://www.acmicpc.net/problem/1260) 

### 성능 요약

메모리: 32236 KB, 시간: 436 ms

### 분류

그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

### 제출 일자

2023년 10월 16일 20:39:52

### 문제 설명

<p>그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.</p>

### 입력 

 <p>첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.</p>

### 출력 

 <p>첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.</p>

### 예제 입력 

5 5 3
5 4
5 2
1 2
3 4
3 1

### 예제 출력 

3 1 2 5 4
3 1 4 2 5


### 답안
```python
def dfs(c) :
    ans_dfs.append(c)        # 방문 노드 추가
    v[c] = 1                # 방문 표시
    
    for n in adj[c] :
        if not v[n] :        # 방문하지 않은 노드인 경우
            dfs(n)
def bfs(s) :
    q = []                    # 필요한 q, v[], 변수 생성
    
    q.append(s)                # q에 초기데이터(들) 삽입
    ans_bfs.append(s)
    v[s] = 1
    
    while q :
        c = q.pop(0)
        for n in adj[c] :
            if not v[n] :        # 방문하지 않은 노드 => q 삽입
                q.append(n)
                ans_bfs.append(n)
                v[n] = 1
                
                
N, M, V = map(int, input().split())
adj = [[] for _ in range(N + 1)]
for _ in range(M) :
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)        # 양방향
    
# [1] 오름차순 정렬
for i in range(1, N + 1) :
    adj[i].sort()
    
v = [0] * (N + 1)
ans_dfs = []
dfs(V)

v = [0] * (N + 1)
ans_bfs = []
bfs(V)

print(*ans_dfs)
print(*ans_bfs)
```

### 풀이

1. 인접리스트 adj를 생성
2. 