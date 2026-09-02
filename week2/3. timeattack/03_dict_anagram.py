"""
[문자열 + 딕셔너리 - 애너그램(Anagram) 판별]

문제 설명:
- 두 문자열이 애너그램인지 판별합니다.
- 애너그램이란 글자의 순서만 바꿔서 서로 만들 수 있는 문자열입니다.
  예) "listen"과 "silent"
- 대소문자는 구분하지 않고, 공백은 무시합니다.
- 각 글자가 몇 번 나오는지 딕셔너리로 세어서 비교하세요.

입력:
- s, t: 비교할 두 문자열 (알파벳과 공백으로만 구성)

출력:
- True: 애너그램인 경우
- False: 애너그램이 아닌 경우

예제:
입력: "listen", "silent"
출력: True

입력: "Dormitory", "dirty room"
출력: True

입력: "abc", "abcd"
출력: False

힌트:
- 문자열을 소문자로 바꾸고 공백은 건너뜁니다
- 딕셔너리에 {글자: 등장 횟수}를 기록합니다 (키가 없으면 0에서 시작)
- 두 딕셔너리가 같으면 애너그램입니다
"""


def is_anagram(s, t):
    """
    두 문자열이 애너그램인지 판별하는 함수

    Args:
        s: 첫 번째 문자열
        t: 두 번째 문자열

    Returns:
        bool: 애너그램이면 True, 아니면 False
    """

    # buffer_list1 = list()
    # buffer_list2 = list()
    # for i in range(len(s)):
    #     i = s[i]
    #     if i.isalnum() == True:
    #         buffer_list1.append(i)
    # for j in range(len(t)):
    #     j = t[j]
    #     if j.isalnum() == True:
    #         buffer_list2.append(j)

    # c = "".join(buffer_list1)
    # d = "".join(buffer_list2)
    # e = c.lower()
    # f = d.lower()
    # g = dict()
    # h = dict()
    # for i in range(len(e)):
    #     temp = e[i]
    #     if not g.get(temp):
    #         g[temp] = 1
    #     else:
    #         g[temp] += 1

    # for i in range(len(f)):
    #     temp = f[i]
    #     if not h.get(temp):
    #         h[temp] = 1
    #     else:
    #         h[temp] += 1
    # if g == h:
    #     return True
    # else:
    #     return False

    # ======================================================
    # dictionary로 시작하고, string인 객체를
    # s.replace(" ","").lower() 로 만들면 훨씬 간단함.
    # ======================================================

    dict_1 = {}
    for char in s.replace(" ", "").lower():
        if not dict_1.get(char):
            dict_1[char] = 1
        else:
            dict_1[char] += 1

    dict_2 = {}
    for char in t.replace(" ", "").lower():
        if not dict_2.get(char):
            dict_2[char] = 1
        else:
            dict_2[char] += 1
    if dict_1 == dict_2:
        return True
    else:
        return False


# 테스트 케이스
if __name__ == "__main__":
    tests = [
        ("listen", "silent"),
        ("hello", "world"),
        ("Dormitory", "dirty room"),
        ("abc", "abcd"),
        ("aabb", "abab"),
    ]
    for i, (s, t) in enumerate(tests, 1):
        print(f"=== 테스트 케이스 {i} ===")
        print(f'입력: "{s}", "{t}"')
        print(f"애너그램 여부: {is_anagram(s, t)}")
        print()
