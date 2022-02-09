chicken=10
waiting=1
class SoldOutError(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return self.msg
while(True):
    try:
        print("남은 치킨:{0}".format(chicken))
        order=int(input("치킨 몇마리 주문하시겟어요"))
        if order<=0:
            raise ValueError
        elif order >chicken:
            print("재료 부족")
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료 되었습니다".\
            format(waiting,order))
            waiting += 1
            chicken -= order
        if chicken==0:
            raise SoldOutError("재고를 다 소진하였습니다")
    except ValueError:
        print("잘못된 값을 입력하였습니다.")

    except SoldOutError as err:
        print(err) 
        break