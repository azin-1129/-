# 0~19 수 중 홀수만
array=[i for i in range(20) if i%2==1]
print(array)

# 1~9 제곱값
array=[i*i for i in range(1,10)]
print(array)

# N*M 크기 리스트 초기화
n=3
m=4
array=[[0]*m for _ in range(n)]
print(array)