# from random import *
# import sys
# list=["apple","banana","orange"]

# a=randint(0,2)
# print("정답 : {0} \n".format(list[a]))
# b=len(list[a])
# list_b=["_"]*b
# for i in range(1,len(list_b)+1):
#     print(list_b[i-1],end=" ")
# #print("{0}".format(list[a][0]))
# num=10
# d=0
# list_c=""
# while True:
#     d += 1
#     c=input("알파벳을 입력하세요:")    
#     if c in list[a]:
#         print("정답입니다")
#         list_c.__add__(c)
#         print(list_c)
#         del list_b[a]
#         list_b.append(c)
#         print(list_b)
#     elif c not in list[a]:
#         num -=1
#         print("기회가 한번 날라갔습니다 남은기회{0}".format(num))
#     if c=="탈출":
#         sys.exit()
#     if num==0:
#         break

from random import *
words=["apple","banana","orange"]
a=randint(0,2)
word=words[a]
print("answer:" + word)
letters=""

class BignumberError(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return self.msg

while True:
    try:
        succeed= True
        for w in word:# a p p l e
            if w in letters:
                print(w,end=" ")
            else: 
                print("_",end=" ")
                succeed= False
        if succeed == True:
            print(" \nall correct")
            break
        
        input_str=input("\n알파벳을 입력하시오")
        if len(input_str)>=2:
            raise BignumberError("한자리 알파벳만 입력하세요^^")
        if input_str not in letters:
            letters += input_str
        if input_str in word:
            print("correct\n")
        else:
            print("wrong\n")
    except BignumberError as err:
        print(err)
    except ValueError:
        print("잘못된 값을 입력하였습니다")
    


