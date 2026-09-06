"""
[DFS - 깊이 우선 탐색 (Depth-First Search)]

문제 설명:
- DFS로 그래프를 탐색합니다.
- 깊이 방향으로 끝까지 탐색합니다.
- 재귀 또는 스택을 사용합니다.

입력:
- graph: 그래프 (인접 리스트)
- current: 시작 정점

출력:
- 방문 순서

예제:
그래프:
  0 ─── 1
  │     │
  └─ 2 ─┘
      │
      3

시작: 0
DFS: [0, 1, 2, 3] (순서는 구현에 따라 다를 수 있음)


"""


def dfs(graph, current, v=None):
    """
    깊이 우선 탐색 (재귀)

    Args:
        graph: 그래프 딕셔너리
        current: 현재 정점
        visited: 방문 리스트

    Returns:
        방문 순서 리스트
    """
    v = []

    def dfs_logic(graph, current, v):
        v.append(current)
        for num in graph[current]:
            if num not in v:
                dfs_logic(graph, num, v)

    dfs_logic(graph, current, v)
    return v


# 테스트 케이스
if __name__ == "__main__":
    # 그래프 생성
    graph = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2]}

    print("=== DFS (깊이 우선 탐색) ===")
    result = dfs(graph, 0)
    print("시작 정점: 0")
    print(f"방문 순서: {result}")

# ===== 대조용: 풀기 전 열람 금지 =====
#
# 힌트:
# - 재귀로 구현
# - 방문 체크 필요
# - 깊이 우선으로 방문
