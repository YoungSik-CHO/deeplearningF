import numpy as np
# 넘파이는 1차원 배열(1줄로 늘어선 배열) 뿐 아니라 다차원 배열도 작성할 수 있음.
# 예를 들어 2차원 배열(행렬)은 다음처럼 작성함.

A = np.array([[1,2], [3,4]])
print(A)

# 몇행 몇열이냐? (2,2) => 2행 2열
print(A.shape)

# 행렬에 담긴 원소의 자료형
print(A.dtype)

B = np.array([[3,0], [0,6]])
# 다차원 행렬의 덧셈
print(A + B)

# 다차원 행렬의 곱셈
print(A * B)

# 형상이 같은 행렬끼리면 행렬의 산술 연산도 대응하는 원소별로 계산됨
# 다차원 행렬도 1차원 행렬과 같이 특정 스칼라와의 연산이 가능함 = 브로드캐스트(broadCast)
print (A * 10)

### 넘파이 배열은 N차원 배열을 작성할 수 있습니다.
### 1차원 배열, 2차원 배열, 3차원 배열 처럼 원하는 차수의 배열을 만들수 있다는 뜻.
### 일반적으로 수학에서는 1차원 배열은 벡터(Vector), 2차원 배열은 행렬(Matrix)이라고 부름.
### 그리고 벡터와 행렬을 일반화 한 것을 텐서(tensor)라고 함 

