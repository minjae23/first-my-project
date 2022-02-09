"""
print('test')
print(not False)
print(not True)
print(not (5>10))

name = "레레"
animal="고양이"
age =10     

a=0x1f
print(not False)
"""
"""
연산 + - * / % ( // 몫, **제곱 연산)
다른 프로그램 -boolean 연산자 and (&&) or(||) not (!)
교집합 & 합집합 | 차집합 -
"""
"""
t1=(1,3,2) # 튜플 (,,)
t2=("hello",2)
t3=t2[0]
print(t1)
print(t1+t2)
print(t1*3)
print(t3)

# dictionary
dic={1:"I",2:"you",3:"LOVE"}

print(dic[1]+" " + dic[3]+" " + dic[2])
print(3 in dic.keys())
print(dic.values())
print(dic.keys())
print(dic.items())

#list < list 안에 다른 list들을 포함할 수 있다

list=[1,2,4,3]
mylist=["a","d","v"]
print(list)
print(list[2])  

# sort , reverse , append ,del

list.sort()
print(list)
list.reverse()
print(list)
list.append(5)
print(list)
list.reverse()
print(list)
list.sort()
print(list)
del list[0]
print(list)

yourlist=[list,mylist]
print(yourlist)
# set {, ,}
s1={1,2,3}
s2={1,3,3}
print(s2)
print(s1-s2)
print(s1&s2)
print(s1|s2)
s3=set(list)
print(s3)




"""
"""

a=1
b=2
if a==1:
    print(1==1)
else:
    print(False)

x=[1,2,3]
print('b' in x)

if a or b  in x:
    print(1==1)
else:
    print(False)

# while 문

meet =0
while meet<4:
    meet= meet + 1
    print("meet 가 %d 번 방문했습니다 " % meet)
    if meet==4:
        print("out")
        break
    """
m="""
안녕
나는 
병신
이다
"""

"""
num=0
while num != 4:
    print(m)
    num=int(input())


i="minjae"
i=str(input())
print(i)

while True:
    print("ang gimothy")
"""
"""
f=[(1,2),(3,4),(5,6)]
for (i,m) in f:
    print(i+m)

sum = 0
for a in range(1,5):
    sum=sum+a
print(sum)
for a in range(2,10):
    for b in range(1,10):
        print(a ,"x",b, "=" , a*b)
c="개 ㅅ ㄲ"
print("우리집"+ str(b) + "이름은 멍멍이다")

def sum_2(s,d):
    return s+d

c=sum_2(3,5)

print(c)

def sum_3(*arsg):
    sum=0
    for z in arsg:
        sum=sum+z
    print(sum)

sum_3(1,3,4,56,173,71,13216)

FILE="C:/PYTHON/test.txt"

f=open("C:/PYTHON/test.txt",'w')
for n in range(1,6):
    line="%d 번째쩨 줄\n" % n
    f.write(line)
f.close()

f=open(FILE,'r')
lines=f.readlines()
for n in lines:
    print(n)

f.close()

f=open(FILE,'a')
for n in range(6,11):
    line="%d 번째쩨 줄\n" % n
    f.write(line)

f.close()

class Horse:
    def __init__(self,age,height,color,xpos,ypos):
        self.__age__=17
"""
station=["사당","신도림","인천공황"]

for i in station:
    print("%s행 열차가 들어오고 있습니다"%i)