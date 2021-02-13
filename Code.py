# write your code here
import random
import copy


def afis_matrix():
    print("---------")
    for i in range(3):
        print('|',end=' ')
        for j in range(3):
            if matrix[i][j]!='_':
                print(matrix[i][j],end=' ')
            else:
                print(" ",end=" ")
        print('|')
    print("---------")





def winnig(sign):
    for i in range(3):
        if matrix[i][0]==matrix[i][1] and matrix[i][1]==matrix[i][2] and matrix[i][2]==sign:
            return True
        if matrix[0][i]==matrix[1][i] and matrix[1][i]==matrix[2][i] and matrix[2][i]==sign:
            return True
    if matrix[0][0]==matrix[1][1] and matrix[1][1]==matrix[2][2] and matrix[2][2]==sign:
        return True
    if matrix[0][2]==matrix[1][1] and matrix[1][1]==matrix[2][0] and matrix[2][0]==sign:
        return True
    return False





def user(sign):
    print("Enter the coordinates:")
    s=input()
    s=list(s.split())
    b=s[0]
    if len(s)>1:
        a=s[1]
    else:
        a="Nimic"
    while a>'3' or a<'1' or b<'1' or b>'3' or matrix[4-int(a)-1][int(b)-1]!='_':
        ok=1
        for i in range(0,10):
            if a.count(str(i))>0:
                ok=0
                break
        for i in range(0,10):
            if b.count(str(i))>0:
                ok-=1
                break
        if ok!=-1:
            print("You should enter numbers!")
        elif a>'3' or a<'1' or b<'1' or b>'3':
            print("Coordinates should be from 1 to 3!")
        elif matrix[4-int(a)-1][int(b)-1]!='_':
            print("This cell is occupied! Choose another one!\nEnter the coordinates:")
        s=input("Enter the coordinates:")
        s=list(s.split())
        b=s[0]
        if len(s)>1:
            a=s[1]
        else:
            a="Nimic"
    matrix[4-int(a)-1][int(b)-1]=sign







def easy(sign):
    print("Making move level \"easy\"")
    if random.choice(range(2))==1:
        for i in range(3):
            ok=0
            for j in range(3):
                if matrix[i][j]=='_':
                    matrix[i][j]=sign
                    ok=1
                    break
            if ok==1:
                break
    else:
        i=random.choice(range(3))
        j=random.choice(range(3))
        while matrix[i][j]!='_':
            i=random.choice(range(3))
            j=random.choice(range(3))
        matrix[i][j]=sign







def medium(sign,enemy):
    print("Making move level \"medium\"")
    castig=0
    pierdere=0
    for j in range(3):
        if matrix[0][j]==matrix[1][j] and matrix[0][j]==sign and matrix[2][j]=='_':
            castig=1
            poz_lin=2
            poz_col=j
            break
        if matrix[2][j]==matrix[1][j] and matrix[2][j]==sign and matrix[0][j]=='_':
            castig=1
            poz_lin=0
            poz_col=j
            break
        if matrix[0][j]==matrix[2][j] and matrix[0][j]==sign and matrix[1][j]=='_':
            castig=1
            poz_lin=1
            poz_col=j
            break
    for i in range(3):
        if matrix[i].count(sign)==2:
            for j in range(3):
                if matrix[i][j]=='_':
                    castig=1
                    poz_lin=i
                    poz_col=j
                    break
            if castig==1:
                break
        if matrix[1][1]==matrix[2][2] and matrix[2][2]==sign and matrix[0][0]=='_':
            castig=1
            poz_col=0
            poz_lin=0
        if matrix[1][1]==matrix[0][0] and matrix[0][0]==sign and matrix[2][2]=='_':
            castig=1
            poz_col=2
            poz_lin=2
        if matrix[2][2]==matrix[0][0] and matrix[0][0]==sign and matrix[1][1]=='_':
            castig=1
            poz_col=1
            poz_lin=1
        if matrix[1][1]==matrix[0][2] and matrix[0][2]==sign and matrix[2][0]=='_':
            castig=1
            poz_col=0
            poz_lin=2
        if matrix[1][1]==matrix[2][0] and matrix[2][0]==sign and matrix[0][2]=='_':
            castig=1
            poz_col=2
            poz_lin=0
        if matrix[0][2]==matrix[2][0] and matrix[2][0]==sign and matrix[1][1]=='_':
            castig=1
            poz_col=1
            poz_lin=1
    if castig==1:
        matrix[poz_lin][poz_col]=sign
    if castig==0:
        for i in range(3):
            if matrix[i].count(enemy)==2:
                for j in range(3):
                    if matrix[i][j]=='_':
                        pierdere=1
                        poz_lin=i
                        poz_col=j
                        break
                if pierdere==1:
                    break
            for j in range(3):
                if matrix[0][j]==matrix[1][j] and matrix[0][j]==enemy and matrix[2][j]=='_':
                    pierdere=1
                    poz_lin=2
                    poz_col=j
                    break
                if matrix[2][j]==matrix[1][j] and matrix[2][j]==enemy and matrix[0][j]=='_':
                    pierdere=1
                    poz_lin=0
                    poz_col=j
                    break
                if matrix[0][j]==matrix[2][j] and matrix[0][j]==enemy and matrix[1][j]=='_':
                    pierdere=1
                    poz_lin=1
                    poz_col=j
                    break
            if matrix[1][1]==matrix[2][2] and matrix[2][2]==enemy and matrix[0][0]=='_':
                pierdere=1
                poz_col=0
                poz_lin=0
            if matrix[1][1]==matrix[0][0] and matrix[0][0]==enemy and matrix[2][2]=='_':
                pierdere=1
                poz_col=2
                poz_lin=2
            if matrix[2][2]==matrix[0][0] and matrix[0][0]==enemy and matrix[1][1]=='_':
                pierdere=1
                poz_col=1
                poz_lin=1
            if matrix[1][1]==matrix[0][2] and matrix[0][2]==enemy and matrix[2][0]=='_':
                pierdere=1
                poz_col=0
                poz_lin=0
            if matrix[1][1]==matrix[2][0] and matrix[2][0]==enemy and matrix[0][2]=='_':
                pierdere=1
                poz_col=2
                poz_lin=2
            if matrix[0][2]==matrix[2][0] and matrix[2][0]==enemy and matrix[1][1]=='_':
                pierdere=1
                poz_col=1
                poz_lin=1
        if pierdere==1:
            matrix[poz_lin][poz_col]=sign
        if pierdere==0:
            i=random.choice(range(3))
            j=random.choice(range(3))
            while matrix[i][j]!='_':
                i=random.choice(range(3))
                j=random.choice(range(3))
            matrix[i][j]=sign







def hard(sign,enemy,free_spaces,Matrix):
    matrix_copy=copy.deepcopy(Matrix)
    scores=[]
    for i in range(3):
        for j in range(3):
            score=0
            if matrix_copy[i][j]=='_':
                free_spaces-=1
                matrix_copy[i][j]=sign
                if winnig(sign)==True:
                    if sign=='X' and command[1]=='hard':
                        return 10
                    if sign=='O' and command[1]=='hard':
                        return -10
                    if sign=='O' and command[2]=='hard':
                        return 10
                    if sign=='X' and command[2]=='hard':
                        return -10
                elif free_spaces>0:
                    score+=hard(enemy,sign,free_spaces,matrix_copy)
                else:
                    return 0
                scores.append(score)
            else:
                scores.append("Nothing here")
    q=max(scores)
    poz=scores.index(q)
    if poz%3!=0:
        matrix[poz/3][poz%3]=sign








while True:
    matrix=[['_','_','_'],['_','_','_'],['_','_','_']]
    afis_matrix()
    empty_space=9
    enemy_sign='O'
    player_sign='X'
    command=input("Input command:\n")
    command=list(command.split())
    if command[0]=="start" and len(command)==3 and (command[1]=='user' or command[1]=='easy' or command[1]=='medium' or command[1]=='hard') and (command[2]=='user' or command[2]=='easy' or command[2]=='medium' or command[1]=='hard'):
        while True:
            if command[1]=='user':
                user(player_sign)
            if command[1]=='easy':
                easy(player_sign)
            if command[1]=='medium':
                medium(player_sign,enemy_sign)
            if command[1]=='hard':
                hard(player_sign,enemy_sign,empty_space,matrix)
            empty_space-=1
            afis_matrix()
            if winnig(player_sign)==True:
                print("{} wins".format(player_sign))
                break
            elif empty_space==0:
                print("Draw")
                break
            if command[2]=='user':
                user(enemy_sign)
            if command[2]=='easy':
                easy(enemy_sign)
            if command[2]=='medium':
                medium(enemy_sign,player_sign)
            if command[2]=='hard':
                hard(player_sign,enemy_sign,empty_space,matrix)
            empty_space-=1
            afis_matrix()
            if winnig(enemy_sign)==True:
                print("{} wins".format(enemy_sign))
                break
            elif empty_space==0:
                print("Draw")
                break
    elif command[0]=="exit":
        break
    else:
        print("Bad parameters!")

