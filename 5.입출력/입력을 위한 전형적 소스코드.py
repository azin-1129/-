n=int(input()) # 데이터 개수
data=list(map(int,input().split()))

data.sort(reverse=True)
print(data)