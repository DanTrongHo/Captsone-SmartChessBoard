# -*- coding: utf-8 -*-
"""

# Name:         Mohammad Shihab

@author: moham
"""
from numpy import array as Ar
import numpy as np

emptylist=[]
x=0

"""
Pawn =1 
Rook = 2
Knight =3
Bishop = 4
Queen= 5
King =6
"""


start=np.array([
        [2,3,4,5,6,4,3,2],
        [1,1,1,1,1,1,1,1],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [1,1,1,1,1,1,1,1],
         [2,3,4,5,6,4,3,2]]
        )  #Initial Chess board

BigDict = {     #Dictionary to convert Bluetooth Data into piece movement steps
        'a' : 200,
        'b' : 400,
        'c' : 600,
        'd' : 800,
        'e' : 900,
        'f' : 1100,
        'g' : 1300,
        
        '1' : 200,
        '2' : 400,
        '3' : 600,
        '4' : 800,
        '5' : 1000,
        '6' : 1200,
        '7' : 1400,
        '8' : 1600,
        
}


ArrayDict = {     #Dictonary to update array
        'a' : 0,
        'b' : 1,
        'c' : 2,
        'd' : 3,
        'e' : 4,
        'f' : 5,
        'g' : 6,
        'h' : 7,
        
        '1' : 0,
        '2' : 1,
        '3' : 2,
        '4' : 3,
        '5' : 4,
        '6' : 5,
        '7' : 6,
        '8' : 7,
        
}

DanString=(input("Input Dan String")) #will always be a 5 letter string in the form of e4-e5

GrabX= BigDict[DanString[0]]
GrabY= BigDict[DanString[1]]

#Movement script for motors to go to Grab X , Grab Y then turn on Electromagnet


print("Grabbing (",GrabX,",",GrabY,")")


DropX= BigDict[DanString[3]]
DropY= BigDict[DanString[4]]

#Movement script for motors to go to DropX , DropY then turn off Electromagnet


#Electromagnet go home 


print(ArrayDict[DanString[0]])
print(ArrayDict[DanString[1]])
POI=start[ArrayDict[DanString[1]]][ArrayDict[DanString[0]]]
print("piece moved is the", POI)

#print(POI)
start[ArrayDict[DanString[1]]][ArrayDict[DanString[0]]]=0
start[ArrayDict[DanString[4]]][ArrayDict[DanString[3]]]=POI

print(start)



#print(start)
#print(start[0][0])
#print(BigDict["a"])

""" ///
Legal Piece movement Check
//"""



"""
Pawn =1 
Rook = 2
Knight =3
Bishop = 4
Queen= 5
King =6
"""
#start[ArrayDict['a']][ArrayDict['1']] = x 


"""
def cfu_func(a,b,x):
    for aRow in range(Rows):
        EachRow=[]
        for aCol in range (Cols):
                EachRow.append(0)
        emptylist.append(EachRow)
        final_array=Ar(emptylist)
    return(final_array)
print(cfu_func(Cols,Rows,x))


"""
