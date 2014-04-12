from pyplasm import *
from larcc import *
from exercise2 import *

brown = makeColor(101,67,33)
lightgrey = makeColor(210,210,210)
grey = makeColor(128,128,128)
darkgrey = makeColor(79,79,79)
lightgreen = makeColor(102,255,0)
stadiumcolor = makeColor(173,255,47)
def makePalace(coordinate):
	bx,by = coordinate
	def makePalace0(x,y,z):
		palace = COLOR(lightgrey)(CUBOID([x,y,z]))
		wx1 = x/4
		wz = z/3
		wx2 = (x/2)-1
		window_x = QUOTE([-1.5,1,-1.5]*wx1)
		window_y = QUOTE([0.1])
		window_z = QUOTE([-1,1,-1]*(wz-1))
		window = MATERIAL(glass)(T(3)(3)((INSR)(PROD)([window_x,window_y,window_z])))
		door_x = QUOTE([-wx2,2])
		door_y = QUOTE([0.1])
		door_z = QUOTE([2])
		door = COLOR(brown)((INSR)(PROD)([door_x,door_y,door_z]))
		palace = T([1,2,3])([3,3,0.2])(STRUCT([T(2)(0.1)(palace),window,door]))
		plan = COLOR(grey)(CUBOID([x+6,y+6,0.2]))
		palace = T([1,2])([bx,by])(STRUCT([palace,plan]))
		return palace
	return makePalace0



# c = makePalace([2,4])(16,10,21)
# VIEW(c)
tribune1 = CUBOID([140,20,1])
tribune2 = CUBOID([140,19,2])
tribune3 = CUBOID([140,18,3])
tribune4 = CUBOID([140,17,4])
tribune5 = CUBOID([140,16,5])
tribune6 = CUBOID([140,15,6])
tribune7 = CUBOID([140,14,7])
tribune8 = CUBOID([140,13,8])
tribune9 = CUBOID([140,12,9])
tribune10 = CUBOID([140,11,10])
tribune11 = CUBOID([140,10,11])
tribune12 = CUBOID([140,9,12])
tribune13 = CUBOID([140,8,13])
tribune14 = CUBOID([140,7,14])
tribune15 = CUBOID([140,6,15])
tribune16 = CUBOID([140,5,16])
tribune17 = CUBOID([140,4,17])
tribune18 = CUBOID([140,3,18])
tribune19 = CUBOID([140,2,19])
tribune20 = CUBOID([140,1,20])
tribune_1 = STRUCT([tribune1,tribune2,tribune3,tribune4,tribune5,tribune6,tribune7,tribune8,tribune9,
	tribune10,tribune11,tribune12,tribune13,tribune14,tribune15,tribune16,tribune17,tribune18,tribune19,tribune20])
tribune_2 = T([1,2])([160,150])(R([1,2])(PI)(tribune_1))
tribune_1 = T([1,2])([20,10])(tribune_1)
tribune = STRUCT([tribune_1,tribune_2])
field = COLOR(stadiumcolor)(CUBOID([140,100,0.2]))
field = T([1,2])([20,30])(field)
stadium = STRUCT([tribune,field])
street = COLOR(darkgrey)(CUBOID([300,300]))
plan1 = COLOR(grey)(CUBOID([90,90,0.2]))
park = COLOR(lightgreen)(T([1,2])([5,5])(CUBOID([80,80,0.4])))
park = T([1,2])([205,205])(STRUCT([plan1,park]))
palace1 = makePalace([30,240])(30,45,90)
palace2 = makePalace([90,240])(33,30,60)
palace3 = makePalace([150,240])(27,30,120)
palace4 = makePalace([30,180])(30,30,30)
palace5 = makePalace([150,180])(45,30,102)
palace6 = makePalace([190,140])(30,30,60)
palace7 = makePalace([240,140])(45,54,45)
palace8 = makePalace([190,90])(30,30,30)
palace9 = makePalace([240,90])(30,30,90)
palace = STRUCT([palace1,palace2,palace3,palace4,palace5,palace6,palace7,palace8,palace9])
plan2 = COLOR(grey)(CUBOID([50,50,0.2]))
fascioHouse = STRUCT([plan2,T([1,2,3])([8.5,10,0.2])(model)])
fascioHouse = T([1,2])([80,170])(fascioHouse)
plan3 = COLOR(grey)(CUBOID([90,70,0.2]))
parking = COLOR(darkgrey)(CUBOID([80,60,0.1]))
parking = T([1,2])([190,10])(STRUCT([plan3,T([1,2,3])([5,5,0.2])(parking)]))
city = STRUCT([street,park,palace,fascioHouse,parking,stadium])
VIEW(city)

