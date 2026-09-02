"""
[재귀 + 이분 탐색 - 재귀로 구현하는 이분 탐색]

문제 설명:
- 정렬된 배열에서 특정 값을 찾는 이분 탐색을 "재귀 함수"로 구현합니다.
- while 반복문 대신, 탐색 범위(left, right)를 절반으로 줄여 자기 자신을 다시 호출합니다.
- 분할 정복(11번 문제)처럼 left, right 인덱스를 인자로 넘기는 형태입니다.

입력:
- arr: 정렬된 정수 배열
- target: 찾고자 하는 값
- left: 탐색 범위의 시작 인덱스
- right: 탐색 범위의 끝 인덱스

출력:
- target이 있는 인덱스 (없으면 -1)

예제:
입력: arr = [1, 3, 5, 7, 9, 11, 13], target = 7, left = 0, right = 6
출력: 3

입력: arr = [1, 3, 5, 7, 9], target = 6, left = 0, right = 4
출력: -1

힌트:
- Base case 1: left > right이면 범위가 비었으므로 -1 반환
- Base case 2: arr[mid] == target이면 mid 반환
- Recursive case: target이 arr[mid]보다 크면 오른쪽 절반(mid+1 ~ right),
  작으면 왼쪽 절반(left ~ mid-1)으로 재귀 호출
"""

def binary_search_recursive(arr, target, left, right):
    """
    재귀를 사용한 이분 탐색

    Args:
        arr: 정렬된 배열
        target: 찾을 값
        left: 시작 인덱스
        right: 끝 인덱스

    Returns:
        target의 인덱스 (없으면 -1)
    """
    # TODO: base case - 탐색 범위가 비어 있으면(left > right) -1 반환

    # TODO: 중간 인덱스 계산

    # TODO: arr[mid]가 target과 같으면 mid 반환

    # TODO: target이 더 크면 오른쪽 절반으로 재귀 호출

    # TODO: target이 더 작으면 왼쪽 절반으로 재귀 호출
    pass

# 테스트 케이스
if __name__ == "__main__":
    tests = [
        ([1, 3, 5, 7, 9, 11, 13], 7),
        ([2, 4, 6, 8, 10, 12, 14, 16, 18, 20], 14),
        ([1, 3, 5, 7, 9], 6),
        ([1, 3, 5, 7, 9], 1),
        ([10], 10),
    ]
    for i, (arr, target) in enumerate(tests, 1):
        result = binary_search_recursive(arr, target, 0, len(arr) - 1)
        print(f"=== 테스트 케이스 {i} ===")
        print(f"배열: {arr}")
        print(f"찾는 값: {target}")
        print(f"결과: 인덱스 {result}")
        print()
