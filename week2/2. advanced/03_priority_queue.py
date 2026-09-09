"""
[우선순위 큐 - 응급실 환자 관리]

문제 설명:
- 우선순위 큐를 사용하여 환자를 우선순위에 따라 처리합니다.
- 숫자가 작을수록 우선순위가 높습니다 (1 > 2 > 3).

입력:
- patients: (이름, 우선순위) 튜플 리스트

출력:
- 우선순위에 따라 처리된 환자 순서

예제:
입력: [("김철수", 3), ("이영희", 1), ("박민수", 2)]
출력:
처리: 이영희 (우선순위: 1)
처리: 박민수 (우선순위: 2)
처리: 김철수 (우선순위: 3)

힌트:
- heapq 모듈 사용
- heappush(): 힙에 추가
- heappop(): 최소값 제거
"""


def process_emergency_room(patients):
    """
    환자를 우선순위에 따라 처리

    Args:
        patients: (이름, 우선순위) 리스트

    Returns:
        처리된 환자 순서
    """

    patients.sort(key=lambda x: x[1])  # 우선순위(x[1]) 기준 오름차순 정렬
    return [x[0] for x in patients]  # 우선순위 기준 이름(x[0]) 추출


# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    patients1 = [("김철수", 3), ("이영희", 1), ("박민수", 2)]
    print("=== 응급실 환자 처리 ===")
    processed1 = process_emergency_room(patients1)
    for name, priority in patients1:
        print(f"처리: {name} (우선순위: {priority})")
    print(f"처리 순서: {processed1}")
    print()

    # 테스트 케이스 2
    patients2 = [("환자A", 5), ("환자B", 1), ("환자C", 3), ("환자D", 2)]
    print("=== 응급실 환자 처리 ===")
    processed2 = process_emergency_room(patients2)
    for name, priority in patients2:
        print(f"처리: {name} (우선순위: {priority})")
    print(f"처리 순서: {processed2}")

    # # ====================================
    # [while & for 문을 통한 완전탐색 버전 - 최악의 경우 O(n!)]
    # # ====================================

    # # 1. 이름, 우선순위, 처리 완료 객체 생성
    # heap = []
    # priority_list = []
    # processed = []

    # # 2. 모든 환자를 힙에 추가
    # for name, priority in patients:
    #     heap.append(name)
    #     priority_list.append(priority)  # priority_list에 우선순위들 추가

    # # 3. [Main](반복) 힙에서 우선순위가 가장 높은 환자 꺼내기 & 환자 처리
    # while heap:
    #     for name, priority in patients:
    #         if not priority_list:
    #             break
    #         if priority == min(priority_list):
    #             processed.append(name)
    #             priority_list.remove(priority)
    #             heap.remove(name)

    # # ======================================
    # [시행착오 1] 4. 우선순위에 따라 tuple의 오른쪽 값(우선순위)을 name과 매칭해서 processed에 집어넣기
    #  --- 왜 이 계획을 철회했는가? => .sort()를 쓴 이유는 결국 while 없이 우선순위를 for(1번 순회)로 정렬하려고 했던 것인데, 자연스럽게 while로 넘어가게 되어서. 사고의 전환이 필요했음.
    # # ====================================

    # while (name, priority) in patients:
    #     if not priority_list:
    #         break
    #     temp = priority_list.pop() # 가장 큰 우선순위 tuple 뽑기
    #     if priority == temp[-1]:
    #         processed.append(name)
    #         priority_list.remove(temp)
    # return processed

    # # ======================================
    # [시행착오 2](-priority, priority) 객체 생성을 통한 sorting & list의 pop()을 활용하고자 했으나, 결국 N(n^2)나서 포기
    # # =====================================

    # # 1. 이름, 우선순위, 처리 완료 객체 생성
    # heap = []
    # priority_list = []
    # processed = []

    # # 2. 모든 환자를 힙에 추가
    # for name, priority in patients:
    #     heap.append(name)
    #     priority_list.append(
    #         (priority * -1, priority)
    #     )  # priority_list에 우선순위들 추가

    # # 3. 시급한 것이 뒤로 오도록 정렬
    # priority_list.sort()

    # # 4. 별도 우선순위를 정렬한
    # for priority_tuple in priority_list:
    #     temp = priority_tuple[-1]
    #     for name, priority in patients:
    #         if priority == temp:
    #             processed.append(name)

    # # ===========================================
    # # [앞 뒤 sorting한 버전 - O(N logN)]
    # # ===========================================

    # patients_reverse = []

    # for tuple in patients:
    #     # print(tuple) - 디버깅용
    #     patients_reverse.append((tuple[-1], tuple[0]))
    #     # print(patients_reverse)
    # patients_reverse.sort() # (우선순위, 환자)로 바꾸고 우선순위 기반 정렬

    # for tuple in patients_reverse:
    #     processed.append(tuple[1]) # 이름만 processed에 추가
    # return processed
    #
    # ======================================
    # 정석(heapq 모듈 사용) 버전
    # ======================================
    #
    #  def process_emergency_room(patients):
    #     processed = []
    #     heap = [(priority, name) for name, priority in patients]
    #     heapq.heapify(heap)
    #     for _ in range(len(heap)): # O(N log N)
    #         item = heapq.heappop(hea p)
    #         name = item[1] # 최솟값의 이름
    #         processed.append(name),
    #     return processed
