# demo.py
# 주석따리
# 코드실행 ctrl + F5
# 터미널 토글 ctrl + ~

print("hello VS code")

colors = ["red","green","blue"]
print(colors)

print (type(colors))


colors.append("white")

print(colors)

colors.insert(1,"black")


print(colors)

print(colors.index("white"))

colors += "red"
print(colors)

#역순으로 삭제
colors.pop()
print(colors)

colors.pop()
print(colors)
colors.pop(4)

print(colors)
colors.remove('r')

colors.sort()

colors.reverse()

#튜플 리스트와 유사, 읽기전용, 속도 리스트에비해 빠름, 기능적음

t = (1,2,3)

#튜플이 주로 사용되는 경우 : 함수에서 하나 이상의 값을 리턴하는 경우
def calc(a,b):
    return a+b, a*b

result = calc(5,6)
print(result)

# 문자열 포맷팅
# 튜플에 있는 값을 함수 인자로 사용
# * 쓰면 튜플을 의미함 pointer가 아님, 튜플에 담에 한번에 넘긴다는 의미


