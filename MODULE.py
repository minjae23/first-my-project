# #일반 가격
# def price(people):
#     print("{0}명 가격은 {1}원 입니다".format(people,people*10000))

# #조조 할인 가격
# def price_morning(people):
#     print("{0}명 조조 할인 가격은 {1}원 입니다".format(people,people*6000))

# def price_soldier(people):
#     print("{0}명 군인 할인 가격은 {1}원 입니다".format(people,people*4000))

# import travel.thilland
# trip_to= travel.thilland.ThillandPackage()
# trip_to.detail()

# from travel.thilland import ThillandPackage
# trip_1=ThillandPackage()
# trip_1.detail()
# from travel import thilland

# trip_1=thilland.ThillandPackage()
# trip_1.detail()

from travel import *
trip_to= thilland.ThillandPackage()
trip_to.detail()

import random
import inspect

print(inspect.getfile(random))
print(inspect.getfile(thilland))
