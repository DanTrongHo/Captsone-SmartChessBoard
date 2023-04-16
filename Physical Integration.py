# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 18:21:31 2023

@author: moham
"""
import chess

board=chess.Board()

#light=LED(22)

def graveyardchecker(listelement):
    
    if listelement[1][0] == 's' or listelement[1][0] == 't':
        return True
    elif listelement[1][1] == '0' or listelement[1][1] == '9':
        return True
    else:
        return False

def castlechecker (thewhole):
    cond1=0
    cond2=0
    cond3=0
    if (thewhole[0][0] == 'King'):
        cond1+=1
    if ((thewhole[1][0] == 'King')):
        cond1+=1
    if ((thewhole[0][0] == 'Rook')):
        cond2+=1
    if ((thewhole[1][0] == 'Rook')):
        cond2+=1
    if thewhole[0][1][0] == 's' or thewhole[0][1][0] == 't':
        cond3+=1
    if thewhole[1][1][0] == 's' or thewhole[1][1][0] == 't':
        cond3+=1
    
    if (cond1 > 0) and (cond2 > 0) and (cond3 == 0) :
        return(True)
    else:
        return(False)


mytest=[["King",'a9'],['Rook','s7']]

print(castlechecker(mytest))
theoldlist=[['Pawn','a2'],
['Pawn','b2'],
['Pawn','c2'],
['Pawn','d2'],
['Pawn','e2'],
['Pawn','f2'],
['Pawn','g2'],
['Pawn','h2'],
['Pawn','a7'],
['Pawn','b7'],
['Pawn','c7'],
['Pawn','d7'],
['Pawn','e7'],
['Pawn','g7'],
['Pawn','h7'],
['Pawn','h7'],

['Rook','a1'],
['Knight','b1'],
['Bishop','c1'],
['Queen','d1'],
['King','e1'],
['Bishop','f1'],
['Knight','g1'],
['Rook','h1'],

['Rook','a8'],
['Knight','b8'],
['Bishop','c8'],
['Queen','d8'],
['King','e8'],
['Bishop','f8'],
['Knight','g8'],
['Rook','h8']
]



newlist = [['Pawn','a4'],
['Pawn','b2'],
['Pawn','c2'],
['Pawn','d2'],
['Pawn','e2'],
['Pawn','f2'],
['Pawn','g2'],
['Pawn','h2'],
['Pawn','a7'],
['Pawn','b7'],
['Pawn','c7'],
['Pawn','d7'],
['Pawn','e7'],
['Pawn','g7'],
['Pawn','h7'],
['Pawn','h7'],

['Rook','a1'],
['Knight','b1'],
['Bishop','c1'],
['Queen','d1'],
['King','e1'],
['Bishop','f1'],
['Knight','g1'],
['Rook','h1'],

['Rook','a8'],
['Knight','b8'],
['Bishop','c8'],
['Queen','d8'],
['King','e8'],
['Bishop','f8'],
['Knight','g8'],
['Rook','h8']
]






oldlist = [['Pawn','a2'],
['Pawn','b2'],
['Pawn','c2'],
['Pawn','d2'],
['Pawn','e2'],
['Pawn','f2'],
['Pawn','g2'],
['Pawn','h2'],
['Pawn','a7'],
['Pawn','b7'],
['Pawn','c7'],
['Pawn','d7'],
['Pawn','e7'],
['Pawn','g7'],
['Pawn','h7'],
['Pawn','h7'],

['Rook','a1'],
['Knight','b1'],
['Bishop','c1'],
['Queen','d1'],
['King','e1'],
['Bishop','f1'],
['Knight','g1'],
['Rook','h1'],

['Rook','a8'],
['Knight','b8'],
['Bishop','c8'],
['Queen','d8'],
['King','e8'],
['Bishop','f8'],
['Knight','g8'],
['Rook','h8']
]









"""

BigDict = {     #Dictionary to convert Bluetooth Data into piece movement steps 400 steps center to center
        "A1" : board.piece_at(chess.A1),
        "A2" : board.piece_at(chess.A2),
        "A3" : board.piece_at(chess.A3),
        "A4" : board.piece_at(chess.A4),
        "A5" : board.piece_at(chess.A5),
        "A6" : board.piece_at(chess.A6),
        "A7" : board.piece_at(chess.A7),
        "A8" : board.piece_at(chess.A8),
        
        "B1" : board.piece_at(chess.B1),
        "B2" : board.piece_at(chess.B2),
        "B3" : board.piece_at(chess.B3),
        "B4" : board.piece_at(chess.B4),
        "B5" : board.piece_at(chess.B5),
        "B6" : board.piece_at(chess.B6),
        "B7" : board.piece_at(chess.B7),
        "B8" : board.piece_at(chess.B8),
        
        "C1" : board.piece_at(chess.C1),
        "C2" : board.piece_at(chess.C2),
        "C3" : board.piece_at(chess.C3),
        "C4" : board.piece_at(chess.C4),
        "C5" : board.piece_at(chess.C5),
        "C6" : board.piece_at(chess.C6),
        "C7" : board.piece_at(chess.C7),
        "C8" : board.piece_at(chess.C8),
        
        "D1" : board.piece_at(chess.D1),
        "D2" : board.piece_at(chess.D2),
        "D3" : board.piece_at(chess.D3),
        "D4" : board.piece_at(chess.D4),
        "D5" : board.piece_at(chess.D5),
        "D6" : board.piece_at(chess.D6),
        "D7" : board.piece_at(chess.D7),
        "D8" : board.piece_at(chess.D8),
        
        "E1" : board.piece_at(chess.E1),
        "E2" : board.piece_at(chess.E2),
        "E3" : board.piece_at(chess.E3),
        "E4" : board.piece_at(chess.E4),
        "E5" : board.piece_at(chess.E5),
        "E6" : board.piece_at(chess.E6),
        "E7" : board.piece_at(chess.E7),
        "E8" : board.piece_at(chess.E8),
        
        "F1" : board.piece_at(chess.F1),
        "F2" : board.piece_at(chess.F2),
        "F3" : board.piece_at(chess.F3),
        "F4" : board.piece_at(chess.F4),
        "F5" : board.piece_at(chess.F5),
        "F6" : board.piece_at(chess.F6),
        "F7" : board.piece_at(chess.F7),
        "F8" : board.piece_at(chess.F8),
        
        "G1" : board.piece_at(chess.G1),
        "G2" : board.piece_at(chess.G2),
        "G3" : board.piece_at(chess.G3),
        "G4" : board.piece_at(chess.G4),
        "G5" : board.piece_at(chess.G5),
        "G6" : board.piece_at(chess.G6),
        "G7" : board.piece_at(chess.G7),
        "G8" : board.piece_at(chess.G8),
        
        "H1" : board.piece_at(chess.H1),
        "H2" : board.piece_at(chess.H2),
        "H3" : board.piece_at(chess.H3),
        "H4" : board.piece_at(chess.H4),
        "H5" : board.piece_at(chess.H5),
        "H6" : board.piece_at(chess.H6),
        "H7" : board.piece_at(chess.H7),
        "H8" : board.piece_at(chess.H8)
        
        }

   """     
        
        
#To update oldlist, check which piece is in first part of DanString, move it to second
#If something is in the second part of the DanString, kill it

listofchanges=[]
ogplace=[]

i=0
j=0
physmove=""
while True:
    
    if newlist[i] not in oldlist:
        listofchanges.append(newlist[i])

    i+=1
    if i==len(newlist):
        break


while True:
    
    if oldlist[j] not in newlist:
        ogplace.append(oldlist[j])
        
    j+=1
    if j==len(oldlist):
        break



print(listofchanges)
print(ogplace)

if len(listofchanges) == 1:
    part1=ogplace[0]
    part2=listofchanges[0]
    ShiestyString= part1[1]+ "-" + part2[1]

elif len(listofchanges) == 2:
    if castlechecker(listofchanges) == True:
        if ogplace[0][0] == 'King':
            part1= ogplace[0]
        else:
            part1= ogplace[1]
        
        if listofchanges[0][0] == 'King':
            part2=listofchanges[0]
        else:
            part2=listofchanges[0]
        
        ShiestyString= part1[1]+ "-" + part2[1]
    else:
        k=0
        while k != 2:
            if graveyardchecker(listofchanges[k]) == False:
                part2=listofchanges[k]
                for u in range (2):
                    if listofchanges[k][0] == ogplace[u][0]:
                        part1= ogplace[u]
                ShiestyString= part1[1]+ "-" + part2[1]
            k+=1
        
print(ShiestyString)

ShiestyString = ShiestyString.replace(ShiestyString[2], "")
"""
movecheck=ShiestyString[0].upper() + ShiestyString[1]


piece2check= BigDict[movecheck]
piece2check=piece2check.symbol()


if piece2check == 'P'  or piece2check == 'p':
    LM= ShiestyString[2]+ShiestyString[3]
else:
    LM= piece2check+ ShiestyString[2]+ShiestyString[3]

if LM in board.legal_moves:
    """
LMCheck=chess.Move.from_uci(ShiestyString) in board.legal_moves
"""
if LMCheck == False: 
    light.on()
    ##Button 27
"""
    
move = chess.Move.from_uci(ShiestyString)
board.push(move)

    

#Length list 1 EZ
#Length List 2 not the graveyard
#Length list 3 not the graveyard not the pawn