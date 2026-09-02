"""
[정렬 - 선택 정렬(Selection Sort) 구현]

문제 설명:
- 선택 정렬은 "아직 정렬되지 않은 부분에서 가장 작은 값을 찾아, 맨 앞과 교환"을
  반복하는 O(n²) 정렬입니다. 버블 정렬(08번)과 같은 급의 기본 정렬입니다.
- 진행 과정 (i 번째 단계):
  1. 인덱스 i 부터 끝까지 중에서 가장 작은 값의 인덱스(min_idx)를 찾습니다.
  2. arr[i] 와 arr[min_idx] 를 교환합니다.
  3. i 를 1 늘려 반복합니다. 마지막 원소는 자동으로 제자리이므로 n-1 단계면 충분합니다.
- 내장 정렬(sorted, list.sort)과 min 함수는 사용하지 않습니다.

입력:
- arr: 정수 리스트 (빈 리스트일 수 있음)

출력:
- 오름차순으로 정렬된 리스트 (같은 리스트를 정렬해서 반환)

예제:
입력: [64, 25, 12, 22, 11]
출력: [11, 12, 22, 25, 64]

진행 과정:
  [64, 25, 12, 22, 11]  → 최솟값 11 을 인덱스 0 과 교환
  [11, 25, 12, 22, 64]  → 최솟값 12 를 인덱스 1 과 교환
  [11, 12, 25, 22, 64]  → 최솟값 22 를 인덱스 2 와 교환
  [11, 12, 22, 25, 64]  → 최솟값 25 는 이미 제자리
  [11, 12, 22, 25, 64]

힌트:
- 바깥 반복문: i 를 0 부터 n-2 까지
- 안쪽 반복문: j 를 i+1 부터 n-1 까지 돌며 arr[j] < arr[min_idx] 이면 min_idx 갱신
- 교환: arr[i], arr[min_idx] = arr[min_idx], arr[i]
"""

def selection_sort(arr):
    """
    선택 정렬 구현

    Args:
        arr: 정렬할 리스트

    Returns:
        오름차순으로 정렬된 리스트
    """
    n = len(arr)

    for i in range(0, n-2)
        min_idx = arr[i]
        for j in range(i+1, n-1) :
            if arr[j-1] < arr[j] :
                arr[j] = min_idx
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 테스트 케이스
if __name__ == "__main__":
    tests = [
        [64, 25, 12, 22, 11],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [3, 3, 1, 2, 1],
        [42],
        [],
    ]
    for i, arr in enumerate(tests, 1):
        print(f"=== 테스트 케이스 {i} ===")
        print(f"정렬 전: {arr}")
        print(f"정렬 후: {selection_sort(arr)}")
        print()
