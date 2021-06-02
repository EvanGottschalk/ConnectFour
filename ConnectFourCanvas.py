#Creates a Connect Four game board which the game can be played on

from tkinter import *
import ConnectFour

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
        mainloop()
        
    #creates the canvas the game is played on
    def createConnectFourBoard(self):
        board = Canvas(self.root, height = 600, width = 700, bg = 'yellow')
        board.pack()
        board.create_line(6,0,6,600, width = 7, fill = 'blue')
        board.create_line(100,0,100,600, width = 3)
        board.create_line(200,0,200,600, width = 3)
        board.create_line(300,0,300,600, width = 3)
        board.create_line(400,0,400,600, width = 3)
        board.create_line(500,0,500,600, width = 3)
        board.create_line(600,0,600,600, width = 3)
        board.create_line(698,0,698,600, width = 7, fill = 'blue')
        board.create_line(0,100,700,100, width = 3)
        board.create_line(0,200,700,200, width = 3)
        board.create_line(0,300,700,300, width = 3)
        board.create_line(0,400,700,400, width = 3)
        board.create_line(0,500,700,500, width = 3)
        for column in range(6):
            for row in range(7):
                x = row * 100 + 50
                y = column * 100 - 75
                board.create_text(x, y, text = '.', fill = 'white',\
                                  font = 'Times 350 bold')
        return(board)

    #drops the player's piece into the column
    def recordPlay(self, column, row):
        y = (5 - row) * 100 - 75
        x = column * 100 + 50
        if self.game.nextPlayer() == -1:
            self.board.create_text(x, y, text = '.', font = 'Times 350 bold')
        else:
            self.board.create_text(x, y, text = '.', fill = 'red',\
                                   font = 'Times 350 bold')

    #determines the column that the user clicked in
    def whichColumn(self, x):
        column = x // 100
        return column

    #restarts the game        
    def newGame(self):
        self.game = ConnectFour.ConnectFour()
        self.board.destroy()
        self.board = self.createConnectFourBoard()
        self.board.grid(row = 0, columnspan = 2)
        self.board.bind('<Button-1>', self.move)
        self.message.config(text = 'Red moves first')

    #makes all the changes execute that occur when a player takes her turn
    def move(self, event):
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
        else:
            messagebox.showerror('Invalid Move', 'You must click an open column.')

ConnectFourCanvas()
