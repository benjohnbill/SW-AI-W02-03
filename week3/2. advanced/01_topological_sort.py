"""
[위상 정렬 - Topological Sort]

문제 설명:
- 방향 그래프에서 순서를 정합니다.
- 선행 작업이 먼저 오도록 정렬합니다.
- 예: 과목 선수과목, 작업 순서

입력:
- graph: 방향 그래프
- vertices: 정점 개수

출력:
- 위상 정렬 순서

예제:
과목:
0(기초) → 1(중급) → 3(고급)
0(기초) → 2(응용)

위상 정렬: [0, 1, 2, 3] 또는 [0, 2, 1, 3]

힌트:
- 진입 차수(in-degree) 사용
- 진입 차수가 0인 정점부터 시작
- 큐 사용
"""

from collections import deque


def topological_sort(vertices, edges):

    # 1. 진입차수 초기화

    all_nodes = set()
    for start, end in edges:
        all_nodes.add(start)
        all_nodes.add(end)
    in_degree = {key: 0 for key in all_nodes}  # 모든 노드를 {key : 0} 형태로
    result = []

    # 2. 그래프 구성 및 진입 차수 계산
    for start, end in edges:
        in_degree[end] += 1

    # 3. 진입 차수가 0인 정점들을 큐에 추가
    que = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            que.append(key)

    # 4. [Main](반복) : 큐에서 정점 꺼내기 & 해당 노드와 관련된 진입차수 감소
    while que:
        temp = que.popleft()
        result.append(temp)
        for start, end in edges:
            if temp == start:
                in_degree[end] -= 1
                if (
                    in_degree[end] == 0
                ):  # 윗줄로 들여쓰기를 하면, 이전에 깎은 놈들도 que에 추가됌
                    que.append(end)
    return result


# 테스트 케이스
if __name__ == "__main__":
    # 과목 선수과목 예제
    vertices = 4
    edges = [
        (0, 1),  # 0 → 1
        (0, 2),  # 0 → 2
        (1, 3),  # 1 → 3
    ]

    print("=== 위상 정렬 ===")
    print("과목 관계:")
    print("  0(기초) → 1(중급) → 3(고급)")
    print("  0(기초) → 2(응용)")
    print()

    result = topological_sort(vertices, edges)
    print(f"수강 순서: {result}")

# ===========================
# list를 쓰던 시절의 로직(node가 0, 1, 2, 3의 순서라 )

# ============================================================
# graph / in_degree를 dict()로 처리 - range(vertices) 때문에 0, 2, 8.. 이런거 커버 X
# ============================================================

# # 1. 그래프 초기화 및 구성 & 진입차수 초기화
# graph = {node: [] for node in range(vertices)}
# for key, value in edges:
#     graph[key].append(value)

# in_degree = {key: 0 for key in graph}
# result = []
