import heapq

def heapsort(iterable):
    h=[]
    result=[]

    for value in iterable:
        heapq.heappush(h,value)

    for i in range(len(h)):
        result.append(heapq.heappop(h)) # heappop의 인자는 대상 리스트.
    return result

result=heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

def heapsortReverse(iterable):
    h=[]
    result=[]
    for value in iterable:
        heapq.heappush(h,-value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result=heapsortReverse([1,3,5,7,9,2,4,6,8,0])
print(result)
