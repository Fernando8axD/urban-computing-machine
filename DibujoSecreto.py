# Created by: Fernando Ochoa V.

from tkinter import *
import random

pares = []      #LISTA PARA ALMACENAR LOS NUMEROS PARES
impares = []    #LISTA PARA ALMACENAR LOS NUMEROS IMPARES

############################################
#FUNCIONES PARA CAMBIAR COLOR DE CADA BOTON
############################################

def Change_Color_19():
    but19.config(background="black", foreground="white")

def Change_Color_21():
    but21.config(background="black", foreground="white")

def Change_Color_29():
    but29.config(background="black", foreground="white")

def Change_Color_32():
    but32.config(background="black", foreground="white")

def Change_Color_34():
    but34.config(background="black", foreground="white")

def Change_Color_37():
    but37.config(background="black", foreground="white")

def Change_Color_41():
    but41.config(background="black", foreground="white")

def Change_Color_45():
    but45.config(background="black", foreground="white")

def Change_Color_46():
    but46.config(background="black", foreground="white")

def Change_Color_47():
    but47.config(background="black", foreground="white")

def Change_Color_51():
    but51.config(background="black", foreground="white")

def Change_Color_53():
    but53.config(background="black", foreground="white")

def Change_Color_54():
    but54.config(background="black", foreground="white")

def Change_Color_55():
    but55.config(background="black", foreground="white")

def Change_Color_58():
    but58.config(background="black", foreground="white")

def Change_Color_59():
    but59.config(background="black", foreground="white")

def Change_Color_60():
    but60.config(background="black", foreground="white")

def Change_Color_63():
    but63.config(background="black", foreground="white")

def Change_Color_64():
    but64.config(background="black", foreground="white")

def Change_Color_65():
    but65.config(background="black", foreground="white")

def Change_Color_66():
    but66.config(background="black", foreground="white")

def Change_Color_67():
    but67.config(background="black", foreground="white")

def Change_Color_68():
    but68.config(background="black", foreground="white")

def Change_Color_69():
    but69.config(background="black", foreground="white")

def Change_Color_70():
    but70.config(background="black", foreground="white")

def Change_Color_71():
    but71.config(background="black", foreground="white")

def Change_Color_72():
    but72.config(background="black", foreground="white")

def Change_Color_73():
    but73.config(background="black", foreground="white")

def Change_Color_74():
    but74.config(background="black", foreground="white")

def Change_Color_75():
    but75.config(background="black", foreground="white")

def Change_Color_76():
    but76.config(background="black", foreground="white")

def Change_Color_77():
    but77.config(background="black", foreground="white")

def Change_Color_78():
    but78.config(background="black", foreground="white")

def Change_Color_79():
    but79.config(background="black", foreground="white")

def Change_Color_80():
    but80.config(background="black", foreground="white")

def Change_Color_81():
    but81.config(background="black", foreground="white")

def Change_Color_82():
    but82.config(background="black", foreground="white")

def Change_Color_83():
    but83.config(background="black", foreground="white")

def Change_Color_84():
    but84.config(background="black", foreground="white")

def Change_Color_85():
    but85.config(background="black", foreground="white")

def Change_Color_86():
    but86.config(background="black", foreground="white")

def Change_Color_87():
    but87.config(background="black", foreground="white")

def Change_Color_88():
    but88.config(background="black", foreground="white")

def Change_Color_89():
    but89.config(background="black", foreground="white")

def Change_Color_90():
    but90.config(background="black", foreground="white")

def Change_Color_91():
    but91.config(background="black", foreground="white")

def Change_Color_92():
    but92.config(background="black", foreground="white")

def Change_Color_93():
    but93.config(background="black", foreground="white")

def Change_Color_94():
    but94.config(background="black", foreground="white")

def Change_Color_95():
    but95.config(background="black", foreground="white")

def Change_Color_96():
    but96.config(background="black", foreground="white")

def Change_Color_97():
    but97.config(background="black", foreground="white")

def Change_Color_98():
    but98.config(background="black", foreground="white")

def Change_Color_99():
    but99.config(background="black", foreground="white")

def Change_Color_100():
    but100.config(background="black", foreground="white")

def Change_Color_101():
    but101.config(background="black", foreground="white")

def Change_Color_102():
    but102.config(background="black", foreground="white")

def Change_Color_103():
    but103.config(background="black", foreground="white")

def Change_Color_104():
    but104.config(background="black", foreground="white")

def Change_Color_105():
    but105.config(background="black", foreground="white")

def Change_Color_106():
    but106.config(background="black", foreground="white")

def Change_Color_107():
    but107.config(background="black", foreground="white")

def Change_Color_109():
    but109.config(background="black", foreground="white")

def Change_Color_110():
    but110.config(background="black", foreground="white")

def Change_Color_111():
    but111.config(background="black", foreground="white")

def Change_Color_112():
    but112.config(background="black", foreground="white")

def Change_Color_113():
    but113.config(background="black", foreground="white")

def Change_Color_115():
    but115.config(background="black", foreground="white")

def Change_Color_116():
    but116.config(background="black", foreground="white")

def Change_Color_117():
    but117.config(background="black", foreground="white")

def Change_Color_119():
    but119.config(background="black", foreground="white")

def Change_Color_123():
    but123.config(background="black", foreground="white")

def Change_Color_124():
    but124.config(background="black", foreground="white")

def Change_Color_125():
    but125.config(background="black", foreground="white")

def Change_Color_129():
    but129.config(background="black", foreground="white")

def Change_Color_132():
    but132.config(background="black", foreground="white")

def Change_Color_137():
    but137.config(background="black", foreground="white")

def Change_Color_142():
    but142.config(background="black", foreground="white")

def Change_Color_143():
    but143.config(background="black", foreground="white")

def Change_Color_146():
    but146.config(background="black", foreground="white")

def Change_Color_150():
    but150.config(background="black", foreground="white")

def Change_Color_154():
    but154.config(background="black", foreground="white")

#####################################
#FUNCIONES DE LOS INTENTOS DEL JUEGO
#####################################

def Reset():
    
    Eliminador()
    Generador()

    but1.config(background="white", foreground="black", text=pares[0],command=Reset_2)
    but2.config(background="white", foreground="black", text=pares[1],command=Reset_2)
    but3.config(background="white", foreground="black", text=pares[2],command=Reset_2)
    but4.config(background="white", foreground="black", text=pares[3],command=Reset_2)
    but5.config(background="white", foreground="black", text=pares[4],command=Reset_2)
    but6.config(background="white", foreground="black", text=pares[5],command=Reset_2)
    but7.config(background="white", foreground="black", text=pares[6],command=Reset_2)
    but8.config(background="white", foreground="black", text=pares[7],command=Reset_2)
    but9.config(background="white", foreground="black", text=pares[8],command=Reset_2)
    but10.config(background="white", foreground="black", text=pares[9],command=Reset_2)
    but11.config(background="white", foreground="black", text=pares[10],command=Reset_2)
    but12.config(background="white", foreground="black", text=pares[11],command=Reset_2)
    but13.config(background="white", foreground="black", text=pares[12],command=Reset_2)
    but14.config(background="white", foreground="black", text=pares[13],command=Reset_2)
    but15.config(background="white", foreground="black", text=pares[14],command=Reset_2)
    but16.config(background="white", foreground="black", text=pares[15],command=Reset_2)
    but17.config(background="white", foreground="black", text=pares[16],command=Reset_2)
    but18.config(background="white", foreground="black", text=pares[17],command=Reset_2)
    but19.config(background="white", foreground="black", text=impares[18],command=Change_Color_19)
    but20.config(background="white", foreground="black", text=pares[19],command=Reset_2)
    but21.config(background="white", foreground="black", text=impares[20],command=Change_Color_21)
    but22.config(background="white", foreground="black", text=pares[21],command=Reset_2)
    but23.config(background="white", foreground="black", text=pares[22],command=Reset_2)
    but24.config(background="white", foreground="black", text=pares[23],command=Reset_2)
    but25.config(background="white", foreground="black", text=pares[24],command=Reset_2)
    but26.config(background="white", foreground="black", text=pares[25],command=Reset_2)
    but27.config(background="white", foreground="black", text=pares[26],command=Reset_2)
    but28.config(background="white", foreground="black", text=pares[27],command=Reset_2)
    but29.config(background="white", foreground="black", text=impares[28],command=Change_Color_29)
    but30.config(background="white", foreground="black", text=pares[29],command=Reset_2)
    but31.config(background="white", foreground="black", text=pares[30],command=Reset_2)
    but32.config(background="white", foreground="black", text=impares[31],command=Change_Color_32)
    but33.config(background="white", foreground="black", text=pares[32],command=Reset_2)
    but34.config(background="white", foreground="black", text=impares[33],command=Change_Color_34)
    but35.config(background="white", foreground="black", text=pares[34],command=Reset_2)
    but36.config(background="white", foreground="black", text=pares[35],command=Reset_2)
    but37.config(background="white", foreground="black", text=impares[36],command=Change_Color_37)
    but38.config(background="white", foreground="black", text=pares[37],command=Reset_2)
    but39.config(background="white", foreground="black", text=pares[38],command=Reset_2)
    but40.config(background="white", foreground="black", text=pares[39],command=Reset_2)
    but41.config(background="white", foreground="black", text=impares[40],command=Change_Color_41)
    but42.config(background="white", foreground="black", text=pares[41],command=Reset_2)
    but43.config(background="white", foreground="black", text=pares[42],command=Reset_2)
    but44.config(background="white", foreground="black", text=pares[43],command=Reset_2)
    but45.config(background="white", foreground="black", text=impares[44],command=Change_Color_45)
    but46.config(background="white", foreground="black", text=impares[45],command=Change_Color_46)
    but47.config(background="white", foreground="black", text=impares[46],command=Change_Color_47)
    but48.config(background="white", foreground="black", text=pares[47],command=Reset_2)
    but49.config(background="white", foreground="black", text=pares[48],command=Reset_2)
    but50.config(background="white", foreground="black", text=pares[49],command=Reset_2)
    but51.config(background="white", foreground="black", text=impares[50],command=Change_Color_51)
    but52.config(background="white", foreground="black", text=pares[51],command=Reset_2)
    but53.config(background="white", foreground="black", text=impares[52],command=Change_Color_53)
    but54.config(background="white", foreground="black", text=impares[53],command=Change_Color_54)
    but55.config(background="white", foreground="black", text=impares[54],command=Change_Color_55)
    but56.config(background="white", foreground="black", text=pares[55],command=Reset_2)
    but57.config(background="white", foreground="black", text=pares[56],command=Reset_2)
    but58.config(background="white", foreground="black", text=impares[57],command=Change_Color_58)
    but59.config(background="white", foreground="black", text=impares[58],command=Change_Color_59)
    but60.config(background="white", foreground="black", text=impares[59],command=Change_Color_60)
    but61.config(background="white", foreground="black", text=pares[60],command=Reset_2)
    but62.config(background="white", foreground="black", text=pares[61],command=Reset_2)
    but63.config(background="white", foreground="black", text=impares[62],command=Change_Color_63)
    but64.config(background="white", foreground="black", text=impares[63],command=Change_Color_64)
    but65.config(background="white", foreground="black", text=impares[64],command=Change_Color_65)
    but66.config(background="white", foreground="black", text=impares[65],command=Change_Color_66)
    but67.config(background="white", foreground="black", text=impares[66],command=Change_Color_67)
    but68.config(background="white", foreground="black", text=impares[67],command=Change_Color_68)
    but69.config(background="white", foreground="black", text=impares[68],command=Change_Color_69)
    but70.config(background="white", foreground="black", text=impares[69],command=Change_Color_70)
    but71.config(background="white", foreground="black", text=impares[70],command=Change_Color_71)
    but72.config(background="white", foreground="black", text=impares[71],command=Change_Color_72)
    but73.config(background="white", foreground="black", text=impares[72],command=Change_Color_73)
    but74.config(background="white", foreground="black", text=impares[73],command=Change_Color_74)
    but75.config(background="white", foreground="black", text=impares[74],command=Change_Color_75)
    but76.config(background="white", foreground="black", text=impares[75],command=Change_Color_76)
    but77.config(background="white", foreground="black", text=impares[76],command=Change_Color_77)
    but78.config(background="white", foreground="black", text=impares[77],command=Change_Color_78)
    but79.config(background="white", foreground="black", text=impares[78],command=Change_Color_79)
    but80.config(background="white", foreground="black", text=impares[79],command=Change_Color_80)
    but81.config(background="white", foreground="black", text=impares[80],command=Change_Color_81)
    but82.config(background="white", foreground="black", text=impares[81],command=Change_Color_82)
    but83.config(background="white", foreground="black", text=impares[82],command=Change_Color_83)
    but84.config(background="white", foreground="black", text=impares[83],command=Change_Color_84)
    but85.config(background="white", foreground="black", text=impares[84],command=Change_Color_85)
    but86.config(background="white", foreground="black", text=impares[85],command=Change_Color_86)
    but87.config(background="white", foreground="black", text=impares[86],command=Change_Color_87)
    but88.config(background="white", foreground="black", text=impares[87],command=Change_Color_88)
    but89.config(background="white", foreground="black", text=impares[88],command=Change_Color_89)
    but90.config(background="white", foreground="black", text=impares[89],command=Change_Color_90)
    but91.config(background="white", foreground="black", text=impares[90],command=Change_Color_91)
    but92.config(background="white", foreground="black", text=impares[91],command=Change_Color_92)
    but93.config(background="white", foreground="black", text=impares[92],command=Change_Color_93)
    but94.config(background="white", foreground="black", text=impares[93],command=Change_Color_94)
    but95.config(background="white", foreground="black", text=impares[94],command=Change_Color_95)
    but96.config(background="white", foreground="black", text=impares[95],command=Change_Color_96)
    but97.config(background="white", foreground="black", text=impares[96],command=Change_Color_97)
    but98.config(background="white", foreground="black", text=impares[97],command=Change_Color_98)
    but99.config(background="white", foreground="black", text=impares[98],command=Change_Color_99)
    but100.config(background="white", foreground="black", text=impares[99],command=Change_Color_100)
    but101.config(background="white", foreground="black", text=impares[100],command=Change_Color_101)
    but102.config(background="white", foreground="black", text=impares[101],command=Change_Color_102)
    but103.config(background="white", foreground="black", text=impares[102],command=Change_Color_103)
    but104.config(background="white", foreground="black", text=impares[103],command=Change_Color_104)
    but105.config(background="white", foreground="black", text=impares[104],command=Change_Color_105)
    but106.config(background="white", foreground="black", text=impares[105],command=Change_Color_106)
    but107.config(background="white", foreground="black", text=impares[106],command=Change_Color_107)
    but108.config(background="white", foreground="black", text=pares[107],command=Reset_2)
    but109.config(background="white", foreground="black", text=impares[108],command=Change_Color_109)
    but110.config(background="white", foreground="black", text=impares[109],command=Change_Color_110)
    but111.config(background="white", foreground="black", text=impares[110],command=Change_Color_111)
    but112.config(background="white", foreground="black", text=impares[111],command=Change_Color_112)
    but113.config(background="white", foreground="black", text=impares[112],command=Change_Color_113)
    but114.config(background="white", foreground="black", text=pares[113],command=Reset_2)
    but115.config(background="white", foreground="black", text=impares[114],command=Change_Color_115)
    but116.config(background="white", foreground="black", text=impares[115],command=Change_Color_116)
    but117.config(background="white", foreground="black", text=impares[116],command=Change_Color_117)
    but118.config(background="white", foreground="black", text=pares[117],command=Reset_2)
    but119.config(background="white", foreground="black", text=impares[118],command=Change_Color_119)
    but120.config(background="white", foreground="black", text=pares[119],command=Reset_2)
    but121.config(background="white", foreground="black", text=pares[120],command=Reset_2)
    but122.config(background="white", foreground="black", text=pares[121],command=Reset_2)
    but123.config(background="white", foreground="black", text=impares[122],command=Change_Color_123)
    but124.config(background="white", foreground="black", text=impares[123],command=Change_Color_124)
    but125.config(background="white", foreground="black", text=impares[124],command=Change_Color_125)
    but126.config(background="white", foreground="black", text=pares[125],command=Reset_2)
    but127.config(background="white", foreground="black", text=pares[126],command=Reset_2)
    but128.config(background="white", foreground="black", text=pares[127],command=Reset_2)
    but129.config(background="white", foreground="black", text=impares[128],command=Change_Color_129)
    but130.config(background="white", foreground="black", text=pares[129],command=Reset_2)
    but131.config(background="white", foreground="black", text=pares[130],command=Reset_2)
    but132.config(background="white", foreground="black", text=impares[131],command=Change_Color_132)
    but133.config(background="white", foreground="black", text=pares[132],command=Reset_2)
    but134.config(background="white", foreground="black", text=pares[133],command=Reset_2)
    but135.config(background="white", foreground="black", text=pares[134],command=Reset_2)
    but136.config(background="white", foreground="black", text=pares[135],command=Reset_2)
    but137.config(background="white", foreground="black", text=impares[136],command=Change_Color_137)
    but138.config(background="white", foreground="black", text=pares[137],command=Reset_2)
    but139.config(background="white", foreground="black", text=pares[138],command=Reset_2)
    but140.config(background="white", foreground="black", text=pares[139],command=Reset_2)
    but141.config(background="white", foreground="black", text=pares[140],command=Reset_2)
    but142.config(background="white", foreground="black", text=impares[141],command=Change_Color_142)
    but143.config(background="white", foreground="black", text=pares[142],command=Reset_2)
    but144.config(background="white", foreground="black", text=pares[143],command=Reset_2)
    but145.config(background="white", foreground="black", text=pares[144],command=Reset_2)
    but146.config(background="white", foreground="black", text=impares[145],command=Change_Color_146)
    but147.config(background="white", foreground="black", text=pares[146],command=Reset_2)
    but148.config(background="white", foreground="black", text=pares[147],command=Reset_2)
    but149.config(background="white", foreground="black", text=pares[148],command=Reset_2)
    but150.config(background="white", foreground="black", text=impares[149],command=Change_Color_150)
    but151.config(background="white", foreground="black", text=pares[150],command=Reset_2)
    but152.config(background="white", foreground="black", text=pares[151],command=Reset_2)
    but153.config(background="white", foreground="black", text=pares[152],command=Reset_2)
    but154.config(background="white", foreground="black", text=impares[153],command=Change_Color_154)
    but155.config(background="white", foreground="black", text=pares[154],command=Reset_2)
    but156.config(background="white", foreground="black", text=pares[155],command=Reset_2)
    but157.config(background="white", foreground="black", text=pares[156],command=Reset_2)
    but158.config(background="white", foreground="black", text=pares[157],command=Reset_2)
    but159.config(background="white", foreground="black", text=pares[158],command=Reset_2)
    but160.config(background="white", foreground="black", text=pares[159],command=Reset_2)
    but161.config(background="white", foreground="black", text=pares[160],command=Reset_2)
    but162.config(background="white", foreground="black", text=pares[161],command=Reset_2)
    but163.config(background="white", foreground="black", text=pares[162],command=Reset_2)
    but164.config(background="white", foreground="black", text=pares[163],command=Reset_2)
    but165.config(background="white", foreground="black", text=pares[164],command=Reset_2)
    but166.config(background="white", foreground="black", text=pares[165],command=Reset_2)
    but167.config(background="white", foreground="black", text=pares[166],command=Reset_2)
    but168.config(background="white", foreground="black", text=pares[167],command=Reset_2)
    but169.config(background="white", foreground="black", text=pares[168],command=Reset_2)

def Reset_2():

    Eliminador()
    Generador()

    but1.config(background="white", foreground="black", text=pares[0],command=Reset)
    but2.config(background="white", foreground="black", text=pares[1],command=Reset)
    but3.config(background="white", foreground="black", text=pares[2],command=Reset)
    but4.config(background="white", foreground="black", text=pares[3],command=Reset)
    but5.config(background="white", foreground="black", text=pares[4],command=Reset)
    but6.config(background="white", foreground="black", text=pares[5],command=Reset)
    but7.config(background="white", foreground="black", text=pares[6],command=Reset)
    but8.config(background="white", foreground="black", text=pares[7],command=Reset)
    but9.config(background="white", foreground="black", text=pares[8],command=Reset)
    but10.config(background="white", foreground="black", text=pares[9],command=Reset)
    but11.config(background="white", foreground="black", text=pares[10],command=Reset)
    but12.config(background="white", foreground="black", text=pares[11],command=Reset)
    but13.config(background="white", foreground="black", text=pares[12],command=Reset)
    but14.config(background="white", foreground="black", text=pares[13],command=Reset)
    but15.config(background="white", foreground="black", text=pares[14],command=Reset)
    but16.config(background="white", foreground="black", text=pares[15],command=Reset)
    but17.config(background="white", foreground="black", text=pares[16],command=Reset)
    but18.config(background="white", foreground="black", text=pares[17],command=Reset)
    but19.config(background="white", foreground="black", text=impares[18],command=Change_Color_19)
    but20.config(background="white", foreground="black", text=pares[19],command=Reset)
    but21.config(background="white", foreground="black", text=impares[20],command=Change_Color_21)
    but22.config(background="white", foreground="black", text=pares[21],command=Reset)
    but23.config(background="white", foreground="black", text=pares[22],command=Reset)
    but24.config(background="white", foreground="black", text=pares[23],command=Reset)
    but25.config(background="white", foreground="black", text=pares[24],command=Reset)
    but26.config(background="white", foreground="black", text=pares[25],command=Reset)
    but27.config(background="white", foreground="black", text=pares[26],command=Reset)
    but28.config(background="white", foreground="black", text=pares[27],command=Reset)
    but29.config(background="white", foreground="black", text=impares[28],command=Change_Color_29)
    but30.config(background="white", foreground="black", text=pares[29],command=Reset)
    but31.config(background="white", foreground="black", text=pares[30],command=Reset)
    but32.config(background="white", foreground="black", text=impares[31],command=Change_Color_32)
    but33.config(background="white", foreground="black", text=pares[32],command=Reset)
    but34.config(background="white", foreground="black", text=impares[33],command=Change_Color_34)
    but35.config(background="white", foreground="black", text=pares[34],command=Reset)
    but36.config(background="white", foreground="black", text=pares[35],command=Reset)
    but37.config(background="white", foreground="black", text=impares[36],command=Change_Color_37)
    but38.config(background="white", foreground="black", text=pares[37],command=Reset)
    but39.config(background="white", foreground="black", text=pares[38],command=Reset)
    but40.config(background="white", foreground="black", text=pares[39],command=Reset)
    but41.config(background="white", foreground="black", text=impares[40],command=Change_Color_41)
    but42.config(background="white", foreground="black", text=pares[41],command=Reset)
    but43.config(background="white", foreground="black", text=pares[42],command=Reset)
    but44.config(background="white", foreground="black", text=pares[43],command=Reset)
    but45.config(background="white", foreground="black", text=impares[44],command=Change_Color_45)
    but46.config(background="white", foreground="black", text=impares[45],command=Change_Color_46)
    but47.config(background="white", foreground="black", text=impares[46],command=Change_Color_47)
    but48.config(background="white", foreground="black", text=pares[47],command=Reset)
    but49.config(background="white", foreground="black", text=pares[48],command=Reset)
    but50.config(background="white", foreground="black", text=pares[49],command=Reset)
    but51.config(background="white", foreground="black", text=impares[50],command=Change_Color_51)
    but52.config(background="white", foreground="black", text=pares[51],command=Reset)
    but53.config(background="white", foreground="black", text=impares[52],command=Change_Color_53)
    but54.config(background="white", foreground="black", text=impares[53],command=Change_Color_54)
    but55.config(background="white", foreground="black", text=impares[54],command=Change_Color_55)
    but56.config(background="white", foreground="black", text=pares[55],command=Reset)
    but57.config(background="white", foreground="black", text=pares[56],command=Reset)
    but58.config(background="white", foreground="black", text=impares[57],command=Change_Color_58)
    but59.config(background="white", foreground="black", text=impares[58],command=Change_Color_59)
    but60.config(background="white", foreground="black", text=impares[59],command=Change_Color_60)
    but61.config(background="white", foreground="black", text=pares[60],command=Reset)
    but62.config(background="white", foreground="black", text=pares[61],command=Reset)
    but63.config(background="white", foreground="black", text=impares[62],command=Change_Color_63)
    but64.config(background="white", foreground="black", text=impares[63],command=Change_Color_64)
    but65.config(background="white", foreground="black", text=impares[64],command=Change_Color_65)
    but66.config(background="white", foreground="black", text=impares[65],command=Change_Color_66)
    but67.config(background="white", foreground="black", text=impares[66],command=Change_Color_67)
    but68.config(background="white", foreground="black", text=impares[67],command=Change_Color_68)
    but69.config(background="white", foreground="black", text=impares[68],command=Change_Color_69)
    but70.config(background="white", foreground="black", text=impares[69],command=Change_Color_70)
    but71.config(background="white", foreground="black", text=impares[70],command=Change_Color_71)
    but72.config(background="white", foreground="black", text=impares[71],command=Change_Color_72)
    but73.config(background="white", foreground="black", text=impares[72],command=Change_Color_73)
    but74.config(background="white", foreground="black", text=impares[73],command=Change_Color_74)
    but75.config(background="white", foreground="black", text=impares[74],command=Change_Color_75)
    but76.config(background="white", foreground="black", text=impares[75],command=Change_Color_76)
    but77.config(background="white", foreground="black", text=impares[76],command=Change_Color_77)
    but78.config(background="white", foreground="black", text=impares[77],command=Change_Color_78)
    but79.config(background="white", foreground="black", text=impares[78],command=Change_Color_79)
    but80.config(background="white", foreground="black", text=impares[79],command=Change_Color_80)
    but81.config(background="white", foreground="black", text=impares[80],command=Change_Color_81)
    but82.config(background="white", foreground="black", text=impares[81],command=Change_Color_82)
    but83.config(background="white", foreground="black", text=impares[82],command=Change_Color_83)
    but84.config(background="white", foreground="black", text=impares[83],command=Change_Color_84)
    but85.config(background="white", foreground="black", text=impares[84],command=Change_Color_85)
    but86.config(background="white", foreground="black", text=impares[85],command=Change_Color_86)
    but87.config(background="white", foreground="black", text=impares[86],command=Change_Color_87)
    but88.config(background="white", foreground="black", text=impares[87],command=Change_Color_88)
    but89.config(background="white", foreground="black", text=impares[88],command=Change_Color_89)
    but90.config(background="white", foreground="black", text=impares[89],command=Change_Color_90)
    but91.config(background="white", foreground="black", text=impares[90],command=Change_Color_91)
    but92.config(background="white", foreground="black", text=impares[91],command=Change_Color_92)
    but93.config(background="white", foreground="black", text=impares[92],command=Change_Color_93)
    but94.config(background="white", foreground="black", text=impares[93],command=Change_Color_94)
    but95.config(background="white", foreground="black", text=impares[94],command=Change_Color_95)
    but96.config(background="white", foreground="black", text=impares[95],command=Change_Color_96)
    but97.config(background="white", foreground="black", text=impares[96],command=Change_Color_97)
    but98.config(background="white", foreground="black", text=impares[97],command=Change_Color_98)
    but99.config(background="white", foreground="black", text=impares[98],command=Change_Color_99)
    but100.config(background="white", foreground="black", text=impares[99],command=Change_Color_100)
    but101.config(background="white", foreground="black", text=impares[100],command=Change_Color_101)
    but102.config(background="white", foreground="black", text=impares[101],command=Change_Color_102)
    but103.config(background="white", foreground="black", text=impares[102],command=Change_Color_103)
    but104.config(background="white", foreground="black", text=impares[103],command=Change_Color_104)
    but105.config(background="white", foreground="black", text=impares[104],command=Change_Color_105)
    but106.config(background="white", foreground="black", text=impares[105],command=Change_Color_106)
    but107.config(background="white", foreground="black", text=impares[106],command=Change_Color_107)
    but108.config(background="white", foreground="black", text=pares[107],command=Reset)
    but109.config(background="white", foreground="black", text=impares[108],command=Change_Color_109)
    but110.config(background="white", foreground="black", text=impares[109],command=Change_Color_110)
    but111.config(background="white", foreground="black", text=impares[110],command=Change_Color_111)
    but112.config(background="white", foreground="black", text=impares[111],command=Change_Color_112)
    but113.config(background="white", foreground="black", text=impares[112],command=Change_Color_113)
    but114.config(background="white", foreground="black", text=pares[113],command=Reset)
    but115.config(background="white", foreground="black", text=impares[114],command=Change_Color_115)
    but116.config(background="white", foreground="black", text=impares[115],command=Change_Color_116)
    but117.config(background="white", foreground="black", text=impares[116],command=Change_Color_117)
    but118.config(background="white", foreground="black", text=pares[117],command=Reset)
    but119.config(background="white", foreground="black", text=impares[118],command=Change_Color_119)
    but120.config(background="white", foreground="black", text=pares[119],command=Reset)
    but121.config(background="white", foreground="black", text=pares[120],command=Reset)
    but122.config(background="white", foreground="black", text=pares[121],command=Reset)
    but123.config(background="white", foreground="black", text=impares[122],command=Change_Color_123)
    but124.config(background="white", foreground="black", text=impares[123],command=Change_Color_124)
    but125.config(background="white", foreground="black", text=impares[124],command=Change_Color_125)
    but126.config(background="white", foreground="black", text=pares[125],command=Reset)
    but127.config(background="white", foreground="black", text=pares[126],command=Reset)
    but128.config(background="white", foreground="black", text=pares[127],command=Reset)
    but129.config(background="white", foreground="black", text=impares[128],command=Change_Color_129)
    but130.config(background="white", foreground="black", text=pares[129],command=Reset)
    but131.config(background="white", foreground="black", text=pares[130],command=Reset)
    but132.config(background="white", foreground="black", text=impares[131],command=Change_Color_132)
    but133.config(background="white", foreground="black", text=pares[132],command=Reset)
    but134.config(background="white", foreground="black", text=pares[133],command=Reset)
    but135.config(background="white", foreground="black", text=pares[134],command=Reset)
    but136.config(background="white", foreground="black", text=pares[135],command=Reset)
    but137.config(background="white", foreground="black", text=impares[136],command=Change_Color_137)
    but138.config(background="white", foreground="black", text=pares[137],command=Reset)
    but139.config(background="white", foreground="black", text=pares[138],command=Reset)
    but140.config(background="white", foreground="black", text=pares[139],command=Reset)
    but141.config(background="white", foreground="black", text=pares[140],command=Reset)
    but142.config(background="white", foreground="black", text=impares[141],command=Change_Color_142)
    but143.config(background="white", foreground="black", text=pares[142],command=Reset)
    but144.config(background="white", foreground="black", text=pares[143],command=Reset)
    but145.config(background="white", foreground="black", text=pares[144],command=Reset)
    but146.config(background="white", foreground="black", text=impares[145],command=Change_Color_146)
    but147.config(background="white", foreground="black", text=pares[146],command=Reset)
    but148.config(background="white", foreground="black", text=pares[147],command=Reset)
    but149.config(background="white", foreground="black", text=pares[148],command=Reset)
    but150.config(background="white", foreground="black", text=impares[149],command=Change_Color_150)
    but151.config(background="white", foreground="black", text=pares[150],command=Reset)
    but152.config(background="white", foreground="black", text=pares[151],command=Reset)
    but153.config(background="white", foreground="black", text=pares[152],command=Reset)
    but154.config(background="white", foreground="black", text=impares[153],command=Change_Color_154)
    but155.config(background="white", foreground="black", text=pares[154],command=Reset)
    but156.config(background="white", foreground="black", text=pares[155],command=Reset)
    but157.config(background="white", foreground="black", text=pares[156],command=Reset)
    but158.config(background="white", foreground="black", text=pares[157],command=Reset)
    but159.config(background="white", foreground="black", text=pares[158],command=Reset)
    but160.config(background="white", foreground="black", text=pares[159],command=Reset)
    but161.config(background="white", foreground="black", text=pares[160],command=Reset)
    but162.config(background="white", foreground="black", text=pares[161],command=Reset)
    but163.config(background="white", foreground="black", text=pares[162],command=Reset)
    but164.config(background="white", foreground="black", text=pares[163],command=Reset)
    but165.config(background="white", foreground="black", text=pares[164],command=Reset)
    but166.config(background="white", foreground="black", text=pares[165],command=Reset)
    but167.config(background="white", foreground="black", text=pares[166],command=Reset)
    but168.config(background="white", foreground="black", text=pares[167],command=Reset)
    but169.config(background="white", foreground="black", text=pares[168],command=Reset)

#################################
#GENERADOR DE VALORES ALEATORIOS
#################################

def Generador():
        
    n = 0

    while n < 2000:
        valor = random.randint(1,99)   #ALMACENA UN VALOR RANDOM ENTRE 1 Y 100

        if valor % 2 == 0:              #VERIFICA SI ES PAR Y LO ALMACENA EN LA
            pares.append(str(valor))    #LISTA CORRESPONDIENTE

        else:                           #SI NO ES PAR, LO ALMACENA EN LA LISTA
            impares.append(str(valor))  #DE IMPARES
        
        n+=1                            #SUMA 1 PARA CONTINUAR CON LAS ITERACIONES

##################################
#ELIMINADOR DE VALORES ALEATORIOS
##################################

def Eliminador():

    pares.clear()
    impares.clear()

########################################
#VENTANA PRINCIPAL DE MATRIZ DE BOTONES
########################################
                                                   
root = Tk()
root.title("Dibujo secreto")
root.iconbitmap("batman.ico")
root.resizable(0, 0)

#####################################################
###################### FILA 1 #######################
#####################################################

Generador()

but1 = Button(root, text=pares[0], command=Reset)
but1.config(background="white", foreground="black", width=4, height=2)
but1.grid(row=0, column=0)

but2 = Button(root, text=pares[1], command=Reset)
but2.config(background="white", foreground="black", width=4, height=2)
but2.grid(row=0, column=1)

but3 = Button(root, text=pares[2], command=Reset)
but3.config(background="white", foreground="black", width=4, height=2)
but3.grid(row=0, column=2)

but4 = Button(root, text=pares[3], command=Reset)
but4.config(background="white", foreground="black", width=4, height=2)
but4.grid(row=0, column=3)

but5 = Button(root, text=pares[4], command=Reset)
but5.config(background="white", foreground="black", width=4, height=2)
but5.grid(row=0, column=4)

but6 = Button(root, text=pares[5], command=Reset)
but6.config(background="white", foreground="black", width=4, height=2)
but6.grid(row=0, column=5)

but7 = Button(root, text=pares[6], command=Reset)
but7.config(background="white", foreground="black", width=4, height=2)
but7.grid(row=0, column=6)

but8 = Button(root, text=pares[7], command=Reset)
but8.config(background="white", foreground="black", width=4, height=2)
but8.grid(row=0, column=7)

but9 = Button(root, text=pares[8], command=Reset)
but9.config(background="white", foreground="black", width=4, height=2)
but9.grid(row=0, column=8)

but10 = Button(root, text=pares[9], command=Reset)
but10.config(background="white", foreground="black", width=4, height=2)
but10.grid(row=0, column=9)

but11 = Button(root, text=pares[10], command=Reset)
but11.config(background="white", foreground="black", width=4, height=2)
but11.grid(row=0, column=10)

but12 = Button(root, text=pares[11], command=Reset)
but12.config(background="white", foreground="black", width=4, height=2)
but12.grid(row=0, column=11)

but13 = Button(root, text=pares[12], command=Reset)
but13.config(background="white", foreground="black", width=4, height=2)
but13.grid(row=0, column=12)

#####################################################
###################### FILA 2 #######################
#####################################################

but14 = Button(root, text=pares[13], command=Reset)
but14.config(background="white", foreground="black", width=4, height=2)
but14.grid(row=1, column=0)

but15 = Button(root, text=pares[14], command=Reset)
but15.config(background="white", foreground="black", width=4, height=2)
but15.grid(row=1, column=1)

but16 = Button(root, text=pares[15], command=Reset)
but16.config(background="white", foreground="black", width=4, height=2)
but16.grid(row=1, column=2)

but17 = Button(root, text=pares[16], command=Reset)
but17.config(background="white", foreground="black", width=4, height=2)
but17.grid(row=1, column=3)

but18 = Button(root, text=pares[17], command=Reset)
but18.config(background="white", foreground="black", width=4, height=2)
but18.grid(row=1, column=4)

but19 = Button(root, text=impares[18], command=Change_Color_19)
but19.config(background="white", foreground="black", width=4, height=2)
but19.grid(row=1, column=5)

but20 = Button(root, text=pares[19], command=Reset)
but20.config(background="white", foreground="black", width=4, height=2)
but20.grid(row=1, column=6)

but21 = Button(root, text=impares[20], command=Change_Color_21)
but21.config(background="white", foreground="black", width=4, height=2)
but21.grid(row=1, column=7)

but22 = Button(root, text=pares[21], command=Reset)
but22.config(background="white", foreground="black", width=4, height=2)
but22.grid(row=1, column=8)

but23 = Button(root, text=pares[22], command=Reset)
but23.config(background="white", foreground="black", width=4, height=2)
but23.grid(row=1, column=9)

but24 = Button(root, text=pares[23], command=Reset)
but24.config(background="white", foreground="black", width=4, height=2)
but24.grid(row=1, column=10)

but25 = Button(root, text=pares[24], command=Reset)
but25.config(background="white", foreground="black", width=4, height=2)
but25.grid(row=1, column=11)

but26 = Button(root, text=pares[25], command=Reset)
but26.config(background="white", foreground="black", width=4, height=2)
but26.grid(row=1, column=12)

#####################################################
###################### FILA 3 #######################
#####################################################

but27 = Button(root, text=pares[26], command=Reset)
but27.config(background="white", foreground="black", width=4, height=2)
but27.grid(row=2, column=0)

but28 = Button(root, text=pares[27], command=Reset)
but28.config(background="white", foreground="black", width=4, height=2)
but28.grid(row=2, column=1)

but29 = Button(root, text=impares[28], command=Change_Color_29)
but29.config(background="white", foreground="black", width=4, height=2)
but29.grid(row=2, column=2)

but30 = Button(root, text=pares[29], command=Reset)
but30.config(background="white", foreground="black", width=4, height=2)
but30.grid(row=2, column=3)

but31 = Button(root, text=pares[30], command=Reset)
but31.config(background="white", foreground="black", width=4, height=2)
but31.grid(row=2, column=4)

but32 = Button(root, text=impares[31], command=Change_Color_32)
but32.config(background="white", foreground="black", width=4, height=2)
but32.grid(row=2, column=5)

but33 = Button(root, text=pares[32], command=Reset)
but33.config(background="white", foreground="black", width=4, height=2)
but33.grid(row=2, column=6)

but34 = Button(root, text=impares[33], command=Change_Color_34)
but34.config(background="white", foreground="black", width=4, height=2)
but34.grid(row=2, column=7)

but35 = Button(root, text=pares[34], command=Reset)
but35.config(background="white", foreground="black", width=4, height=2)
but35.grid(row=2, column=8)

but36 = Button(root, text=pares[35], command=Reset)
but36.config(background="white", foreground="black", width=4, height=2)
but36.grid(row=2, column=9)

but37 = Button(root, text=impares[36], command=Change_Color_37)
but37.config(background="white", foreground="black", width=4, height=2)
but37.grid(row=2, column=10)

but38 = Button(root, text=pares[37], command=Reset)
but38.config(background="white", foreground="black", width=4, height=2)
but38.grid(row=2, column=11)

but39 = Button(root, text=pares[38], command=Reset)
but39.config(background="white", foreground="black", width=4, height=2)
but39.grid(row=2, column=12)

#####################################################
###################### FILA 4 #######################
#####################################################

but40 = Button(root, text=pares[39], command=Reset)
but40.config(background="white", foreground="black", width=4, height=2)
but40.grid(row=3, column=0)

but41 = Button(root, text=impares[40], command=Change_Color_41)
but41.config(background="white", foreground="black", width=4, height=2)
but41.grid(row=3, column=1)

but42 = Button(root, text=pares[41], command=Reset)
but42.config(background="white", foreground="black", width=4, height=2)
but42.grid(row=3, column=2)

but43 = Button(root, text=pares[42], command=Reset)
but43.config(background="white", foreground="black", width=4, height=2)
but43.grid(row=3, column=3)

but44 = Button(root, text=pares[43], command=Reset)
but44.config(background="white", foreground="black", width=4, height=2)
but44.grid(row=3, column=4)

but45 = Button(root, text=impares[44], command=Change_Color_45)
but45.config(background="white", foreground="black", width=4, height=2)
but45.grid(row=3, column=5)

but46 = Button(root, text=impares[45], command=Change_Color_46)
but46.config(background="white", foreground="black", width=4, height=2)
but46.grid(row=3, column=6)

but47 = Button(root, text=impares[46], command=Change_Color_47)
but47.config(background="white", foreground="black", width=4, height=2)
but47.grid(row=3, column=7)

but48 = Button(root, text=pares[47], command=Reset)
but48.config(background="white", foreground="black", width=4, height=2)
but48.grid(row=3, column=8)

but49 = Button(root, text=pares[48], command=Reset)
but49.config(background="white", foreground="black", width=4, height=2)
but49.grid(row=3, column=9)

but50 = Button(root, text=pares[49], command=Reset)
but50.config(background="white", foreground="black", width=4, height=2)
but50.grid(row=3, column=10)

but51 = Button(root, text=impares[50], command=Change_Color_51)
but51.config(background="white", foreground="black", width=4, height=2)
but51.grid(row=3, column=11)

but52 = Button(root, text=pares[51], command=Reset)
but52.config(background="white", foreground="black", width=4, height=2)
but52.grid(row=3, column=12)

#####################################################
###################### FILA 5 #######################
#####################################################

but53 = Button(root, text=impares[52], command=Change_Color_53)
but53.config(background="white", foreground="black", width=4, height=2)
but53.grid(row=4, column=0)

but54 = Button(root, text=impares[53], command=Change_Color_54)
but54.config(background="white", foreground="black", width=4, height=2)
but54.grid(row=4, column=1)

but55 = Button(root, text=impares[54], command=Change_Color_55)
but55.config(background="white", foreground="black", width=4, height=2)
but55.grid(row=4, column=2)

but56 = Button(root, text=pares[55], command=Reset)
but56.config(background="white", foreground="black", width=4, height=2)
but56.grid(row=4, column=3)

but57 = Button(root, text=pares[56], command=Reset)
but57.config(background="white", foreground="black", width=4, height=2)
but57.grid(row=4, column=4)

but58 = Button(root, text=impares[57], command=Change_Color_58)
but58.config(background="white", foreground="black", width=4, height=2)
but58.grid(row=4, column=5)

but59 = Button(root, text=impares[58], command=Change_Color_59)
but59.config(background="white", foreground="black", width=4, height=2)
but59.grid(row=4, column=6)

but60 = Button(root, text=impares[59], command=Change_Color_60)
but60.config(background="white", foreground="black", width=4, height=2)
but60.grid(row=4, column=7)

but61 = Button(root, text=pares[60], command=Reset)
but61.config(background="white", foreground="black", width=4, height=2)
but61.grid(row=4, column=8)

but62 = Button(root, text=pares[61], command=Reset)
but62.config(background="white", foreground="black", width=4, height=2)
but62.grid(row=4, column=9)

but63 = Button(root, text=impares[62], command=Change_Color_63)
but63.config(background="white", foreground="black", width=4, height=2)
but63.grid(row=4, column=10)

but64 = Button(root, text=impares[63], command=Change_Color_64)
but64.config(background="white", foreground="black", width=4, height=2)
but64.grid(row=4, column=11)

but65 = Button(root, text=impares[64], command=Change_Color_65)
but65.config(background="white", foreground="black", width=4, height=2)
but65.grid(row=4, column=12)

#####################################################
###################### FILA 6 #######################
#####################################################

but66 = Button(root, text=impares[65], command=Change_Color_66)
but66.config(background="white", foreground="black", width=4, height=2)
but66.grid(row=5, column=0)

but67 = Button(root, text=impares[66], command=Change_Color_67)
but67.config(background="white", foreground="black", width=4, height=2)
but67.grid(row=5, column=1)

but68 = Button(root, text=impares[67], command=Change_Color_68)
but68.config(background="white", foreground="black", width=4, height=2)
but68.grid(row=5, column=2)

but69 = Button(root, text=impares[68], command=Change_Color_69)
but69.config(background="white", foreground="black", width=4, height=2)
but69.grid(row=5, column=3)

but70 = Button(root, text=impares[69], command=Change_Color_70)
but70.config(background="white", foreground="black", width=4, height=2)
but70.grid(row=5, column=4)

but71 = Button(root, text=impares[70], command=Change_Color_71)
but71.config(background="white", foreground="black", width=4, height=2)
but71.grid(row=5, column=5)

but72 = Button(root, text=impares[71], command=Change_Color_72)
but72.config(background="white", foreground="black", width=4, height=2)
but72.grid(row=5, column=6)

but73 = Button(root, text=impares[72], command=Change_Color_73)
but73.config(background="white", foreground="black", width=4, height=2)
but73.grid(row=5, column=7)

but74 = Button(root, text=impares[73], command=Change_Color_74)
but74.config(background="white", foreground="black", width=4, height=2)
but74.grid(row=5, column=8)

but75 = Button(root, text=impares[74], command=Change_Color_75)
but75.config(background="white", foreground="black", width=4, height=2)
but75.grid(row=5, column=9)

but76 = Button(root, text=impares[75], command=Change_Color_76)
but76.config(background="white", foreground="black", width=4, height=2)
but76.grid(row=5, column=10)

but77 = Button(root, text=impares[76], command=Change_Color_77)
but77.config(background="white", foreground="black", width=4, height=2)
but77.grid(row=5, column=11)

but78 = Button(root, text=impares[77], command=Change_Color_78)
but78.config(background="white", foreground="black", width=4, height=2)
but78.grid(row=5, column=12)

#####################################################
###################### FILA 7 #######################
#####################################################


but79 = Button(root, text=impares[78], command=Change_Color_79)
but79.config(background="white", foreground="black", width=4, height=2)
but79.grid(row=6, column=0)

but80 = Button(root, text=impares[79], command=Change_Color_80)
but80.config(background="white", foreground="black", width=4, height=2)
but80.grid(row=6, column=1)

but81 = Button(root, text=impares[80], command=Change_Color_81)
but81.config(background="white", foreground="black", width=4, height=2)
but81.grid(row=6, column=2)

but82 = Button(root, text=impares[81], command=Change_Color_82)
but82.config(background="white", foreground="black", width=4, height=2)
but82.grid(row=6, column=3)

but83 = Button(root, text=impares[82], command=Change_Color_83)
but83.config(background="white", foreground="black", width=4, height=2)
but83.grid(row=6, column=4)

but84 = Button(root, text=impares[83], command=Change_Color_84)
but84.config(background="white", foreground="black", width=4, height=2)
but84.grid(row=6, column=5)

but85 = Button(root, text=impares[84], command=Change_Color_85)
but85.config(background="white", foreground="black", width=4, height=2)
but85.grid(row=6, column=6)

but86 = Button(root, text=impares[85], command=Change_Color_86)
but86.config(background="white", foreground="black", width=4, height=2)
but86.grid(row=6, column=7)

but87 = Button(root, text=impares[86], command=Change_Color_87)
but87.config(background="white", foreground="black", width=4, height=2)
but87.grid(row=6, column=8)

but88 = Button(root, text=impares[87], command=Change_Color_88)
but88.config(background="white", foreground="black", width=4, height=2)
but88.grid(row=6, column=9)

but89 = Button(root, text=impares[88], command=Change_Color_89)
but89.config(background="white", foreground="black", width=4, height=2)
but89.grid(row=6, column=10)

but90 = Button(root, text=impares[89], command=Change_Color_90)
but90.config(background="white", foreground="black", width=4, height=2)
but90.grid(row=6, column=11)

but91 = Button(root, text=impares[90], command=Change_Color_91)
but91.config(background="white", foreground="black", width=4, height=2)
but91.grid(row=6, column=12)

#####################################################
###################### FILA 8 #######################
#####################################################

but92 = Button(root, text=impares[91], command=Change_Color_92)
but92.config(background="white", foreground="black", width=4, height=2)
but92.grid(row=7, column=0)

but93 = Button(root, text=impares[92], command=Change_Color_93)
but93.config(background="white", foreground="black", width=4, height=2)
but93.grid(row=7, column=1)

but94 = Button(root, text=impares[93], command=Change_Color_94)
but94.config(background="white", foreground="black", width=4, height=2)
but94.grid(row=7, column=2)

but95 = Button(root, text=impares[94], command=Change_Color_95)
but95.config(background="white", foreground="black", width=4, height=2)
but95.grid(row=7, column=3)

but96 = Button(root, text=impares[95], command=Change_Color_96)
but96.config(background="white", foreground="black", width=4, height=2)
but96.grid(row=7, column=4)

but97 = Button(root, text=impares[96], command=Change_Color_97)
but97.config(background="white", foreground="black", width=4, height=2)
but97.grid(row=7, column=5)

but98 = Button(root, text=impares[97], command=Change_Color_98)
but98.config(background="white", foreground="black", width=4, height=2)
but98.grid(row=7, column=6)

but99 = Button(root, text=impares[98], command=Change_Color_99)
but99.config(background="white", foreground="black", width=4, height=2)
but99.grid(row=7, column=7)

but100 = Button(root, text=impares[99], command=Change_Color_100)
but100.config(background="white", foreground="black", width=4, height=2)
but100.grid(row=7, column=8)

but101 = Button(root, text=impares[100], command=Change_Color_101)
but101.config(background="white", foreground="black", width=4, height=2)
but101.grid(row=7, column=9)

but102 = Button(root, text=impares[101], command=Change_Color_102)
but102.config(background="white", foreground="black", width=4, height=2)
but102.grid(row=7, column=10)

but103 = Button(root, text=impares[102], command=Change_Color_103)
but103.config(background="white", foreground="black", width=4, height=2)
but103.grid(row=7, column=11)

but104 = Button(root, text=impares[103], command=Change_Color_104)
but104.config(background="white", foreground="black", width=4, height=2)
but104.grid(row=7, column=12)

#####################################################
###################### FILA 9 #######################
#####################################################

but105 = Button(root, text=impares[104], command=Change_Color_105)
but105.config(background="white", foreground="black", width=4, height=2)
but105.grid(row=8, column=0)

but106 = Button(root, text=impares[105], command=Change_Color_106)
but106.config(background="white", foreground="black", width=4, height=2)
but106.grid(row=8, column=1)

but107 = Button(root, text=impares[106], command=Change_Color_107)
but107.config(background="white", foreground="black", width=4, height=2)
but107.grid(row=8, column=2)

but108 = Button(root, text=pares[107], command=Reset)
but108.config(background="white", foreground="black", width=4, height=2)
but108.grid(row=8, column=3)

but109 = Button(root, text=impares[108], command=Change_Color_109)
but109.config(background="white", foreground="black", width=4, height=2)
but109.grid(row=8, column=4)

but110 = Button(root, text=impares[109], command=Change_Color_110)
but110.config(background="white", foreground="black", width=4, height=2)
but110.grid(row=8, column=5)

but111 = Button(root, text=impares[110], command=Change_Color_111)
but111.config(background="white", foreground="black", width=4, height=2)
but111.grid(row=8, column=6)

but112 = Button(root, text=impares[111], command=Change_Color_112)
but112.config(background="white", foreground="black", width=4, height=2)
but112.grid(row=8, column=7)

but113 = Button(root, text=impares[112], command=Change_Color_113)
but113.config(background="white", foreground="black", width=4, height=2)
but113.grid(row=8, column=8)

but114 = Button(root, text=pares[113], command=Reset)
but114.config(background="white", foreground="black", width=4, height=2)
but114.grid(row=8, column=9)

but115 = Button(root, text=impares[114], command=Change_Color_115)
but115.config(background="white", foreground="black", width=4, height=2)
but115.grid(row=8, column=10)

but116 = Button(root, text=impares[115], command=Change_Color_116)
but116.config(background="white", foreground="black", width=4, height=2)
but116.grid(row=8, column=11)

but117 = Button(root, text=impares[116], command=Change_Color_117)
but117.config(background="white", foreground="black", width=4, height=2)
but117.grid(row=8, column=12)

#####################################################
###################### FILA 10 ######################
#####################################################

but118 = Button(root, text=pares[117], command=Reset)
but118.config(background="white", foreground="black", width=4, height=2)
but118.grid(row=9, column=0)

but119 = Button(root, text=impares[118], command=Change_Color_119)
but119.config(background="white", foreground="black", width=4, height=2)
but119.grid(row=9, column=1)

but120 = Button(root, text=pares[119], command=Reset)
but120.config(background="white", foreground="black", width=4, height=2)
but120.grid(row=9, column=2)

but121 = Button(root, text=pares[120], command=Reset)
but121.config(background="white", foreground="black", width=4, height=2)
but121.grid(row=9, column=3)

but122 = Button(root, text=pares[121], command=Reset)
but122.config(background="white", foreground="black", width=4, height=2)
but122.grid(row=9, column=4)

but123 = Button(root, text=impares[122], command=Change_Color_123)
but123.config(background="white", foreground="black", width=4, height=2)
but123.grid(row=9, column=5)

but124 = Button(root, text=impares[123], command=Change_Color_124)
but124.config(background="white", foreground="black", width=4, height=2)
but124.grid(row=9, column=6)

but125 = Button(root, text=impares[124], command=Change_Color_125)
but125.config(background="white", foreground="black", width=4, height=2)
but125.grid(row=9, column=7)

but126 = Button(root, text=pares[125], command=Reset)
but126.config(background="white", foreground="black", width=4, height=2)
but126.grid(row=9, column=8)

but127 = Button(root, text=pares[126], command=Reset)
but127.config(background="white", foreground="black", width=4, height=2)
but127.grid(row=9, column=9)

but128 = Button(root, text=pares[127], command=Reset)
but128.config(background="white", foreground="black", width=4, height=2)
but128.grid(row=9, column=10)

but129 = Button(root, text=impares[128], command=Change_Color_129)
but129.config(background="white", foreground="black", width=4, height=2)
but129.grid(row=9, column=11)

but130 = Button(root, text=pares[129], command=Reset)
but130.config(background="white", foreground="black", width=4, height=2)
but130.grid(row=9, column=12)

#####################################################
###################### FILA 11 ######################
#####################################################

but131 = Button(root, text=pares[130], command=Reset)
but131.config(background="white", foreground="black", width=4, height=2)
but131.grid(row=10, column=0)

but132 = Button(root, text=impares[131], command=Change_Color_132)
but132.config(background="white", foreground="black", width=4, height=2)
but132.grid(row=10, column=1)

but133 = Button(root, text=pares[132], command=Reset)
but133.config(background="white", foreground="black", width=4, height=2)
but133.grid(row=10, column=2)

but134 = Button(root, text=pares[133], command=Reset)
but134.config(background="white", foreground="black", width=4, height=2)
but134.grid(row=10, column=3)

but135 = Button(root, text=pares[134], command=Reset)
but135.config(background="white", foreground="black", width=4, height=2)
but135.grid(row=10, column=4)

but136 = Button(root, text=pares[135], command=Reset)
but136.config(background="white", foreground="black", width=4, height=2)
but136.grid(row=10, column=5)

but137 = Button(root, text=impares[136], command=Change_Color_137)
but137.config(background="white", foreground="black", width=4, height=2)
but137.grid(row=10, column=6)

but138 = Button(root, text=pares[137], command=Reset)
but138.config(background="white", foreground="black", width=4, height=2)
but138.grid(row=10, column=7)

but139 = Button(root, text=pares[138], command=Reset)
but139.config(background="white", foreground="black", width=4, height=2)
but139.grid(row=10, column=8)

but140 = Button(root, text=pares[139], command=Reset)
but140.config(background="white", foreground="black", width=4, height=2)
but140.grid(row=10, column=9)

but141 = Button(root, text=pares[140], command=Reset)
but141.config(background="white", foreground="black", width=4, height=2)
but141.grid(row=10, column=10)

but142 = Button(root, text=impares[141], command=Change_Color_142)
but142.config(background="white", foreground="black", width=4, height=2)
but142.grid(row=10, column=11)

but143 = Button(root, text=pares[142], command=Reset)
but143.config(background="white", foreground="black", width=4, height=2)
but143.grid(row=10, column=12)

#####################################################
###################### FILA 12 ######################
#####################################################

but144 = Button(root, text=pares[143], command=Reset)
but144.config(background="white", foreground="black", width=4, height=2)
but144.grid(row=11, column=0)

but145 = Button(root, text=pares[144], command=Reset)
but145.config(background="white", foreground="black", width=4, height=2)
but145.grid(row=11, column=1)

but146 = Button(root, text=impares[145], command=Change_Color_146)
but146.config(background="white", foreground="black", width=4, height=2)
but146.grid(row=11, column=2)

but147 = Button(root, text=pares[146], command=Reset)
but147.config(background="white", foreground="black", width=4, height=2)
but147.grid(row=11, column=3)

but148 = Button(root, text=pares[147], command=Reset)
but148.config(background="white", foreground="black", width=4, height=2)
but148.grid(row=11, column=4)

but149 = Button(root, text=pares[148], command=Reset)
but149.config(background="white", foreground="black", width=4, height=2)
but149.grid(row=11, column=5)

but150 = Button(root, text=impares[149], command=Change_Color_150)
but150.config(background="white", foreground="black", width=4, height=2)
but150.grid(row=11, column=6)

but151 = Button(root, text=pares[150], command=Reset)
but151.config(background="white", foreground="black", width=4, height=2)
but151.grid(row=11, column=7)

but152 = Button(root, text=pares[151], command=Reset)
but152.config(background="white", foreground="black", width=4, height=2)
but152.grid(row=11, column=8)

but153 = Button(root, text=pares[152], command=Reset)
but153.config(background="white", foreground="black", width=4, height=2)
but153.grid(row=11, column=9)

but154 = Button(root, text=impares[153], command=Change_Color_154)
but154.config(background="white", foreground="black", width=4, height=2)
but154.grid(row=11, column=10)

but155 = Button(root, text=pares[154], command=Reset)
but155.config(background="white", foreground="black", width=4, height=2)
but155.grid(row=11, column=11)

but156 = Button(root, text=pares[155], command=Reset)
but156.config(background="white", foreground="black", width=4, height=2)
but156.grid(row=11, column=12)

#####################################################
###################### FILA 13 ######################
#####################################################

but157 = Button(root, text=pares[156], command=Reset)
but157.config(background="white", foreground="black", width=4, height=2)
but157.grid(row=12, column=0)

but158 = Button(root, text=pares[157], command=Reset)
but158.config(background="white", foreground="black", width=4, height=2)
but158.grid(row=12, column=1)

but159 = Button(root, text=pares[158], command=Reset)
but159.config(background="white", foreground="black", width=4, height=2)
but159.grid(row=12, column=2)

but160 = Button(root, text=pares[159], command=Reset)
but160.config(background="white", foreground="black", width=4, height=2)
but160.grid(row=12, column=3)

but161 = Button(root, text=pares[160], command=Reset)
but161.config(background="white", foreground="black", width=4, height=2)
but161.grid(row=12, column=4)

but162 = Button(root, text=pares[161], command=Reset)
but162.config(background="white", foreground="black", width=4, height=2)
but162.grid(row=12, column=5)

but163 = Button(root, text=pares[162], command=Reset)
but163.config(background="white", foreground="black", width=4, height=2)
but163.grid(row=12, column=6)

but164 = Button(root, text=pares[163], command=Reset)
but164.config(background="white", foreground="black", width=4, height=2)
but164.grid(row=12, column=7)

but165 = Button(root, text=pares[164], command=Reset)
but165.config(background="white", foreground="black", width=4, height=2)
but165.grid(row=12, column=8)

but166 = Button(root, text=pares[165], command=Reset)
but166.config(background="white", foreground="black", width=4, height=2)
but166.grid(row=12, column=9)

but167 = Button(root, text=pares[166], command=Reset)
but167.config(background="white", foreground="black", width=4, height=2)
but167.grid(row=12, column=10)

but168 = Button(root, text=pares[167], command=Reset)
but168.config(background="white", foreground="black", width=4, height=2)
but168.grid(row=12, column=11)

but169 = Button(root, text=pares[168], command=Reset)
but169.config(background="white", foreground="black", width=4, height=2)
but169.grid(row=12, column=12)

root.mainloop() #INICIALIZA LA INTERFAZ