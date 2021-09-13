# bool 이라는 자료형이 있음
# True 또는 False 의 값을 가짐
# bool에는 and , or , not 연산자를 사용할 수 있음
# and : 두가지 이상의 bool의 교집합
# or : 두가지 이상의 bool의 합집합
# not : 해당 bool의 반대(bool이 아님)

hungry = True
sleepy = False

print(hungry)
print(sleepy)

# <class 'bool'>
print(type(hungry))

# true && false = false
print(hungry and sleepy)
# true || false = true
print(hungry or sleepy)
# not(true) = false
print(not hungry)