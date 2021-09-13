import numpy as np

# 혹여나 넘파이(numpy) 가 설치되있징 않다면
# cmd => pip install numpy 실행하면 알아서 설치댐

x = np.array([1.0, 2.0, 3.0])
# [1.2.3.]
print(x)

# <class 'numpy.ndarray'>
print(type(x))

y = np.array([2.0, 4.0, 6.0])

# 원소별 덧셈을 실행
print(x + y)

# 원소별 뺄셈을 실행
print(x - y)

# 원소별 곱셈을 실행
print(x * y)

# 원소별 나눗셈을 실행
print(x / y )


# 여기서 주의할 점은 배열 x와 y의 원소 갯수가 같다는 점입니다. (둘다 원소를 3개씩 가지는 1차원 배열)
# x 와 y의 원소 갯수가 다르다면 오류가 발생합니다.

# 참고로 "원소별" 이라는 말은 영어로 element-wise 라고 함
# "원소별 곱셈"은 element-wise product라고 함

# 그리고 원소들끼리의 산술연산이 아닌 특정 스칼라와의 연산도 가능함
# 이럴땐 배열 내 모든 원소가 하나의 스칼라와 산술연산을 실행함
print(x / 2.0)

