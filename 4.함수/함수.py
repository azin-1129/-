def add(a,b):
    return a+b

print(add(3,7))

# return문 없이 작성

def add(a,b):
    print('함수의 결과:',a+b)

add(3,7)

def add(a,b):
    print('a의 값:',a,'b의 값:',b)
    print('함수의 결과:',a+b)

add(b=3,a=7)

# global

a=0

def func():
    global a
    a+=1

for i in range(10):
    func()

print(a)

# 람다

def add(a,b):
    return a+b

# 일반적 add() method
print(add(3,7))

# lambda
print((lambda a,b:a+b)(3,7))