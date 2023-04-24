# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 18:21:31 2023

@author: moham
"""
import chess

board = chess.Board()
oldList = ['a7','b2','c2','d2','e2','f2','g2','a1','b1','c1','d1','e1','f1','g1','h1', 't1']
newList = ['a8','b2','c2','d2','e2','f2','g2','a1','b1','c1','d1','e1','f1','g1','h1', 's1']
DestinationList = []
SourceList = []

'''
Move: S and D are only size 1, no graveyard coord
old = [e2] -> Source = [e2]
new = [e4] -> Destination = [e4]

Capture: S and D are only size 1, no graveyard coord
old = [e5] -> Source = [e5]
new = [c5] -> Destination = [c5] *here t1 is just to designate some graveyard spot

Castle: S and D are size 2, no graveyard coords
old = [e1, h1] -> Source = [e1, h1]
new = [f1, g1] -> Destination = [f1, g1]

Promotion: S and D are size 2, S contains one piece graveyard spot and D contains one pawn graveyard spot
old = [c7, t1] -> Source = [c7, t1] *t1 is a special piece graveyard spot
new = [c8, s1] -> Destination = [c8, s1] *s1 is the pawn dead spot

En Passant: S and D are size 1
old = [a5] -> Source = [a5] 
new = [b6] -> Destination = [b6] *s1 is the pawn dead spot

Kill Promotion: S and D are size 2, S contains one piece spot, D contains only graveyard, one piece and one pawn
old = [a7, t1] -> Source = [a7, t1] *t1 is the promoted special piece graveyard spot
new = [b8, s1] -> Destination = [b8, s1] *s1 is the pawn dead spot, t2 is the killed special piece graveyard

'''

def graveyardCheck(inputList):
    returnList = [0, 0] #[numPieceGY, numPawnGY]
    for i in range(len(inputList)):
        if inputList[i][0] == 't' or inputList[i][0] == 's': # Contains something from the piece GY
            returnList[0] += 1
        elif inputList[i][1:] == '10' or inputList[i][1:] == '0': # contains something from the pawn GY
            returnList[1] += 1
    return returnList

def castleCheck(inputList): # Return Castle String
    for i in range(len(inputList)):
        if inputList[i][0] == "g": # King side Castle
            if inputList[i][1] == "1": # White Castle
                return "e1-g1"
            elif inputList[i][1] == "8": # Black Castle
                return "e8-g8"
        elif inputList[i][0] == "c": # QueenSide Castle
            if inputList[i][1] == "1": # White Castle
                return "e1-c1"
            elif inputList[i][1] == "8": # Black Castle
                return "e8-c8"

def promotionCheck(inputList1, inputList2): # Return promotion string
    returnString1 = ''
    returnString2 = ''
    for i in range(len(inputList1)): # List
        if inputList1[i][0] != 't' and inputList1[i][0] != 's':
            returnString1 = inputList1[i]
        if inputList2[i][0] != 't' and inputList2[i][0] != 's':
            returnString2 = inputList2[i]
    return returnString1 + '-' + returnString2

def determineString(SourceList, DestinationList):
    SourceCheck = graveyardCheck(SourceList)
    DestinationCheck = graveyardCheck(DestinationList)
    returnString = ""

    if len(SourceList) == 1 and len(DestinationList) == 1: # Piece movement, Capture, En Passant
        returnString = SourceList[0] + "-" + DestinationList[0]
    else: # May need to check for size 2, but shouldnt have to
        if (SourceCheck[0] == 0 and SourceCheck[1] == 0) and (DestinationCheck[0] == 0 and DestinationCheck[1] == 0): # Castle
            returnString = castleCheck(DestinationList)
        else: # Promotion
            returnString = promotionCheck(SourceList, DestinationList)
    return returnString

def diffList(OldList, NewList):
    for i in range(len(newList)):
        if newList[i] not in oldList:
            DestinationList.append(newList[i])
    for i in range(len(oldList)):
        if oldList[i] not in newList:
            SourceList.append(oldList[i])

diffList(oldList,newList)
print(determineString(SourceList, DestinationList)) # This is the Sheisty String



'''
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

['Rook','a1'],
['Knight','b1'],
['Bishop','c1'],
['Queen','d1'],
['King','e1'],
['Bishop','f1'],
['Knight','g1'],
['Rook','h1'],
]



newlist = [['Pawn','a4'],
['Pawn','b2'],
['Pawn','c2'],
['Pawn','d2'],
['Pawn','e2'],
['Pawn','f2'],
['Pawn','g2'],
['Pawn','h2'],

['Rook','a1'],
['Knight','b1'],
['Bishop','c1'],
['Queen','d1'],
['King','e1'],
['Bishop','f1'],
['Knight','g1'],
['Rook','h1']
]




oldlist = [['Pawn','a2'],
['Pawn','b2'],
['Pawn','c2'],
['Pawn','d2'],
['Pawn','e2'],
['Pawn','f2'],
['Pawn','g2'],
['Pawn','h2'],


['Rook','a1'],
['Knight','b1'],
['Bishop','c1'],
['Queen','d1'],
['King','e1'],
['Bishop','f1'],
['Knight','g1'],
['Rook','h1']
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
'''