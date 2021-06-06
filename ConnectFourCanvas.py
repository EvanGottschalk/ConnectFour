#Creates a Connect Four game board which the game can be played on

from tkinter import *
import ConnectFour

import time

class ConnectFourCanvas:

    #creates the game object
    def __init__(self):
        self.root = Tk()
        self.root.title('Connect Four')        
        self.game = ConnectFour.ConnectFour()
        self.board = self.createConnectFourBoard()
        self.board.bind('<Button-1>', self.move)
        self.board.grid(row = 0, columnspan = 2)
        self.newGame = Button(self.root, text ='New Game', bg = 'green',\
                              font = 'Times 18 bold', command = self.newGame)
        self.newGame.grid(row = 1, column = 1)
        self.message = Label(self.root, text = 'Red moves first', fg = 'red',\
                             bg = 'pink', font = 'Times 22 bold', width = 33)        
        self.message.grid(row = 1, column = 0)
    # allow_input was added when the falling animation was added
    # It is set to False while the animation is being executed to prevent the mixing-up of moves
        self.allow_input = True
        mainloop()
        
    #creates the canvas the game is played on
    def createConnectFourBoard(self):
        self.board = Canvas(self.root, height = 600, width = 700, bg = 'yellow')
        self.board.pack()
        self.board.create_line(6,0,6,600, width = 7, fill = 'blue')
        self.board.create_line(100,0,100,600, width = 3)
        self.board.create_line(200,0,200,600, width = 3)
        self.board.create_line(300,0,300,600, width = 3)
        self.board.create_line(400,0,400,600, width = 3)
        self.board.create_line(500,0,500,600, width = 3)
        self.board.create_line(600,0,600,600, width = 3)
        self.board.create_line(698,0,698,600, width = 7, fill = 'blue')
        self.board.create_line(0,100,700,100, width = 3)
        self.board.create_line(0,200,700,200, width = 3)
        self.board.create_line(0,300,700,300, width = 3)
        self.board.create_line(0,400,700,400, width = 3)
        self.board.create_line(0,500,700,500, width = 3)
        self.clearBoard()
        return(self.board)

# This function animates the taking of a player's turn, in which the player drops a piece of their color into a column
    def recordPlay(self, column, row):
    # This for loop was added to create a falling animation to the player's turns. 6/5/21
        self.allow_input = False
        for num in range(row, 6):
        # This places a white dot on the boardm, which hide the prior temporary colored dot
            y = (num - row - 1) * 100 - 75
            x = column * 100 + 50
            self.board.create_text(x, y, text = '.', fill = 'white',\
                                         font = 'Times 350 bold')
        # This places a colored dot on the board
        # When num < 5, this is placing a dot temporarily to create a falling animation. It will get covered by a white dot next time in the for loop
        # When num == 5, this is placing final dot represeting the player's actual move
            y = (num - row) * 100 - 75
            x = column * 100 + 50
            if self.game.nextPlayer() == -1:
                self.board.create_text(x, y, text = '.', font = 'Times 350 bold')
            else:
                self.board.create_text(x, y, text = '.', font = 'Times 350 bold', fill = 'red')
            self.board.update()
            time.sleep(.015)
        self.allow_input = True

    #determines the column that the user clicked in
    def whichColumn(self, x):
        column = x // 100
        return column

    #restarts the game        
    def newGame(self):
        if self.allow_input:
            self.game = ConnectFour.ConnectFour()
            self.clearBoard()
            self.message.config(text = 'Red moves first')

    #makes all the changes execute that occur when a player takes her turn
    def move(self, event):
        if self.allow_input:
            column = self.whichColumn(event.x)
            if self.game.columnOpen(column):
                row = self.game.takeTurn(column)
                self.recordPlay(column, row)
                if self.game.winner():
                    self.message.config(text = 'Connect Four! '\
                                        + self.game.getWinner() + ' wins!')
                elif not(self.game.columnOpen(0) or self.game.columnOpen(1)\
                         or self.game.columnOpen(2) or self.game.columnOpen(3)\
                         or self.game.columnOpen(4) or self.game.columnOpen(5)\
                         or self.game.columnOpen(6)):
                    self.message.config(text = 'Stalemate! The game ends in a draw!')
                else:
                    if self.game.nextPlayer() == 1:
                        self.message.config(text = '''Black's move''', fg = 'black')
                    else:
                        self.message.config(text = '''Red's move''', fg = 'red')

# This function "clears the board", removing all players' pieces and replacing them with empty white spots. 6/5/21
    def clearBoard(self):
        for column in range(6):
            for row in range(7):
                x = row * 100 + 50
                y = column * 100 - 75
                self.board.create_text(x, y, text = '.', fill = 'white', font = 'Times 350 bold')
    
ConnectFourCanvas()
