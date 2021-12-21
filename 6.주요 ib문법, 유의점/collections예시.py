# append,pop (뒤)
# appendleft,popleft (앞)

from collections import deque
from collections import Counter

data=deque([2,3,4])
data.appendleft(1) # 1,2,3,4
data.append(5) # 1,2,3,4,5

print(data)
print(list(data))

print()
counter=Counter(['red','blue','red','green','blue','blue']) # 숫자는 안 되는 거 같넹

print(counter['blue'])
print(counter['green'])
print(dict(counter))
print(counter)