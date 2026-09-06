"""
[퀵 정렬 구현]

문제 설명:
- 퀵 정렬(Quick Sort) 알고리즘을 구현합니다.
- 분할 정복(Divide and Conquer) 방식을 사용합니다.
- 피벗(pivot)을 기준으로 작은 값과 큰 값을 분할하여 재귀적으로 정렬합니다.

입력:
- arr: 정렬되지 않은 정수 배열

출력:
- 오름차순으로 정렬된 배열

예제:
입력: [10, 7, 8, 9, 1, 5]
출력: [1, 5, 7, 8, 9, 10]

힌트:
- 피벗 선택 (일반적으로 마지막 원소)
- 피벗보다 작은 원소는 왼쪽, 큰 원소는 오른쪽으로 분할
- 재귀적으로 왼쪽과 오른쪽 부분 정렬
"""


def quick_sort(arr):
    start = 0
    end = len(arr) - 1

    def quick_sort_helper(arr, start, end):
        while start < end:
            n = (start + end) // 2
            if arr[start] > arr[n]:
                arr[start], arr[n] = arr[n], arr[start]
            if arr[start] > arr[end]:
                arr[start], arr[end] = arr[end], arr[start]
            if arr[n] > arr[end]:
                arr[n], arr[end] = arr[end], arr[n]
            # start, n(중앙 인덱스), end를 최소값 - 중앙값 - 최댓값으로 정렬

            i = start - 1
            j = end + 1
            pivot = arr[n]
            while True:
                i += 1
                j -= 1
                while arr[i] < pivot:
                    i += 1
                while arr[j] > pivot:
                    j -= 1
                if i >= j:
                    break
                arr[i], arr[j] = arr[j], arr[i]
            if (j - start + 1) >= end - j:
                # 왼쪽 부분이(start, j)이 오른쪽(j + 1, end)보다 더 크면
                quick_sort_helper(arr, j + 1, end)  # 오른쪽(작은 쪽)만 재귀
                end = j  # (j + 1, end)까지 다 정렬되었다고 생각하고, while 반복으로 다시 다룰 end 값을 피벗 인덱스로 -> 부모 함수의 범위값 조정

            else:  # 오른쪽 부분(j + 1, end)이 왼쪽(start, j)보다 더 크면
                quick_sort_helper(arr, start, j)  # 왼쪽(작은 쪽)만 재귀
                start = j + 1  # 다음 반복의 end 값을 피벗 인덱스로

            # 재귀를 양쪽으로 도는 게 아니라, 한 쪽만 돌리고 싶어서

    quick_sort_helper(arr, start, end)
    return arr


# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    arr1 = [10, 7, 8, 9, 1, 5]
    print("=== 테스트 케이스 1 ===")
    print(f"정렬 전: {arr1}")
    result1 = quick_sort(arr1.copy())
    print(f"정렬 후: {result1}")
    print()

    # 테스트 케이스 2
    arr2 = [64, 34, 25, 12, 22, 11, 90]
    print("=== 테스트 케이스 2 ===")
    print(f"정렬 전: {arr2}")
    result2 = quick_sort(arr2.copy())
    print(f"정렬 후: {result2}")
    print()

    # 테스트 케이스 3: 중복 원소
    arr3 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print("=== 테스트 케이스 3: 중복 원소 ===")
    print(f"정렬 전: {arr3}")
    result3 = quick_sort(arr3.copy())
    print(f"정렬 후: {result3}")
    print()

    # 테스트 케이스 4: 이미 정렬된 배열
    arr4 = [1, 2, 3, 4, 5]
    print("=== 테스트 케이스 4: 이미 정렬됨 ===")
    print(f"정렬 전: {arr4}")
    result4 = quick_sort(arr4.copy())
    print(f"정렬 후: {result4}")
    print("이미 정렬된 경우 O(n²) 시간 소요 (최악의 경우)")
