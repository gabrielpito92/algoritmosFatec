# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 20:23:11 2023

@author: gabri
"""
resultado = ((18 + 3 * 2) / 8 + 5 * 3) / 6
print(resultado)

resultado2 = ((8 * 4 + 3) / 7) + (((3 + 15 / 5) * 3) * 2) - (((19 - 7) / 6) * 2) + 12
print (resultado2)

resultado3 = 14.4 * 0.072 / 0.16 * 0.000027
print(resultado3)

resultado4 = ((2) * ((3 / 4)*-1) / ((2 / 3)*-1))
print(resultado4)


def tryConta():
    resultado5 = (+2 -3 +1) / (-2 + 2)
    
try:
    tryConta()
except ZeroDivisionError as err:
    print("Não há como dividir por zero:", err)

resultado6 = (+4 -9) / (-5 +3)
print(resultado6)

resultado7 = (2 -3 +1) / (-7)
print(resultado7)

def XOR (a, b): 
    if a != b: 
        return 1
    else: 
        return 0

print("+---------------+----------------+") 
print(" | XOR Truth Table | Result |") 
print(" A = False, B = False | A XOR B =",XOR(False,False)," | ")
print(" A = False, B = True | A XOR B =",XOR(False,True)," | ")
print(" A = True, B = False | A XOR B =",XOR(True,False)," | ")
print(" A = True, B = True | A XOR B =",XOR(True,True)," | ")

def XNOR(a,b): 
    if(a == b): 
        return 1
    else: 
        return 0
  
print("+---------------+----------------+") 
print(" | XNOR Truth Table | Result |") 
print(" A = False, B = False | A XNOR B =",XNOR(False,False)," | ") 
print(" A = False, B = True | A XNOR B =",XNOR(False,True)," | ") 
print(" A = True, B = False | A XNOR B =",XNOR(True,False)," | ") 
print(" A = True, B = True | A XNOR B =",XNOR(True,True)," | ") 

resultado3_1 = 27 ** 1/3
print(resultado3_1)

import math
resultado3_2 = math.sqrt(49)
print(resultado3_2)

resultado3_3 = 2 ** 10
print(resultado3_3)

resultado4_1 = 49 % 5
print(resultado4_1)

resultado4_2 = 49 // 5
print(resultado4_2)

# inteiro aleatório
integer = -20
print('O valor absoluto de -20 é:', abs(integer))

# número flutuante aleatório
floating = -30.33
print('O valor absoluto de -30.33 é:', abs(floating))