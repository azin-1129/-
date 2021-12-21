from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement

# 클래스라서 list로 변환

data=['A','B','C']
result=list(permutations(data,3)) # 객체에서 r개 데이터 뽑아 일렬로 나열하는 모든 경우의 수
print(result)
print()

result=list(combinations(data,2)) # 객체에서 r개 데이터 뽑아 순서 고려하지 않고 나열
print(result)
print()

result=list(product(data,repeat=2)) # 객체에서 r개 데이터 뽑아 일렬로 나열하는 모든 경우의 수(중복 포함)
print(result)

result=list(combinations_with_replacement(data,2)) # 객체에서 r개 데이터 뽑아 순서 고려하지 않고 나열(중복 포함)

