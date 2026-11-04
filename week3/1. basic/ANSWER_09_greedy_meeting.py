"""
[그리디 - 회의실 배정 — 대조용 정답본 / 채점 대상 아님]

문제 설명:
- 하나의 회의실에 여러 회의를 배정합니다.
- 각 회의는 시작 시간과 종료 시간이 있습니다.
- 최대한 많은 회의를 배정하려고 합니다.

입력:
- meetings: [(시작, 종료), ...] 회의 리스트

출력:
- (배정된 회의 개수, 선택된 회의 리스트)

예제:
입력: [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
출력: 4개
선택: [(1, 4), (5, 7), (8, 11), (12, 14)]

핵심 아이디어:
- 종료 시간이 이른 회의부터 고르면, 남는 시간이 가장 길어진다.
- 남는 시간이 가장 길다는 것은, 뒤에 이어붙일 수 있는 회의의 후보가
  다른 어떤 선택보다 넓다는 뜻이므로, 이 선택이 손해를 볼 수 없다.
  (교환 논증: 최적해의 첫 회의를 '종료가 가장 이른 회의'로 바꿔치기해도
   회의 개수는 줄지 않는다. 이를 반복 적용하면 그리디 해가 최적해가 된다.)
"""

def select_meetings(meetings):
    """
    회의실 배정 (그리디)

    Args:
        meetings: [(시작, 종료)] 리스트

    Returns:
        (배정된 회의 개수, 선택된 회의 리스트)
    """
    # 회의가 없으면 빈 결과를 그대로 돌려준다.
    if not meetings:
        return 0, []

    # 종료 시간 오름차순 정렬. 종료가 같으면 시작이 이른 쪽을 앞에 둔다.
    # (개수에는 영향이 없지만, 선택 결과를 항상 같게 만들어 준다.)
    sorted_meetings = sorted(meetings, key=lambda m: (m[1], m[0]))

    selected = []

    # 첫 회의는 무조건 선택한다. 종료가 가장 이르므로 손해가 없다.
    selected.append(sorted_meetings[0])
    last_end = sorted_meetings[0][1]

    # 나머지 회의는 '직전 회의가 끝난 뒤에 시작하는가'만 확인한다.
    for start, end in sorted_meetings[1:]:
        if start >= last_end:
            selected.append((start, end))
            last_end = end

    return len(selected), selected


# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    meetings1 = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9)]
    count1, selected1 = select_meetings(meetings1)
    print("=== 테스트 케이스 1 ===")
    print(f"전체 회의: {meetings1}")
    print(f"배정된 회의 개수: {count1}개")
    print(f"선택된 회의: {selected1}")
    print()

    # 테스트 케이스 2
    meetings2 = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
    count2, selected2 = select_meetings(meetings2)
    print("=== 테스트 케이스 2 ===")
    print(f"전체 회의: {len(meetings2)}개")
    print(f"배정된 회의 개수: {count2}개")
    print(f"선택된 회의: {selected2}")
