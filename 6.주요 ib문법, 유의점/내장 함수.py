result=sum([1,2,3,4,5]) # 총합
print(result)
print()

result=min(7,3,5,2) # 최솟값
print(result)
print()

result=max(7,3,5,2) # 최댓값
print(result)
print()

result=eval("(3+5)*7") # 문자열 형태 수식 계산 결과
print(result)
print()

result=sorted([9,1,8,5,4])
print(result)
result=sorted([9,1,8,5,4],reverse=True) # iterable 객체 정렬. 역=내림차순
print(result)
result=sorted([('홍길동',35),('이순신',75),('아무개',50)],key=lambda x:x[1],reverse=True)
print(result)
print()

data=[9,1,8,5,4]
data.sort() # 데이터가 정렬된 값으로 바뀜
print(data)