"""
[우선순위 큐 - 단계별 벤치마크]

03_priority_queue.py의 주석에 묻혀 있는 시도들을 실행 가능한 함수로 복원하고,
정확성 교차검증과 실행 시간 측정을 수행합니다.

원본 03_priority_queue.py는 제출물이므로 수정하지 않습니다.
이 파일은 그 주석을 읽기 위한 별도의 측정 도구입니다.

각 단계 함수의 로직은 원본 주석과 동일합니다. 실행을 위해 최소한으로 손댄 곳은
함수마다 주석으로 명시했습니다.
"""

import heapq
import random
import time


# ============================================================
# 단계 1 : 원본 62-84행
#   [while & for 문을 통한 완전탐색 버전 - 최악의 경우 O(n!)]
#   손댄 곳: patients를 인자로 받도록 감쌌고, processed를 return합니다.
# ============================================================
def stage1_bruteforce(patients):
    heap = []
    priority_list = []
    processed = []

    for name, priority in patients:
        heap.append(name)
        priority_list.append(priority)

    while heap:
        for name, priority in patients:
            if not priority_list:
                break
            if priority == min(priority_list):
                processed.append(name)
                priority_list.remove(priority)
                heap.remove(name)

    return processed


# ============================================================
# 단계 2 : 원본 100-124행
#   [시행착오 2] (-priority, priority) 객체 생성을 통한 sorting
#   손댄 곳: 함수로 감쌌고, processed를 return합니다.
#           쓰이지 않는 heap 리스트는 원본 그대로 남겨 두었습니다.
# ============================================================
def stage2_negtuple(patients):
    heap = []
    priority_list = []
    processed = []

    for name, priority in patients:
        heap.append(name)
        priority_list.append((priority * -1, priority))

    priority_list.sort()

    for priority_tuple in priority_list:
        temp = priority_tuple[-1]
        for name, priority in patients:
            if priority == temp:
                processed.append(name)

    return processed


# ============================================================
# 단계 3 : 원본 126-140행
#   [앞 뒤 sorting한 버전 - O(N logN)]
#   손댄 곳: 함수로 감쌌고, processed를 함수 안에서 초기화합니다.
#           디버깅용 print 두 줄은 뺐습니다.
# ============================================================
def stage3_sortpair(patients):
    processed = []
    patients_reverse = []

    for tuple in patients:
        patients_reverse.append((tuple[-1], tuple[0]))
    patients_reverse.sort()

    for tuple in patients_reverse:
        processed.append(tuple[1])

    return processed


# ============================================================
# 단계 4 : 원본 39-40행 (현재 제출본)
#   손댄 곳: 없습니다. 원본 그대로입니다.
#   주의: 인자로 받은 리스트를 제자리에서 정렬합니다(부작용 있음).
# ============================================================
def stage4_sortkey(patients):
    patients.sort(key=lambda x: x[1])
    return [x[0] for x in patients]


# ============================================================
# 부록 : 원본 142-154행
#   정석(heapq 모듈 사용) 버전
#   손댄 곳: 151행의 오타 `heapq.heappop(hea p)`를 `heapq.heappop(heap)`으로
#           고쳤습니다. 그 외에는 원본 그대로입니다.
# ============================================================
def stage5_heapq(patients):
    processed = []
    heap = [(priority, name) for name, priority in patients]
    heapq.heapify(heap)
    for _ in range(len(heap)):
        item = heapq.heappop(heap)
        name = item[1]
        processed.append(name)
    return processed


STAGES = [
    ("단계 1  완전탐색", stage1_bruteforce),
    ("단계 2  음수 튜플", stage2_negtuple),
    ("단계 3  앞뒤 뒤집어 sort", stage3_sortpair),
    ("단계 4  key로 sort", stage4_sortkey),
    ("부록    heapq", stage5_heapq),
]


def make_patients(n, distinct=True):
    """(이름, 우선순위) 리스트를 만듭니다.

    distinct=True  이면 우선순위가 1..n으로 전부 다릅니다.
    distinct=False 이면 우선순위가 1..5에서 뽑혀 중복이 많이 생깁니다.

    이름은 인덱스로 붙여서 전부 다르게 만듭니다. 단계 1이 heap.remove(name)을
    쓰기 때문에, 이름이 겹치면 엉뚱한 원소가 지워집니다.
    """
    if distinct:
        priorities = list(range(1, n + 1))
        random.shuffle(priorities)
    else:
        priorities = [random.randint(1, 5) for _ in range(n)]
    return [(f"환자{i:07d}", priorities[i]) for i in range(n)]


def make_shaped(n, shape):
    """입력 모양별 환자 명단.

    단계 1은 입력 모양에 따라 비용이 크게 달라집니다. 우선순위가 오름차순으로
    들어오면 바깥 while이 한 바퀴만에 전부 빼내지만, 내림차순이면 한 바퀴에
    한 명씩만 빠져서 while이 n번 돕니다.
    """
    if shape == "asc":
        priorities = list(range(1, n + 1))
    elif shape == "desc":
        priorities = list(range(n, 0, -1))
    elif shape == "rand":
        priorities = list(range(1, n + 1))
        random.shuffle(priorities)
    else:
        raise ValueError(shape)
    return [(f"환자{i:07d}", priorities[i]) for i in range(n)]


# ============================================================
# 1부 : 정확성 교차검증
# ============================================================
def check_tie_order():
    """이름의 사전순과 입력 순서가 어긋나는 입력으로 동점 처리 규칙을 드러냅니다.

    make_patients()는 이름을 인덱스 순으로 붙이기 때문에 사전순과 입력 순서가
    항상 같습니다. 그러면 단계별 동점 규칙 차이가 보이지 않습니다.
    """
    print()
    print("=" * 68)
    print("1부-보충. 우선순위가 같을 때 누가 먼저 나오는가")
    print("=" * 68)

    data = [("정환자", 1), ("김환자", 1), ("박환자", 1)]
    print(f"  입력(셋 다 우선순위 1): {[n for n, _ in data]}")
    for name, fn in STAGES:
        out = fn([t for t in data])
        print(f"  {name:24s} {out}")
    print("  단계 4만 입력 순서를 유지합니다. 나머지는 이름 사전순이 됩니다.")


def check_correctness():
    print("=" * 68)
    print("1부. 정확성 교차검증")
    print("=" * 68)

    for label, distinct in (("우선순위가 전부 다른 경우", True),
                            ("우선순위가 겹치는 경우", False)):
        random.seed(20260910)
        data = make_patients(8, distinct=distinct)
        print(f"\n[{label}]  n=8")
        print(f"  입력: {data}")

        results = {}
        for name, fn in STAGES:
            out = fn([t for t in data])   # 단계 4의 부작용을 막으려고 사본을 넘깁니다
            results[name] = out
            print(f"  {name:24s} 길이 {len(out):2d}  {out}")

        baseline = results["단계 4  key로 sort"]
        print("  -- 단계 4를 기준으로 비교하면 --")
        for name, out in results.items():
            if name == "단계 4  key로 sort":
                continue
            if out == baseline:
                verdict = "일치"
            elif len(out) != len(baseline):
                verdict = f"불일치: 개수가 다름 ({len(out)} vs {len(baseline)})"
            elif out == baseline[::-1]:
                verdict = "불일치: 순서가 완전히 역순"
            elif sorted(out) == sorted(baseline):
                verdict = "동점 순서만 다름 (구성은 같음)"
            else:
                verdict = "불일치: 구성이 다름"
            print(f"  {name:24s} {verdict}")


# ============================================================
# 2부 : 실행 시간 측정
# ============================================================
REPEAT = 3
TIME_BUDGET = 20.0   # 이 시간을 넘기면 더 큰 n은 건너뜁니다

# 단계마다 감당 가능한 n의 범위가 크게 다릅니다.
# 하나의 n으로 통일하면 빠른 단계가 전부 0.000초로 뭉개져서 아무것도 안 보입니다.
LADDERS = {
    "단계 1  완전탐색": [100, 200, 500, 1_000, 2_000],
    "단계 2  음수 튜플": [1_000, 2_000, 4_000, 8_000],
    "단계 3  앞뒤 뒤집어 sort": [10_000, 100_000, 400_000, 1_000_000],
    "단계 4  key로 sort": [10_000, 100_000, 400_000, 1_000_000],
    "부록    heapq": [10_000, 100_000, 400_000, 1_000_000],
}


def measure(fn, data):
    """REPEAT회 중 최솟값을 돌려줍니다.

    평균은 다른 프로세스의 방해를 그대로 먹습니다. 최솟값이 그 기계에서
    가능한 가장 깨끗한 실행에 가깝습니다.
    매 회 리스트 사본을 새로 만들어 넘깁니다. 단계 4가 입력을 제자리에서
    정렬하기 때문에, 사본을 안 만들면 2회차부터 이미 정렬된 입력을 재게 됩니다.
    """
    best = None
    for _ in range(REPEAT):
        copy = [t for t in data]
        start = time.perf_counter()
        fn(copy)
        elapsed = time.perf_counter() - start
        if best is None or elapsed < best:
            best = elapsed
    return best


def run_timings():
    print()
    print("=" * 68)
    print(f"2부. 실행 시간 측정  ({REPEAT}회 중 최솟값, 우선순위가 전부 다른 입력)")
    print("=" * 68)

    table = {}
    for name, fn in STAGES:
        print(f"\n[{name}]")
        row = {}
        for n in LADDERS[name]:
            random.seed(20260910)
            data = make_patients(n, distinct=True)
            elapsed = measure(fn, data)
            row[n] = elapsed
            print(f"  n = {n:>9,}   {elapsed:>10.4f}초")
        table[name] = row
    return table


def print_growth(table):
    print()
    print("=" * 68)
    print("3부. n이 2배가 될 때 시간은 몇 배가 되는가")
    print("=" * 68)
    print("  (제곱이면 4배, 세제곱이면 8배, n log n이면 2배 남짓입니다)")

    for name, row in table.items():
        ns = sorted(row)
        print(f"\n[{name}]")
        for prev, cur in zip(ns, ns[1:]):
            ratio_n = cur / prev
            ratio_t = row[cur] / row[prev] if row[prev] > 0 else float("nan")
            print(f"  n {prev:,} → {cur:,} (×{ratio_n:.1f})"
                  f"   시간 ×{ratio_t:.2f}")


def run_shape_sensitivity():
    """단계 1의 비용이 입력 모양에 얼마나 좌우되는지 잽니다."""
    print()
    print("=" * 68)
    print("2부-보충. 단계 1은 입력 모양에 따라 비용이 달라진다")
    print("=" * 68)

    ns = [100, 200, 400, 800, 1_600]
    rows = {}
    for shape, label in (("asc", "오름차순(가장 유리)"),
                         ("desc", "내림차순(가장 불리)"),
                         ("rand", "무작위")):
        print(f"\n[{label}]")
        row = {}
        for n in ns:
            random.seed(20260910)
            data = make_shaped(n, shape)
            elapsed = measure(stage1_bruteforce, data)
            row[n] = elapsed
            print(f"  n = {n:>6,}   {elapsed:>10.4f}초", end="")
            if len(row) > 1:
                prev = ns[ns.index(n) - 1]
                print(f"   (직전 대비 ×{elapsed / row[prev]:.2f})", end="")
            print()
            if elapsed > TIME_BUDGET:
                print(f"  n = {ns[ns.index(n) + 1]:>6,}   건너뜀 "
                      f"({TIME_BUDGET:.0f}초 예산 초과)"
                      if ns.index(n) + 1 < len(ns) else "")
                break
        rows[label] = row
    return rows


# ============================================================
# 5부 : 힙이 이기는 자리
#
#   주의: 이 시나리오는 03_priority_queue.py에 없습니다.
#   부록에서 "그러면 힙은 왜 있나"에 답하려고 덧붙인 측정입니다.
#   원본 문제는 명단을 통째로 받아 한 번에 다 배출하므로, 그 조건에서는
#   정렬이 이깁니다. 아래는 조건을 바꾸면 판이 뒤집힌다는 것만 보여 줍니다.
# ============================================================
def stream_resort(arrivals):
    """환자가 한 명씩 도착할 때마다 대기줄 전체를 다시 정렬합니다."""
    waiting = []
    answers = []
    for name, priority in arrivals:
        waiting.append((priority, name))
        waiting.sort()
        answers.append(waiting[0][1])   # 지금 가장 급한 사람
    return answers


def stream_heappush(arrivals):
    """도착할 때마다 힙에 밀어 넣고 꼭대기만 봅니다."""
    heap = []
    answers = []
    for name, priority in arrivals:
        heapq.heappush(heap, (priority, name))
        answers.append(heap[0][1])      # 지금 가장 급한 사람
    return answers


def run_streaming():
    print()
    print("=" * 68)
    print("5부. 도착과 조회가 뒤섞이면  (이 시나리오는 문제 파일에 없습니다)")
    print("=" * 68)
    print("  환자가 한 명 올 때마다 '지금 가장 급한 사람'을 묻습니다.")

    for n in (1_000, 5_000, 20_000, 50_000):
        random.seed(20260910)
        arrivals = make_patients(n, distinct=True)

        a = stream_resort([t for t in arrivals])
        b = stream_heappush([t for t in arrivals])
        same = "답 일치" if a == b else "답 불일치!"

        t_sort = measure(stream_resort, arrivals)
        t_heap = measure(stream_heappush, arrivals)
        print(f"  n = {n:>7,}   매번 재정렬 {t_sort:>9.4f}초   "
              f"heappush {t_heap:>8.4f}초   "
              f"({t_sort / t_heap:>6.1f}배)   {same}")


def run_overlap():
    """다섯 버전을 같은 n에서 나란히 잽니다.

    단계별 사다리는 서로 겹치지 않아서 그대로는 비교표를 만들 수 없습니다.
    단계 1이 감당하는 범위 안에서 전부 재야 한 표에 나란히 놓을 수 있습니다.
    """
    print()
    print("=" * 68)
    print("2부-비교. 다섯 버전을 같은 n에서 나란히")
    print("=" * 68)

    ns = [250, 500, 1_000, 2_000]
    header = "  {:>7s}".format("n") + "".join(f"{name.split()[0] + name.split()[-1]:>16s}"
                                              for name, _ in STAGES)
    print(header)
    for n in ns:
        cells = []
        for name, fn in STAGES:
            random.seed(20260910)
            data = make_patients(n, distinct=True)
            elapsed = measure(fn, data)
            cells.append(f"{elapsed:>15.4f}초")
        print(f"  {n:>7,}" + "".join(cells))


def print_html_rows(table):
    print()
    print("=" * 68)
    print("4부. HTML 표에 붙여 넣을 형태")
    print("=" * 68)
    for name, row in table.items():
        print(f"\n<!-- {name} -->")
        for n in sorted(row):
            print(f'<tr><td>{n:,}</td><td class="mono">{row[n]:.4f}초</td></tr>')


if __name__ == "__main__":
    import platform
    import sys

    print(f"측정 환경: CPython {platform.python_version()} / "
          f"{platform.system()} / {platform.machine()}")
    print(f"명령: {' '.join(sys.argv)}")
    print()

    check_correctness()
    check_tie_order()
    timings = run_timings()
    shapes = run_shape_sensitivity()
    run_overlap()
    print_growth(timings)
    run_streaming()
    print_html_rows(timings)
