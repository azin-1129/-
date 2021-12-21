i=1
result=0

while i<=9:
    result+=i
    i+=1

print(result)

# 1~9까지 홀수일 경우만 더하기

i=1
result=0

while i<=9:
    if i%2!=0:
        result+=i
        i+=1
    else:
        i+=1

print(result)