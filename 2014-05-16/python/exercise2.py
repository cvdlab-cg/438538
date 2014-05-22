from exercise1 import *
from larcc import *

def makeStairs(l1,l2,l3):
	stairs = []
	j = l2/5
	for i in range(l2):
		V,CV = larCuboids([l1,1,1])
		V = scalePoints(V,[1,j,l3])
		V = translatePoints(V,[0,i,i*l3])
		steps = V,CV
		stairs = stairs+[steps]
	return larStruct(stairs)

def larStruct(model_list):
	finalV=[]
	finalCV=[]
	count=0
	for m in model_list:
		finalV=finalV+m[0]
		tempCV = AA(AA(lambda x: x+count))(m[1])
		finalCV=finalCV+tempCV
		count = count + len(m[0])
	return finalV,finalCV

def makeBars(l1,h):
	bars = []
	for i in range(l1*2):
		if i==0:
			x = 0.15
		else :
			x = (.5*i)+.15
		V,CV = larCuboids([1,1,1])
		V = translatePoints(scalePoints(V,[.2,.2,h]),[x,0,0])
		bar = V,CV
		bars = bars + [bar]
	V,CV = larCuboids([1,1,1])
	V = translatePoints(scalePoints(V,[l1,.2,.2]),[0,0,h])
	bar = V,CV
	bars = bars + [bar]
	return larStruct(bars)

def makeCurve(controlpoints):
	domain = larDomain([32])
	mapping = larBezierCurve(controlpoints)
	obj = larMap(mapping)(domain)
	return STRUCT(MKPOLS(obj))

def makeTree(coordinate):
	bx,by = coordinate
	def makeTree0(dimensions):
		r,h = dimensions
		tronco = larCylinder(r,h)([32,1])
		chioma = larSphere(r*4)()
		tronco = COLOR(brown)(STRUCT(MKPOLS(tronco)))
		chioma = COLOR(forest)(STRUCT(MKPOLS(chioma)))
		return T([1,2])([bx,by])(STRUCT([tronco,T(3)(h+r)(chioma)]))
	return makeTree0

def translatePoints (points, tvect):
	result = []
	for p in points :
		result = result+[[p[0]+tvect[0],p[1]+tvect[1],p[2]+tvect[2]]]
	return result

# defining all the colors

green = makeColor(1,121,111)
grey = makeColor(147,147,147)
brown = makeColor(101,67,33)
forest = makeColor(34,139,34)
lawnColor = makeColor(152,255,152)
# water = makeColor(153,203,255)
water = [0.05,0.4,0.4,1,  0,0.3,0.3,0.5,  2,2,2,1, 0,0,0,1, 100]

apartmentRotate = larApply(s(-1,1,1))(apartment)
apartmentRotate = larApply(t(19.8,0,0))(apartmentRotate)

master = assemblyDiagramInit([3,1,13])([[19.8,8,19.8],[26],[.5,3.5,.5,3.5,.5,3.5,.5,3.5,.5,3.5,.5,3.5,.5]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),gold,2)
# VIEW(hpc)

toRemove = [14,16,18,20,22,24]
master = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),gold,2)
# VIEW(hpc)

toMerge = 14
diagram = assemblyDiagramInit([3,4,1])([[2,4,2],[4.2,2,10,7.8],[0.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)
# VIEW(hpc)

toMerge = 14
diagram = assemblyDiagramInit([3,4,1])([[2,4,2],[4.2,2,10,7.8],[0.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 14
diagram = assemblyDiagramInit([3,4,1])([[2,4,2],[4.2,2,10,7.8],[0.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)


toMerge = 14
diagram = assemblyDiagramInit([3,4,1])([[2,4,2],[4.2,2,10,7.8],[0.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 14
diagram = assemblyDiagramInit([3,4,1])([[2,4,2],[4.2,2,10,7.8],[0.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)
# VIEW(hpc)

toRemove = [14,28,32,34,36,40,44,46,48,52,56,58,60,64,68,70,72,76,80,82,84]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),gold,2)
# VIEW(hpc)
# DRAW(master)

toMerge = 0
diagram = assemblyDiagramInit([1,2,1])([[19.8],[4.2,21.8],[.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)
# VIEW(hpc)

toMerge = 0
diagram = assemblyDiagramInit([1,2,1])([[19.8],[4.2,21.8],[3.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)
# VIEW(hpc)

toMerge = 0
diagram = assemblyDiagramInit([1,2,1])([[19.8],[4.2,21.8],[3.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)
# VIEW(hpc)

toMerge = 1
diagram = assemblyDiagramInit([1,2,1])([[19.8],[4.2,21.8],[3.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)
# VIEW(hpc)

toMerge = 2
diagram = assemblyDiagramInit([1,2,1])([[19.8],[4.2,21.8],[3.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)
# VIEW(hpc)

toMerge = 3
diagram = assemblyDiagramInit([1,2,1])([[19.8],[4.2,21.8],[3.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)
# VIEW(hpc)

toMerge = 4
diagram = assemblyDiagramInit([1,2,1])([[19.8],[4.2,21.8],[3.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)
# VIEW(hpc)

toMerge = 5
diagram = assemblyDiagramInit([1,2,1])([[19.8],[4.2,21.8],[3.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)
# VIEW(hpc)

toMerge = 5
diagram = assemblyDiagramInit([1,2,1])([[8],[4.2,21.8],[3.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)
# VIEW(hpc)

toMerge = 5
diagram = assemblyDiagramInit([1,2,1])([[19.8],[4.2,21.8],[.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)
# VIEW(hpc)

toMerge = 5
diagram = assemblyDiagramInit([1,2,1])([[19.8],[4.2,21.8],[3.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)
# VIEW(hpc)

toMerge = 5
diagram = assemblyDiagramInit([1,2,1])([[19.8],[4.2,21.8],[.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)
# VIEW(hpc)

toMerge = 6
diagram = assemblyDiagramInit([1,2,1])([[19.8],[4.2,21.8],[.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)
# VIEW(hpc)

toMerge = 7
diagram = assemblyDiagramInit([1,2,1])([[19.8],[4.2,21.8],[.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)
# VIEW(hpc)

toMerge = 8
diagram = assemblyDiagramInit([1,2,1])([[19.8],[4.2,21.8],[.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)
# VIEW(hpc)

toMerge = 9
diagram = assemblyDiagramInit([1,2,1])([[19.8],[4.2,21.8],[.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)
# VIEW(hpc)

toMerge = 10
diagram = assemblyDiagramInit([1,2,1])([[19.8],[4.2,21.8],[.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = makeHole(master,gold)
# VIEW(hpc)

toRemove = [50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),gold,2)
# VIEW(hpc)

toMerge = 0
master = diagram2cell(apartmentRotate,master,toMerge)
hpc = makeHole(master,gold)
# VIEW(hpc)

toMerge = 0
master = diagram2cell(apartmentRotate,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 0
master = diagram2cell(apartmentRotate,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 0
master = diagram2cell(apartmentRotate,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 0
master = diagram2cell(apartmentRotate,master,toMerge)
hpc = makeHole(master,gold)
# VIEW(hpc)

toMerge = 0
master = diagram2cell(apartment,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 0
master = diagram2cell(apartment,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 0
master = diagram2cell(apartment,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 0
master = diagram2cell(apartment,master,toMerge)
hpc = makeHole(master,gold)

toMerge = 0
master = diagram2cell(apartment,master,toMerge)
hpc = makeHole(master,gold)

# VIEW(hpc)

condominium = (STRUCT(MKPOLS(master)))

stairs = makeStairs(4,10,.4)
stairs1 = MKPOLS((translatePoints(stairs[0],[21.8,6.5,0.5]),stairs[1]))
stairs2 = MKPOLS((translatePoints(stairs[0],[21.8,6.5,4.5]),stairs[1]))
stairs3 = MKPOLS((translatePoints(stairs[0],[21.8,6.5,8.5]),stairs[1]))
stairs4 = MKPOLS((translatePoints(stairs[0],[21.8,6.5,12.5]),stairs[1]))
stairs5 = MKPOLS((translatePoints(stairs[0],[21.8,6.5,16.5]),stairs[1]))
stairs = STRUCT(stairs1+stairs2+stairs3+stairs4+stairs5)

# VIEW(STRUCT([stairs,condominium]))

bars = makeBars(8,1)
bars1 = MKPOLS((translatePoints(bars[0],[19.8,26,0.5]),bars[1]))
bars2 = MKPOLS((translatePoints(bars[0],[19.8,4.2,4.5]),bars[1]))
bars3 = MKPOLS((translatePoints(bars[0],[19.8,26,8.5]),bars[1]))
bars4 = MKPOLS((translatePoints(bars[0],[19.8,4.2,8.5]),bars[1]))
bars5 = MKPOLS((translatePoints(bars[0],[19.8,26,8.5]),bars[1]))
bars6 = MKPOLS((translatePoints(bars[0],[19.8,4.2,12.5]),bars[1]))
bars7 = MKPOLS((translatePoints(bars[0],[19.8,26,12.5]),bars[1]))
bars8 = MKPOLS((translatePoints(bars[0],[19.8,4.2,16.5]),bars[1]))
bars9 = MKPOLS((translatePoints(bars[0],[19.8,26,16.5]),bars[1]))
bars10 = MKPOLS((translatePoints(bars[0],[19.8,4.2,20.5]),bars[1]))
bars11 = MKPOLS((translatePoints(bars[0],[19.8,26,20.5]),bars[1]))
bars = STRUCT(bars1+bars2+bars3+bars4+bars5+bars6+bars7+bars8+bars9+bars10+bars11)
condominium = STRUCT([condominium,stairs,bars])

# VIEW(condominium)
condominium = T([1,2])([20,25])(STRUCT([condominium,stairs,bars]))

V,CV = larCuboids([1,1,1])
V = scalePoints(V,[87.6,54.2,.3])
lawn = MKPOLS((V,CV))
lawn = COLOR(lawnColor)(STRUCT(lawn))

c1 = makeCurve([[1.96, 4.432], [-0.119, 4.181], [0.898, 1.189], [1.987, 0.875]])
c2 = makeCurve([[1.987, 0.875], [2.526, 0.922], [2.57, 1.095], [2.83, 1.065]])
c3 = makeCurve([[2.83, 1.065], [3.007, 1.168], [3.475, 0.843], [3.631, 0.883]])
c4 = makeCurve([[3.631, 0.883], [4.114, 0.858], [4.604, 1.606], [4.773, 2.137]])
c5 = makeCurve([[4.773, 2.137], [4.054, 2.42], [3.801, 3.453], [4.628, 3.97]])
c6 = makeCurve([[4.628, 3.97], [4.382, 4.385], [3.961, 4.425], [3.824, 4.441]])
c7 = makeCurve([[3.824, 4.441], [3.386, 4.501], [2.874, 4.163], [2.797, 4.224]])
c8 = makeCurve([[2.797, 4.224], [2.345, 4.284], [2.356, 4.454], [1.96, 4.432]])
c9 = makeCurve([[2.836, 4.555], [2.768, 5.206], [3.344, 5.522], [3.871, 5.606]])
c10 = makeCurve([[3.871, 5.606], [3.88, 5.321], [3.757, 4.568], [2.836, 4.555]])

apple1 = T([1,2,3])([25,8,.51])(S([1,2])([2.5,2.5])(SOLIDIFY(STRUCT([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]))))
apple2 = T(1)(25)(apple1)
apple = COLOR(green)(STRUCT([apple1,apple2]))

c1 = makeCurve([[10,10],[2.5,11],[2.49,23],[2.5,25]])
c2 = makeCurve([[2.5,25],[2.49,27],[2.5,39],[10,40]])
c3 = makeCurve([[10,40],[17.5,39],[17.51,27],[17.5,25]])
c4 = makeCurve([[17.5,25],[17.51,23],[17.5,11],[10,10]])
lake = SOLIDIFY(STRUCT([c1,c2,c3,c4]))
lake1 = T(3)(.5)(lake)
lake = T(3)(.6)(MATERIAL(water)(lake))
lake = STRUCT([lake1,lake])

V,CV = larCuboids([1,1,1])
V = translatePoints(scalePoints(V,[8,29.2,.3]),[39.8,0,.5])
sidewalk = MKPOLS((V,CV))
sidewalk = COLOR(grey)(STRUCT(sidewalk))

tree1 = makeTree([80,5])([1,10])
tree2 = makeTree([80,18])([1,11.6])
tree3 = makeTree([80,31])([1,13.2])
tree4 = makeTree([80,44])([1,15])
tree = STRUCT([tree1,tree2,tree3,tree4])

VIEW(STRUCT([condominium,apple,lawn,sidewalk,lake,tree]))