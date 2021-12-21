a=1
b=2
print(a,b)

print()
# 출력 줄 바꿈 예시

print(a)
print(b)

# 변수를 문자열로 바꾸어 출력

answer=7
print("정답은 "+str(answer)+"입니다.")
print("정답은",str(answer),"입니다.") # 의도치 않은 공백이 삽입될 수 있음

print(f"정답은 {answer}입니다.") # f-string