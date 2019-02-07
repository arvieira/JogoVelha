class Board:
    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.session = 0
        self.playerNumber = 0
        self.cpuNumber = 0

    def setSession(self, session):
        self.session = session

    def getSession(self):
        return self.session

    def setPlayerNumber(self, playerNumber):
        self.playerNumber = playerNumber

    def getPlayerNumber(self):
        return self.playerNumber

    def setCpuNumber(self, cpuNumber):
        self.cpuNumber = cpuNumber

    def getCpuNumber(self):
        return self.cpuNumber

    def setPosition (self, position, player):
        if (type(position) == tuple and
            position[0] >= 0 and position[0] <= 2 and
            position[1] >= 0 and position[1] <= 2):
            if (self.board[position[0]][position[1]] == 0):
                self.board[position[0]][position[1]] = player
                return True
            else:
                print ("Posição já ocupada. Escolha outra.")
                return False
        else:
            print ("Uso inválido")
            return False

    def showBoard (self):
        print ("STATUS")
        print (self.board[0][0], " | ", self.board[0][1], " | ", self.board[0][2])
        print ("-------------")
        print (self.board[1][0], " | ", self.board[1][1], " | ", self.board[1][2])
        print ("-------------")
        print (self.board[2][0], " | ", self.board[2][1], " | ", self.board[2][2])
        print ()