"""
[스택 - 세 종류 괄호 짝 맞추기]

문제 설명:
- 스택(Stack)을 사용하여 세 종류의 괄호 '()', '[]', '{}' 가 올바르게 짝지어져 있는지 확인합니다.
- 12번 문제(소괄호만)의 확장입니다. 이번에는 "종류까지" 맞아야 합니다.
- 올바른 괄호 문자열의 조건:
  1. 모든 여는 괄호는 같은 종류의 닫는 괄호로 닫혀야 합니다.
  2. 괄호는 열린 순서의 역순으로 닫혀야 합니다. 예) "([)]" 는 잘못된 괄호.

입력:
- s: 괄호 문자만으로 이루어진 문자열 (빈 문자열일 수 있음)

출력:
- True: 올바른 괄호
- False: 잘못된 괄호

예제:
입력: "([{}])"
출력: True

입력: "([)]"
출력: False

입력: ""
출력: True

힌트:
- 여는 괄호는 스택에 push
- 닫는 괄호를 만나면: 스택이 비어 있거나, 스택의 맨 위가 짝이 맞는 여는 괄호가 아니면 False
- 짝이 맞으면 pop
- 마지막에 스택이 비어 있으면 True
- 딕셔너리로 {닫는 괄호: 여는 괄호} 짝을 미리 정해 두면 편합니다
"""


def is_valid_brackets(s):
    """
    세 종류 괄호의 짝이 맞는지 확인

    Args:
        s: 괄호 문자열

    Returns:
        올바른 괄호면 True, 아니면 False
    """
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for i in s:
        if i == "(" or i == "[" or i == "{":
            stack.append(i)
        elif i == ")" or i == "]" or i == "}":
            if stack == [] or mapping.get(i) not in mapping.values():
                return False
            else:
                stack.pop()
    if stack == []:
        return True


# 테스트 케이스
if __name__ == "__main__":
    tests = ["()[]{}", "([{}])", "(]", "([)]", "{[", "", "]"]
    for i, s in enumerate(tests, 1):
        print(f"=== 테스트 케이스 {i} ===")
        print(f'입력: "{s}"')
        print(f"결과: {is_valid_brackets(s)}")
        print()
