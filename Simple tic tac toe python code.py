# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it tic-tac-toe.
# write your code here
class OutofBoundsError(Exception):
    pass
class OccupiedError(Exception):
    pass
print("---------")
print("|"," "," "," ","|")
print("|"," "," "," ","|")
print("|"," "," "," ","|")
print("---------")
bol = True
turn = 0
xc,yc = input().split()
li = [[" " for j in range(3)] for i in range(3)]
while bol:
    try:
        try:
           val1=int(xc)
           val2=int(yc)
        except ValueError:
           print("You should enter numbers!")
           xc,yc = input().split()
        if (int(xc) > 3 or int(xc) < 1) or (int(yc) > 3 or int(yc) < 1):
           raise OutofBoundsError
        elif (li[int(xc)-1][int(yc)-1] == 'X') or (li[int(xc)-1][int(yc)-1] == 'O'):
           raise OccupiedError
    except OutofBoundsError:
       print("Coordinates should be from 1 to 3!")
       xc,yc = input().split()
    except OccupiedError:
       print("This cell is occupied! Choose another one!")
       xc,yc = input().split()
    else:
        if turn == 0:
           li[int(xc)-1][int(yc)-1] = 'X'
           print("---------")
           print("|",li[0][0],li[0][1],li[0][2],"|")
           print("|",li[1][0],li[1][1],li[1][2],"|")
           print("|",li[2][0],li[2][1],li[2][2],"|")
           print("---------")
           turn = 1
        else:
            li[int(xc)-1][int(yc)-1] = 'O'
            print("---------")
            print("|",li[0][0],li[0][1],li[0][2],"|")
            print("|",li[1][0],li[1][1],li[1][2],"|")
            print("|",li[2][0],li[2][1],li[2][2],"|")
            print("---------")
            turn = 0
        space = 0 # for to count no of spaces
        for item in li:
            space += item.count(" ")   
        if li[0][0] == li[0][1] == li[0][2] and (li[0][0] != " "):
            print(li[0][0],"wins")
            break
        elif li[1][0] == li[1][1] == li[1][2] and (li[1][0] != " "):
            print(li[1][0],"wins")
            break
        elif li[2][0] == li[2][1] == li[2][2] and (li[2][0] != " "):
            print(li[2][0], "wins")
            break
        elif li[0][0] == li[1][0] == li[2][0] and (li[0][0] != " "):
            print(li[0][0], "wins")
            break
        elif li[0][1] == li[1][1] == li[2][1] and (li[0][1] != " "):
            print(li[0][1] ,"wins")
            break
        elif li[0][2] == li[1][2] == li[2][2] and (li[0][2] != " "):
            print(li[0][2], "wins")
            break
        elif li[0][0] == li[1][1] == li[2][2] and (li[0][0] != " "):
            print(li[0][0], "wins") 
            break
        elif li[0][2] == li[1][1] == li[2][0] and (li[0][2] != " "):
            print(li[0][2],"wins")
            break
        elif space == 0:
            print("Draw ")  
            break
        xc,yc = input().split()    
            
          

    
               

