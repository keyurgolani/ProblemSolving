import random
import itertools

class Board(object):
    def __init__(self, player1, player2):
        self.elements = [None] * 3
        for i in range(3):
            row = [None] * 3
            for j in range(3):
                row[j] = State()
            self.elements[i] = row
        self.player1 = {
            "name" : player1,
            "token": State.getToken(1),
            "object": Bot(State.getToken(1))
        }
        self.player2 = {
            "name": player2,
            "token": State.getToken(2),
            "object": Player(State.getToken(2))
        }

    def __str__(self):
        ret_str = ""
        for row in self.elements:
            ret_str += ("|".join([str(x) for x in row])) + "\n"
        return ret_str

    def checkWin(self):
        return None

    def makeMove(self, token, x, y):
        self.elements[x][y].makeToken(token)
        self.checkWin()

    def getState(self, x, y):
        return self.elements[x][y]

    def isAvailable(self, x, y):
        return self.elements[x][y].isAvailable()

    def getNextPlayer(self):
        for player in itertools.cycle([self.player1, self.player2]):
            yield player
        

    def declareResult(self):
        winner = self.checkWin()
        if winner == "Draw":
            print "=" * 40
            print "Congratulations! It's a draw."
            print "=" * 40
        elif winner == "Player 1":
            print "=" * 40
            print "The Bot won. Better luck next time."
            print "=" * 40
        else:
            print "=" * 40
            print "Congratulations! You beat the bot."
            print "=" * 40

    def play(self):
        print "=" * 20
        print str(self)
        print "=" * 20
        while not self.checkWin():
            self.getNextPlayer().next()["object"].makeMove(self)
            print "=" * 20
            print str(self)
            print "=" * 20
        else:
            self.declareResult()


class State(object):

    @staticmethod
    def getStates():
        return {
            "-": 0,
            "O": 1,
            "X": 2
        }

    @staticmethod
    def getTokens():
        return dict([(value, key) for (key, value) in State.getStates().items()])

    @staticmethod
    def getState(token):
        return State.getStates()[token]

    @staticmethod
    def getO():
        return State.getToken(1)

    @staticmethod
    def getX():
        return State.getToken(2)

    @staticmethod
    def getToken(state):
        return State.getTokens()[state]

    def __init__(self):
        self.state = 0

    def token(self):
        return State.getToken(self.state)

    def makeToken(self, token):
        self.state = State.getState(token)

    def __str__(self):
        return self.token()

    def isAvailable(self):
        return self.state == 0

class Player(object):
    def __init__(self, token):
        self.token = token

    def makeMove(self, board):
        while True:
            print "Enter index to the cell you want to play at seperated by space"
            try:
                x, y = map(int, raw_input().split(" "))
            except Exception:
                print "Invalid Input. Please try again."
            else:
                if board.isAvailable(x, y):
                    board.makeMove(self.token, x, y)
                    break
                else:
                    print "The cell is already explored. Choose another one."

class Bot(object):
    def __init__(self, token):
        self.token = token

    def makeMove(self, board):
        while True:
            move = random.randint(0, 8)
            x, y = move/3, move%3
            if board.isAvailable(x, y):
                board.makeMove(self.token, x, y)
                break


def main():
    b = Board("Keyur", "John")
    b.play()

if __name__ == '__main__':
    main()