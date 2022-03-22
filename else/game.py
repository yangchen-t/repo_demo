import random,sys


class Game():

        def __init__(self,input):
            self.input = input

        def game_bijiao(self):
            sum = random.randint(0, 12)
            print(sum)
            if int(self.input) > int(sum) :
                print('您的点数大于我，您赢！')
            elif int(self.input) < int(sum):
                print('您的点数小于我，您输啦')
            else:
                print('平局')


game = Game(sys.argv[1])
game.game_bijiao()

