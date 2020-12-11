table = [
         ["BR", "BH", "BB", "BQ", "BK", "BB", "BH", "BR"],
         ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP"],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP"],
         ["WR", "WH", "WB", "WQ", "WK", "WB", "WH", "WR"]]
showing_table = [
         ["BR", "BH", "BB", "BQ", "BK", "BB", "BH", "BR"],
         ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP"],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP"],
         ["WR", "WH", "WB", "WQ", "WK", "WB", "WH", "WR"]]


class Play_game():
    def __init__(self):
        self.win=False
        self.turn = "W"
        self.next_turn = "B"
        self.turn_multiply = 1
        self.rook_plays =False
        self.king_plays = False
        self.choose_to_side()

    def change_turn(self):

        if self.turn == "W":  # if WHITE user played now it is changing with BLACK
            self.turn = "B"
            self.next_turn = "W"
            self.turn_multiply = -1  # this is for about algoritm to make easier
            print("BLACK TURNS !!!!!")

        elif self.turn == "B":  # if BLACK user played now it is changing with WHITE
            self.turn = "W"
            self.next_turn = "B"
            self.turn_multiply = 1
            print("WHITE TURNS !!!!!")

    def pawn(self,x_1,y_1,x_2,y_2):

        #   Algorithm for pawn moving
        if table[x_2][y_2] == "  " and y_1 == y_2 and table[x_1][y_1][0] == self.turn:
            print(x_1)
            print(self.turn_multiply,x_1,x_2+(2*self.turn_multiply))
            if x_1 == 6 or x_1==1:
                if x_1 == x_2+(2*self.turn_multiply) or x_1 == x_2+1*self.turn_multiply:

                    #  if everything is ok . Under of this gonna work and selected rock will go second inputs side
                    if table[x_1 - 1*self.turn_multiply][y_2] == "  " and table[x_2][y_2] == "  ":
                        table[x_1][y_1] = "  "
                        table[x_2][y_2] = self.turn + "P"
                        self.change_turn()
            else:

                #  if everything is ok . Under of this gonna work and selected rock will go second inputs side
                if x_1 - 1*self.turn_multiply == x_2 and table[x_2][y_2] == "  ":
                    table[x_1][y_1] = "  "
                    table[x_2][y_2] = self.turn+"P"
                    self.change_turn()

        elif y_1 != 0 and y_1 !=7 and( y_2 == y_1+1 or y_2 == y_1-1 )and table[x_2][y_2] != "  ":
            #  if everything is ok . Under of this gonna work and selected rock will go second inputs side
            table[x_1][y_1] = "  "
            table[x_2][y_2] = self.turn + "P"
            self.change_turn()   # this one is change the player who is turn after moving

        elif y_1 == 0 or y_1 ==7 and y_1 !=y_2:
            if y_1 == 0 and (y_2 == y_1 + 1) and table[x_2][y_2] != "  ":

                #  if everything is ok . Under of this gonna work and selected rock will go second inputs side
                table[x_1][y_1] = "  "
                table[x_2][y_2] = self.turn + "P"
                self.change_turn()  # this one is change the player who is turn after moving

            elif y_1 == 7 and (y_2 == y_1 - 1) and table[x_2][y_2] != "  ":

                #  if everything is ok . Under of this gonna work and selected rock will go second inputs side
                table[x_1][y_1] = "  "
                table[x_2][y_2] = self.turn + "P"
                self.change_turn()  # this one is change the player who is turn after moving

    def horse(self,x_1,y_1,x_2,y_2):
        # This code is a lit bit gives error still not correct
        if table[x_1][y_1][0] == self.turn and table[x_2][y_2][0] != self.turn:
            if (y_1 + 2 == y_2 and (x_1 + 1 == x_2 or x_1 - 1 == x_2)) or (y_1 - 2 == y_2 and (x_1 + 1 == x_2 or x_1 - 1 == x_2)) or (x_1 - 2 == x_2 and (y_1 + 1 == y_2 or y_1 - 1 == y_2)) or (x_1 + 2 == x_2 and (y_1 + 1 == y_2 or y_1 - 1 == y_2)):
                table[x_1][y_1] = "  "
                table[x_2][y_2] = self.turn + "H"
                self.check_control()  # check control
                self.change_turn()  # change turn other player to play

    def bishop(self, x_1, y_1, x_2, y_2):
        clear=True
        # algorithm makes moving to bishop to play cross
        if (x_2-x_1)**2 == (y_2-y_1)**2:
            dy_1 = 0  # this is default
            dy_2 = 0  # this is default
            k = 1   # this is default
            if table[x_1][y_1][0] == self.turn and table[x_2][y_2][0] != self.turn:
                if x_1 > x_2:
                    dx_1 = x_1-1
                    dx_2 = x_2
                    k = -1
                    if y_1> y_2:
                        temp = y_1
                        dy_1 = y_2
                        dy_2 = temp -1
                        k = 1
                    elif y_2> y_1:
                        dy_1 = y_1 + 1
                        dy_2 = y_2
                        k=1
                    for i,j in zip(range(dx_1,dx_2,k),range(dy_1,dy_2,k)):
                        print(i,j)
                        if table[i][j][0] != " ":
                            clear = False
                    if clear == True:
                        table[x_1][y_1] = "  "
                        table[x_2][y_2] = self.turn + "B"
                        self.check_control()  # check control
                        self.change_turn()  # change turn other player to play

                elif x_2> x_1:
                    dx_1 = x_1+1
                    dx_2 = x_2
                    if y_1> y_2:
                        dy_1 = y_1 - 1
                        dy_2 = y_2
                        k = -1
                    elif y_2> y_1:
                        dy_1 = y_1+ 1
                        dy_2 = y_2
                        k = 1
                    for i,j in zip(range(dx_1,dx_2),range(dy_1,dy_2,k)):
                        if table[i][j][0] != " ":
                            print(table[i][j][0])
                            clear = False
                    if clear == True:
                        table[x_1][y_1] = "  "
                        table[x_2][y_2] = self.turn + "B"
                        self.check_control()  # check control
                        self.change_turn()  # change turn other player to play

    def rook(self, x_1, y_1, x_2, y_2):
        clear = True
        rooks_plays = True  # this is for make roke to player but there is problem if user play just one rook and he wants to make roke with ather rook it is not able to make roke with other one

        if x_1 == x_2 or y_1 == y_2 :
            if (table[x_2][y_2] == "  " or table[x_2][y_2][0]!= self.turn) and table[x_1][y_1][0] == self.turn and table[x_2][y_2][0] != self.turn :
                if x_1 == x_2:
                    k=1
                    d_1 = y_1 + 1
                    d_2 = y_2
                    if y_1 > y_2 :
                        temp = y_1
                        d_1 = y_2+1
                        d_2 = temp
                    for i in range(d_1,d_2):
                        if table[x_1][i][0] != " ":
                            clear = False

                    if clear == True:
                        table[x_1][y_1] = "  "
                        table[x_2][y_2] = self.turn + "R"
                        self.check_control()
                        self.change_turn()
                elif y_1 == y_2:
                    d_1= x_1 +1
                    d_2 = x_2
                    if x_1 > x_2 :
                        temp = x_1
                        d_1 = x_2+1
                        d_2 = temp
                    for i in range(d_1,d_2):
                        if table[i][y_2][0] != " ":  # if there is not empty between first input and second input User cannat play
                            clear = False

                    if clear == True:
                        table[x_1][y_1] = "  "
                        table[x_2][y_2] = self.turn + "R"
                        self.check_control()
                        self.change_turn()

    def queen(self, x_1, y_1, x_2, y_2):
        # THIS checks code between first input and second input , if it is TRUE ,user can play if it turns false , User can not play
        clear = True
        if (x_2 - x_1) ** 2 == (y_2 - y_1) ** 2:
            dy_1 = 0
            dy_2 = 0
            k = 1
            if table[x_1][y_1][0] == self.turn and table[x_2][y_2][0] != self.turn:
                if x_1> x_2:
                    dx_1 = x_1-1
                    dx_2 = x_2
                    k = -1
                    if y_1> y_2:
                        temp = y_1
                        dy_1 = y_2
                        dy_2 = temp -1
                        k = 1
                    elif y_2> y_1:
                        dy_1 = y_1 + 1
                        dy_2 = y_2
                        k=1
                    for i,j in zip(range(dx_1,dx_2,k),range(dy_1,dy_2,k)):
                        if table[i][j][0] != " ":
                            clear = False
                    if clear == True:
                        table[x_1][y_1] = "  "
                        table[x_2][y_2] = self.turn + "Q"
                        self.check_control()
                        self.change_turn()
                elif x_2> x_1:
                    dx_1 = x_1+1
                    dx_2 = x_2
                    if y_1> y_2:
                        dy_1 = y_1 - 1
                        dy_2 = y_2
                        k = -1
                    elif y_2> y_1:
                        dy_1 = y_1+ 1
                        dy_2 = y_2
                        k = 1
                    for i,j in zip(range(dx_1,dx_2),range(dy_1,dy_2,k)):
                        if table[i][j][0] != " ":
                            clear = False
                    if clear == True:
                        table[x_1][y_1] = "  "
                        table[x_2][y_2] = self.turn + "Q"
                        self.check_control()
                        self.change_turn()


        elif x_1 == x_2 or y_1 == y_2:
            if (table[x_2][y_2] == "  " or table[x_2][y_2][0] != self.turn) and table[x_1][y_1][0] == self.turn and \
                    table[x_2][y_2][0] != self.turn:
                if x_1 == x_2:
                    k = 1
                    d_1 = y_1 + 1
                    d_2 = y_2
                    if y_1 > y_2:
                        temp = y_1
                        d_1 = y_2 + 1
                        d_2 = temp
                    for i in range(d_1, d_2):

                        if table[x_1][i][0] != " ":
                            clear = False

                    if clear == True:
                        table[x_1][y_1] = "  "
                        table[x_2][y_2] = self.turn + "Q"
                        self.check_control()
                        self.change_turn()
                elif y_1 == y_2:
                    d_1 = x_1 + 1
                    d_2 = x_2
                    if x_1 > x_2:
                        temp = x_1
                        d_1 = x_2 + 1
                        d_2 = temp
                    for i in range(d_1, d_2):
                        print(i, y_2)
                        if table[i][y_2][0] != " ":
                            clear = False
                    if clear == True:
                        table[x_1][y_1] = "  "
                        table[x_2][y_2] = self.turn + "Q"
                        self.check_control()
                        self.change_turn()

    def king(self, x_1, y_1, x_2, y_2):
        if (table[x_2][y_2] == "  " or table[x_2][y_2][0] != self.turn) and table[x_1][y_1][0] == self.turn :
            if x_2 == x_1+1 or x_2 == x_1-1 or y_2 == y_1+1 or y_2 == y_1 - 1 or(x_2 == x_1+1 and y_2 == y_1+1) or(x_2 == x_1+ 1 and y_2 == y_1-1) or(x_2 == x_1-1 and y_2 == y_1+1) or(x_2 == x_1-1 and y_2 == y_1-1):
                self.check_control()
                if self.check == False:
                    table[x_1][y_1] = "  "
                    table[x_2][y_2] = self.turn + "K"

        elif table[x_2][y_2] == self.next_turn + "R" and self.king_plays == False and self.rook_plays == False:
            if x_1==x_2 and y_1 > y_2:
                for i in range(y_1-1 + y_2, -1):
                    if table[x_1][i] == self.next_turn + "R" and self.rook_plays == False:
                        table[x_1][y_1] = "  "
                        table[x_2][y_2] = "  "
                        table[x_1][2] = self.next_turn + "K"
                        table[x_1][3] = self.next_turn + "R"
                    elif table[x_1][i] != "  ":
                        break
            elif x_1 == x_2 and y_2 > y_1:
                for i in range(y_1 + 1 + y_2+1):
                    if table[x_1][i] == self.next_turn + "R" and self.rook_plays == False:
                        table[x_1][y_1] = "  "
                        table[x_2][y_2] = "  "
                        table[x_1][6] = self.next_turn + "K"
                        table[x_1][5] = self.next_turn + "R"
                    elif table[x_1][i] != "  ":
                        break

        self.king_plays = True

    def check_control(self):
        self.check = False
        self.rook_clear = False
        self.bishop_clear = False
        if self.turn == "W":
            self.next_turn ="B"
        elif self.turn == "B":
            self.next_turn = "W"
        for i in range(0,len(table)):
            for j,y in zip(table[i],range(0,len(table[i]))):
                if j == self.next_turn+ "K":
                    self.yeri = [i,y]
        x = int(self.yeri[0])
        y = int(self.yeri[1])
        #  Horse Control
        if self.rock == "H":
            if table[x+2][y+1] ==self.turn+"H" or table[x+2][y-1] ==self.turn+"H"or table[x-2][y+1] ==self.turn+"H"or table[x-2][y-1]==self.turn+"H" or table[x+1][y+2] ==self.turn+"H"or table[x+1][y-2]==self.turn+"H" or table[x-1][y+2]==self.turn+"H" or table[x-1][y-2]==self.turn+"H":
                print("check",self.next_turn)
                self.check = True
        #  Rook Control
        for i in range(x-1,-1,-1):
            if table[i][y] == self.turn+"R" or table[i][y] == self.turn + "Q":
                self.rook_clear=True
                self.check = True
            elif table[i][y] != "  " :
                break

        for i in range(x+1,8):
            if table[i][y] == self.turn + "R" or table[i][y] == self.turn + "Q":
                self.rook_clear = True
                self.check = True
            elif table[i][y] != "  " :
                break


        for i in range(y-1,-1,-1):
            if table[x][i] == self.turn + "R" or table[x][i] == self.turn + "Q":
                self.rook_clear = True
                self.check = True
            elif table[x][i] != "  " :
                break


        for i in range(y+1,8):
            if table[x][i] == self.turn + "R" or table[x][i] == self.turn + "Q":
                self.rook_clear = True
                self.check = True
                break
            elif table[x][i] != "  ":
                break


        # if self.rook_clear == True:
        #     print("CHECK FROM ROCK !!!")
        # -------------------------------------- for rock

        #  Bishop Control
        num1 = y
        num2 = y
        for i in range(x-1,-1,-1):
            print("eksili",i)
            num1 = num1 + 1
            num2 = num2 - 1
            if num1 < 8 :
                if table[i][num1] == self.turn+"B" or table[i][num1] ==self.turn + "Q":
                    self.bishop_clear=True
                    self.check = True
                    break
                elif (table[i][num1] == "  " ):
                    continue
                else:
                    break
            elif num2 >0:
                if table[i][num2] == self.turn+"B" or table[i][num2] ==self.turn + "Q":
                    self.check = True
                    self.bishop_clear=True
                    break
                elif ( table[i][num2] == "  " ):
                    continue
                else:
                    break
        num1 = y
        num2 = y
        for i in range(x+1,8):
            num1 = num1 + 1
            num2 = num2 - 1
            if num1 < 8 :
                if table[i][num1] == self.turn + "B" or table[i][num1] ==self.turn + "Q":
                    self.bishop_clear = True
                    self.check = True
                    break
                elif (table[i][num1] == "  " ):
                    continue
                else:
                    break
            elif num2 >0:
                if table[i][num2] == self.turn + "B" or table[i][num2] ==self.turn + "Q":
                    self.check = True
                    self.bishop_clear = True
                    break
                elif table[i][num2] == "  ":
                    continue
                else:
                    break
        num1 = x
        num2 = x
        for i in range(y-1,-1,-1):
            num1 = num1 + 1
            num2 = num2 - 1
            if num1 < 8 :
                if table[num1][i] == self.turn + "B" or table[num1][i] ==self.turn + "Q":
                    self.check = True
                    self.bishop_clear = True
                    break
                elif table[num1][i] == "  " :
                    continue
                else:
                    break

            elif num2 >-1:
                if table[num2][i] == self.turn + "B" or table[num2][i] ==self.turn + "Q":
                    self.check = True
                    self.bishop_clear = True
                    break
                elif table[num2][i] == "  ":
                    continue
                else:
                    break
        num1 = x
        num2 = x
        for i in range(y+1,8):
            num1 = num1 + 1
            num2 = num2 - 1
            if num1 < 8 :
                if table[num1][i] == self.turn + "B" or table[num1][i] ==self.turn + "Q":
                    self.check = True
                    self.bishop_clear = True
                    break
                elif table[num1][i] == "  " :
                    continue
                else:
                    break
            elif num2 >0 :
                if table[num2][i] == self.turn + "B" or table[num2][i] ==self.turn + "Q":
                    self.check = True
                    self.bishop_clear = True
                    break
                elif table[num2][i] == "  ":
                    continue
                else:
                    break
        if self.rook_clear == True and self.bishop_clear == False:
            print("CHECK FROM ROCK !!!")
        elif self.bishop_clear == True and self.rook_clear == False:
            print("CHECK !!! from BISHOP" )
        elif self.bishop_clear == True and self.rook_clear == True:
            print("CHECK !!! from QUEEN" )
        # ------------------------------------- for bishop

        #  Queen Control


    def getting(self,first, second):
        # some algorithm to get eaier side to make more comfortable code
        x_1 = 8-int(first[1])
        y_1 = int(first[0])
        x_2 = 8-int(second[1])
        y_2 = int(second[0])

        pos_1 = table[8-int(first[1])][int(first[0])]
        to_pos_2 = table[8-int(second[1])][int(second[0])]

        if pos_1 == "  ":
            #  if user select empty spot to play ask user again to play another spot
            print("your choosing side is not available (there is no any chess piece)")
            self.choose_to_side()

        else:
            turn = pos_1[0]

            # PAWNS moves
            if pos_1[1] == "P":
                print("PAWN was selected")
                self.rock = "P"
                self.pawn(x_1,y_1,x_2,y_2)

            # ROOK moves
            elif pos_1[1] == "R":
                print("ROOK was selected")
                self.rock = "R"
                self.rook(x_1,y_1,x_2,y_2)

            # HORSE moves
            elif pos_1[1] == "H":
                print("HORSE was selected")
                self.rock = "H"
                self.horse(x_1,y_1,x_2,y_2)

            # BISHOP moves
            elif pos_1[1] == "B":
                print("BISHOP was selected")
                self.rock = "B"
                self.bishop(x_1,y_1,x_2,y_2)

            # QUEEN moves
            elif pos_1[1] == "Q":
                print("QUEEN was selected")
                self.rock = "Q"
                self.queen(x_1,y_1,x_2,y_2)

            # KING moves
            elif pos_1[1] == "K":
                print("KING was selected")
                self.king(x_1,y_1,x_2,y_2)

    def choose_to_side(self):
        cols = ["a", "b", "c", "d", "e", "f", "g", "h"]
        cols_reverse = ["8", "7", "6", "5", "4", "3", "2", "1"]
        while self.win == False:
            try:
                # here is for showing to playing gameboard to player can able to play
                showing_table = table
                for i,j in zip(showing_table,cols_reverse):
                    print(end="{} ".format(j))
                    element = i
                    for count, element in enumerate(i,0):
                        element= element.replace("BR","♜|").replace("BH","♞|").replace("BB","♝|").replace("BQ","♛|").replace("BK","♚|").replace("BP","♟|").replace("WR","♖|").replace("WH","♘").replace("WB","♗").replace("WQ","♕|").replace("WK","♔|").replace("WP","♙|").replace("  "," |")
                        print(element,end=" ")
                    print("")
                print(" ", "A ", "B ", "C", "D ", "E ", "F ", "G", "H ")
                # -----------------------------------------------------------------------
                first = input("first side ")  # first side inputs is  which spot to select your rock,for playing
                first_column = first[0]

                first_row = first[1]
                second = input("second side ")  # second side input is choosing for playing your rock to where

                second_column = second[0]
                second_row = second[1]
                # for first pick
                first = str(cols.index(first_column)) + str(first_row)
                # for second pick
                second = str(cols.index(second_column)) + str(second_row)
                self.getting(first, second)
            except ValueError:
                # if you who is player get something wrong to play . it asks again
                print("your selected side is not available")

    #  side = input("choose your side WHITE(W) , BLACK(B) or RANDOM(R)")

Play_game()


