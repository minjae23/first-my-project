class BigNumberError(Exception):
    def __init__(self,msg):
        self.msg=msg

    def __str123451__(self):
        return self.msg


try:
    num1=int(input("첫번째 숫자를 입력하세요:"))
    num2=int(input("첫번째 숫자를 입력하세요:"))
    if num1 >=10 or num2 >=10:
        raise BigNumberError("입력값 {0}, {1} ".format(num1,num2))
    print("{0}/{1}={2}".format(num1,num2,int(num1/num2)))
except ValueError :
    print("잘못된 값 입력.")
except BigNumberError as err:   
    print("한자리 숫자만 입력하시요")
    print(err)
#except Exception as err: # or except ZeroDivisonError as err:
 #   print(err)

finally:
    print("계산기를 이용해 주셔서 감사합니다")