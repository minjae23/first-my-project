#일반유닛

from types import ClassMethodDescriptorType


class Unit:
    def __init__(self, name, hp,speed):
        self.name=name
        self.hp=hp
        self.speed=speed
    def move(self,location):
        print("[지상 유닛 이동]")
        print("{0}:{1} 방향으로 이동합니다 스피드:{2}"\
            .format(self.name,location,self.speed))
        
        
#공격유닛
class AttackUnit(Unit):
    def __init__(self,name,hp,speed ,damage):
        Unit.__init__(self,name,hp,speed)
        self.damage=damage
    def attack(self,location):
        print("{0}가 {1}방향으로 공격하고있습니다. 공격력 {2}"\
         .format(self.name,location,self.damage))
    def damaged(self,damage):
        print("{0} : {1}  데미지를 입었습니다 ".format(\
            self.name,damage))
        self.hp-=damage
        print("{0}의 남은 체력은 {1} 입니다.".format(\
            self.name,self.hp))
        if self.hp<=0:
            print("{0} 가 파괴되었습니다".format(self.name))
            

firebat=AttackUnit("파이어뱃", 80 , 7,15)

firebat.attack(5)
while firebat.hp!=0:
    firebat.damaged(10)
    if firebat.hp<=0:
        break

#낧수 있는 유닛
class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed=flying_speed
    
    def fly(self,name,location):
        print("{0}:{1} 방향으로 날라갑니다. [속도 : {2}]"\
            .format(name,location,self.flying_speed))

#공중 공격 유닛
class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self,name,hp,damage,flying_speed):
        AttackUnit.__init__(self,name,hp,0,damage)#상속받은 클래스 변수 초기화
        Flyable.__init__(self,flying_speed)
    def move(self,location): # 메소드 오버라이딩
        print("[공중 유닛 이동]")
        self.fly(self.name,location)
# #발카리 공중 공격 유닛 한번에 14발 미사일 발사 
valkyrie=FlyableAttackUnit("발키리",200,6,5)
valkyrie.fly(valkyrie.name,"3시")
print(firebat.name)
print(valkyrie.name)

vulture=AttackUnit("벌처",100,10,20)
vulture.move("11시")

battlecrusie=FlyableAttackUnit("배틀크루저",500,50,3)
battlecrusie.move("11시")

def game_start():
    print("게임을 시작합니다")
def game_over():
    pass

game_start()
game_over()

class BuildingUnit(Unit):
    def __init__(self,name,hp,location):
        super().__init__(name,hp,location)