a=[1,4,3]
print("기본 리스트:",a)

a.append(2) #[1,4,3,2]
print("삽입:",a)

a.sort() #[1,2,3,4]
print("오름차순 정렬:",a)

a.sort(reverse=True) #[4,3,2,1]
print("내림차순 정렬:",a)

a.reverse() #[1,2,3,4]
print("원소 뒤집기:",a)

a.insert(2,3) #[1,2,3,3,4]
print("인덱스 2에 3 추가:",a)

print("값이 3인 데이터 개수:",a.count(3))

a.remove(1)
print("값이 1인 데이터 삭제:",a)

a=[1,2,3,4,5,5,5]
remove_set={3,5}

result=[i for i in a if i not in remove_set]
print(result)