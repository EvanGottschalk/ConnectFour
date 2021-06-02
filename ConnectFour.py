#Defines an class representative of a Connect Four game

class ConnectFour:   

    def __init__(self):
        self.__board = [[0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0],\
                        [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0],\
                        [0,0,0,0,0,0], ]
        self.__player = -1
        self.__winner = ''
        self.__round = 0
        
    #accessor methods
    def getWinner(self):
        return self.__winner

    def getRound(self):
        return self.__round
    
    def nextPlayer(self):
        return self.__player
    
     
    #mutator methods
    def takeTurn(self, column):
        done = False
        for num in range(6):
            if done == False:
                if self.__board[column][num] == 0:
                    self.__board[column][num] = self.__player
                    done = True
                    row = num
        self.__round += 1
        if self.__player == 1:
            self.__player = -1
        else:
            self.__player = 1
        return(row)

    #checks if a column is full
    def columnOpen(self, column):
        if self.__board[column].count(0) != 0:
            return True

    #looks for four in a row
    def winner(self):        
        for column in self.__board:
            for cell in range(3):
                if column[cell] == 1:
                    if column[cell+1] + column[cell+2] + column[cell+3] == 3:
                        self.__winner = 'Black'
                        return(True)
                elif column[cell] == -1:
                    if column[cell+1] + column[cell+2] + column[cell+3] == -3:
                        self.__winner = 'Red'
                        return(True)
        for num in range (6):
            for column in range(4):
                if self.__board[column][num] == 1:
                    if self.__board[column+1][num] + self.__board[column+2][num]\
                    + self.__board[column+3][num] == 3:
                        self.__winner = 'Black'
                        return(True)
                elif self.__board[column][num] == -1:
                    if self.__board[column+1][num] + self.__board[column+2][num]\
                    + self.__board[column+3][num] == -3:
                        self.__winner = 'Red'
                        return(True)
        for column in range(4):
            for row in range(6):
                if row < 3:
                    if self.__board[column][row] == 1:
                        if self.__board[column+1][row+1]\
                        + self.__board[column+2][row+2]\
                        + self.__board[column+3][row+3] == 3:
                            self.__winner = 'Black'
                            return(True)
                    elif self.__board[column][row] == -1:
                        if self.__board[column+1][row+1]\
                        + self.__board[column+2][row+2]\
                        + self.__board[column+3][row+3] == -3:
                            self.__winner = 'Red'
                            return(True)
                else:
                    if self.__board[column][row] == 1:
                        if self.__board[column+1][row-1]\
                        + self.__board[column+2][row-2]\
                        + self.__board[column+3][row-3] == 3:
                            self.__winner = 'Black'
                            return(True)
                    elif self.__board[column][row] == -1:
                        if self.__board[column+1][row-1]\
                        + self.__board[column+2][row-2]\
                        + self.__board[column+3][row-3] == -3:
                            self.__winner = 'Red'
                            return(True)
        return(False)

    #creates a text version of the board
    def __str__(self):
        boardString = ''
        for num in range(6):
            rowString = ('|  %i  |  %i  |  %i  |  %i  |  %i  |  %i  |  %i  |\n'\
                         % (self.__board[0][5-num], self.__board[1][5-num],\
                            self.__board[2][5-num], self.__board[3][5-num],\
                            self.__board[4][5-num], self.__board[5][5-num],\
                            self.__board[6][5-num]))
            boardString += rowString
        return(boardString)
