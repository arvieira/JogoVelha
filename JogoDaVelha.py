import sys
import NetworkGameManager


def main (argv):
    print("Jogo Da Velha:")
    text = input("Iniciar uma partida[S/n]:\n")
    if (text == "s" or text == "S"):
        print("Iniciando jogo...")
        game = NetworkGameManager.NetworkGameManager()
        game.startGame()

        while (not game.gameEnd()):
            text = input("Sua vez. Insira uma posição <linha>,<coluna>:")
            jogada = text.split(",")
            try:
                game.sendTuple((int(jogada[0]), int(jogada[1])))
            except(ValueError):
                print("Jogada inválida. Tente novamente.")
    else:
        return


if __name__ == ("__main__"):
    main (sys.argv)