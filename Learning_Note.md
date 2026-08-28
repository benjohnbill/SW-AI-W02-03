01_strin.py_Note

### 01_String.py

1. "대소문자", 특수문자와 공백을 지워버린다.
    "s".isalnum()을 이용해서 T/F를 분류하고, 그 분류된 값들을 따로 담는다.
        for 문을 이용해서 str에 있는 글자들을 하나하나 꺼내 isalnum()을 한다.
		    if "n(특정 문자)".isalnum() == True:
			    그 특정 문자를 list에 append한다
				그 list에 있는 개별 문자들을 "".join한다.
  "s".lower()를 통해 변환한다.
		
2. 첫 글자와 마지막 글자가 같은 지 비교한다
(조건문에서  == operation)
    for 문에서 [i]하고 [len(items)-i]가 같은 지 비교

3. 만약 짝수라면, 2번의 과정을 n(total length)/2 번 실행하고, 각 bool 값을 & 연산자로 도출해서 return한다.

4. 만약 홀수라면, (n-1)/2번 2번의 과정을 실행하고, 즉시 & 연산자로 도출해서(중간값은 제외되게) return한다.
