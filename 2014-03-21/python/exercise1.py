from pyplasm import *
BLU= (Color4f([0.94,0.97,1,1]))
perimetro_x = QUOTE([33])
perimetro_y = QUOTE([33])
perimetro = COLOR(Color4f([1,1,0.5,1]))(PROD([perimetro_x,perimetro_y]))
#floor 0

lati_x1 = QUOTE([-7.7,0.3])
lati_y1 = QUOTE([33])
lati1 = PROD([lati_x1,lati_y1])
lati_x2 = QUOTE([8])
lati_y2 = QUOTE([-5.2,0.3]*6)
lati2 = PROD([lati_x2,lati_y2])
lati = COLOR(BLU)(STRUCT([lati1,lati2,T(1)(17)(lati1), T(1)(25)(lati2)]))
ingresso_x1 = QUOTE([-9.7,0.3,-13,0.3])
ingresso_y1 = QUOTE([2])
ingresso1 = PROD([ingresso_x1,ingresso_y1])
ingresso_x2 = QUOTE([-9.7,13.6])
ingresso_y2 = QUOTE([-1.7,0.3])
ingresso2 = PROD([ingresso_x2,ingresso_y2])
ingresso = COLOR(BLU)(STRUCT([ingresso1,ingresso2]))
floor0 = STRUCT([perimetro,lati,ingresso])

#floor 1

tetto_x = QUOTE([-10,13])
tetto_y = QUOTE([-12,13])
tetto = COLOR(Color4f([1,0.5,0,1.0]))(PROD([tetto_x,tetto_y]))
latoOvest_x1 = QUOTE([-24.7,0.3])
latoOvest_y1 = QUOTE([33])
latoOvest1 = PROD([latoOvest_x1,latoOvest_y1])
latoOvest_x2 = QUOTE([-24.7,8.3])
latoOvest_y2 = QUOTE([-4.4,0.3]*6)
latoOvest2 = PROD([latoOvest_x2,latoOvest_y2])
latoOvest = COLOR(BLU)(STRUCT([latoOvest1,latoOvest2]))
latoSud_x1 = QUOTE([-7.4,0.3]*3)
latoSud_y1 = QUOTE([8])
latoSud1 = PROD([latoSud_x1,latoSud_y1])
latoSud_x2 = QUOTE([23])
latoSud_y2 = QUOTE([-7.7,0.3])
latoSud2 = PROD([latoSud_x2,latoSud_y2])
latoSud = COLOR(BLU)(STRUCT([latoSud1,latoSud2]))
latoNord_x1 = QUOTE([-5.95,0.3]*4)
latoNord_y1 = QUOTE([-27.9,5.1])
latoNord1 = PROD([latoNord_x1,latoNord_y1])
latoNord_x2 = QUOTE([25])
latoNord_y2 = QUOTE([-27.9,0.3])
latoNord2 = PROD([latoNord_x2,latoNord_y2])
latoNord = COLOR(BLU)(STRUCT([latoNord1,latoNord2]))
floor1 = STRUCT([perimetro,tetto,latoOvest,latoSud,latoNord])

#floor 2

perimetro2 = COLOR(Color4f([1,1,0.5,1]))(DIFF([perimetro,tetto]))
floor2 = STRUCT([perimetro2,latoSud,latoOvest,latoNord])
#VIEW(floor2)

#floor 3
latoSud_x1 = QUOTE([-11.2,0.3]*2)
latoSud_y1 = QUOTE([8])
latoSud1 = PROD([latoSud_x1,latoSud_y1])
latoSud_x2 = QUOTE([23])
latoSud_y2 = QUOTE([-7.7,0.3])
latoSud2 = PROD([latoSud_x2,latoSud_y2])
latoSud = COLOR(BLU)(STRUCT([latoSud1,latoSud2]))
latoEst_x1 = QUOTE([10])
latoEst_y1 = QUOTE([-22.7,0.3])
latoEst1 = PROD([latoEst_x1,latoEst_y1])
latoEst_x2 = QUOTE([-4.7,0.3]*2)
latoEst_y2 = QUOTE([-23,10])
latoEst2 = PROD([latoEst_x2,latoEst_y2])
latoEst = COLOR(BLU)(STRUCT([latoEst1,latoEst2,T(2)(5)(latoEst1)]))
floor3 = STRUCT([perimetro2,latoOvest,latoSud,latoEst])

floor1_2P5D = T(3)(4.125)(floor1)
floor2_2P5D = T(3)(8.25)(floor2)
floor3_2P5D = T(3)(12.375)(floor3)
two_and_half_model = STRUCT([floor0,floor1_2P5D,floor2_2P5D,floor3_2P5D])
VIEW(two_and_half_model)
