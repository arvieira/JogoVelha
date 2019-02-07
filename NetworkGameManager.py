import requests
import json
import Board


class NetworkGameManager:
    def __init__(self):
        self.startPayload = {
            'start' : 'true',
            'session' : 0,
            'row' : 0,
            'col' : 0
        }
        self.url = "http://labcores.ppgi.ufrj.br/niv_python/ttt"
        self.end = False


    def startGame(self):
        req = requests.get(self.url, params=self.startPayload)
        response = json.loads(req.text)

        self.board = Board.Board()
        self.board.setSession(response['session'])
        self.board.setPlayerNumber(response['player_num'])
        self.board.setCpuNumber(2)
        if (self.board.getPlayerNumber() == 2):
            self.board.setCpuNumber(1)
            self.board.setPosition((response['cpu_move'][0], response['cpu_move'][1]), self.board.getCpuNumber())

        self.board.showBoard()


    def sendTuple(self, jogada):
        if self.board.setPosition(jogada, self.board.getPlayerNumber()) == True:

            data = {
                'session' : self.board.getSession(),
                'row' : jogada[0],
                'col' : jogada[1]
            }
            req = requests.get(self.url, params=data)
            response = json.loads(req.text)
            if 'row' in response:
                self.board.setPosition((response['row'], response['col']), self.board.getCpuNumber())
            else:
                self.end = True
                print("\n\nO jogo terminou: O", response['winner'], "é o vencedor")

            self.board.showBoard()

    def gameEnd(self):
        return self.end