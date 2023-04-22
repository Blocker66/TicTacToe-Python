import os
import consolecolors
# board = ["" for _ in range(9)]
# board[0] = "X"
# board[5] = "O"
# displayedBoard = "\
# -----------------\n" + \
# "|  " + board[0] + "  |  " + board[1] + "  |  " +  board[2] + "  |\n" +\
# "-----------------\n" + \
# "|  " + board[3] + "   |  " + board[4] + "  |  " +  board[5] + "  |\n" +\
# "-----------------\n" + \
# "|  " + board[6] + "  |  " + board[7] + "  |  " +  board[8] + "  |" +\
# "-------------------\n"
clear = lambda: os.system('clear')

class Tictactoe:
    def __init__(self):
        self.rowLabels = "abc"
        self.columnLabels = "123"

        self.board = [" " for _ in range(9)]
        self.displayedBoard = self.updateDisplayBoard(self.board)
        self.playerXUp = True
        self.running = True
        
        self.legalMoves = [row + column for column in self.columnLabels for row in self.rowLabels]
        self.moveToBoardIndex = {self.legalMoves[i]: self.legalMoves.index(self.legalMoves[i]) for i in range(9)}

    def updateDisplayBoard(self, board):
        # Account for offset due to labeling of rows
        lid = " " *3 + "-" * 19
        displayBoard = "      " 
        for i in range(3):
            displayBoard += self.rowLabels[i] + " "*5

        displayBoard += "\n" + lid + "\n"
        for i in range(9):
            gap = " " * 2
            box = "|" + gap + board[i] + gap
            if i % 3 == 0:
                # When will you use algebra, haha. The relation (0, 1), (3, 2), (6, 9), or 
                # (index of box, row number adjacent to box), can be modeled by the equation (1/3)x + 1.
                # We use // or the floor division operator as we want integers, not floats.
                box = str(i//3 + 1) + gap + box
            displayBoard += box

            # If the box is located at the end of the board (i = 2, 5, or 8), we need to close the box off, 
            # then jump to a new line and close the row off with a lid. 
            # Then we need to jump to a new line to create a another row or if we are at the last box, just end the row.
            if i % 3 == 2 and i < 8:
                displayBoard += "|\n" + lid + "\n" 
                continue
            elif i == 8:
                displayBoard += "|\n" + lid
        return displayBoard
    
    def validMove(self, move):
        if (len(move) != 2 or move not in self.legalMoves):
            return False
        elif (self.board[self.moveToBoardIndex[move]] != " "):
            return False
        
        return True

    def getMove(self):
        move = input("What is your move?\n")
        if (not self.validMove(move)):
            validResponse = False
            while not validResponse:
                clear()
                print(self.displayedBoard)
                print("Invalid Move")
                move = input("What is your move?\n")
                validResponse = move in self.legalMoves        
        return move

    

        return True
    def updateBoard(self, move):
        marker = "X" if self.playerXUp else "O"
        self.board[self.moveToBoardIndex[move]] = marker
        self.displayedBoard = self.updateDisplayBoard(self.board)
        
    def checkWin(self):
        winningPositions = [
            [0,1,2],
            [3,4,5],
            [6,7,8],
            [0,3,6],
            [1,4,7],
            [2,5,8],
            [0,4,8],
            [2,4,6]
        ]
        
        for winningPos in winningPositions:
            if self.board[winningPos[0]] == self.board[winningPos[1]] == self.board[winningPos[2]] and self.board[winningPos[1]] != " ":
                print(self.displayedBoard)
                print(f"Player {self.board[winningPos[0]]} won!")
                self.restart()

    def checkTie(self):
        emptySpacesOnBoard = list(filter(lambda move: move ==" ", self.board))
        if len(emptySpacesOnBoard) == 0:
            print(self.displayedBoard)
            print("Tie!")
            self.restart()
    
    def restart(self):
        response = input("Do you want to restart (y/n)\n")
        validAnswers = (("y", "yes"), ("n", "no"))
        if (response.lower() not in validAnswers[0] and response.lower() not in validAnswers[1]):
            validResponse = False
            while not validResponse:
                clear()
                print(self.displayedBoard)
                print("Invalid answer")
                response = input("Do you want to restart (y/n)\n")
                validResponse = response.lower() in validAnswers[0] or response.lower() in validAnswers[1]
                
        doRestart = True if response in validAnswers[0] else False
        if doRestart:
            self.board = [" " for _ in range(9)]
            self.displayedBoard = self.updateDisplayBoard(self.board)
        
        else:
            print("Hope you enjoyed!")
            self.running = False
        
        

                

    def run(self):
        while self.running:
            print(self.displayedBoard)
            move = self.getMove()
            clear()
            self.updateBoard(move)
            self.checkWin()
            self.checkTie()
            self.playerXUp = not self.playerXUp

    

game = Tictactoe()
game.run()
print
