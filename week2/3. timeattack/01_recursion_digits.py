"""
[재귀 함수 - 자릿수의 합과 거듭제곱]

문제 설명:
- 재귀 함수를 사용하여 (1) 정수의 각 자릿수의 합, (2) 거듭제곱을 계산합니다.
- 반복문(for, while)과 내장 함수(sum, str, pow, ** 연산자)는 사용하지 않습니다.
- 두 함수 모두 base case와 recursive case로만 구성해야 합니다.

입력:
- sum_of_digits(n): n은 0 이상의 정수
- power(base, exp): base는 정수, exp는 0 이상의 정수

출력:
- sum_of_digits: n의 각 자릿수를 모두 더한 값
- power: base의 exp 제곱

예제:
입력: n = 12345
출력: 15 (1 + 2 + 3 + 4 + 5)

입력: base = 2, exp = 10
출력: 1024

힌트:
- 자릿수의 합: 12345 = (12345 % 10) + (1234의 자릿수 합). 한 자리 수가 되면 멈춥니다.
- 거듭제곱: base^exp = base × base^(exp-1), base^0 = 1
"""


def sum_of_digits(n):
    """
    재귀를 사용한 자릿수의 합 계산

    Args:
        n: 0 이상의 정수

    Returns:
        n의 각 자릿수의 합
    """
    if n < 10:
        return n
    return sum_of_digits(n // 10) + n % 10


def power(base, exp):
    """
    재귀를 사용한 거듭제곱 계산

    Args:
        base: 밑 (정수)
        exp: 지수 (0 이상의 정수)

    Returns:
        base의 exp 제곱
    """
    if exp == 0:
        return 1
    return base * power(base, exp - 1)


# 테스트 케이스
if __name__ == "__main__":
    print("=== 자릿수의 합 ===")
    for n in [12345, 0, 9, 1000, 98765]:
        print(f"sum_of_digits({n}) = {sum_of_digits(n)}")
    print()

    print("=== 거듭제곱 ===")
    for base, exp in [(2, 10), (5, 0), (3, 4), (7, 1), (10, 3)]:
        print(f"power({base}, {exp}) = {power(base, exp)}")
