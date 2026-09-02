"""
[재귀 함수 - 문자열 뒤집기와 리스트 원소의 합]

문제 설명:
- 재귀 함수를 사용하여 (1) 문자열을 뒤집고, (2) 리스트 원소의 합을 구합니다.
- 반복문(for, while)과 내장 함수(reversed, sum, [::-1] 슬라이스)는 사용하지 않습니다.
- 두 함수 모두 base case와 recursive case로만 구성해야 합니다.

입력:
- reverse_string(s): 문자열 (빈 문자열일 수 있음)
- list_sum(lst): 정수 리스트 (빈 리스트일 수 있음)

출력:
- reverse_string: s를 뒤집은 문자열
- list_sum: 리스트의 모든 원소를 더한 값

예제:
입력: s = "hello"
출력: "olleh"

입력: lst = [1, 2, 3, 4, 5]
출력: 15

힌트:
- 문자열 뒤집기: "hello" 뒤집기 = "ello" 뒤집기 + "h". 길이가 1 이하이면 그대로 반환.
- 리스트 합: [1,2,3] 의 합 = 1 + [2,3] 의 합. 빈 리스트의 합은 0.
- 첫 글자(원소)를 떼어 내는 데 s[0] 과 s[1:] 를 사용할 수 있습니다.
"""


def reverse_string(s):
    """
    재귀를 사용한 문자열 뒤집기

    Args:
        s: 뒤집을 문자열

    Returns:
        뒤집힌 문자열
    """
    if s == "":
        return ""
    return reverse_string(s - s[0]) + s[0]


def list_sum(lst):
    """
    재귀를 사용한 리스트 원소의 합

    Args:
        lst: 정수 리스트

    Returns:
        모든 원소의 합
    """
    if list_sum == []:
        return 0
    a = list_sum.pop()
    return list_sum(lst) + a


# 테스트 케이스
if __name__ == "__main__":
    print("=== 문자열 뒤집기 ===")
    for s in ["hello", "a", "", "racecar", "Python 3"]:
        print(f'reverse_string("{s}") = "{reverse_string(s)}"')
    print()

    print("=== 리스트 원소의 합 ===")
    for lst in [[1, 2, 3, 4, 5], [], [10], [-3, 7, -4], [100, 200, 300]]:
        print(f"list_sum({lst}) = {list_sum(lst)}")
