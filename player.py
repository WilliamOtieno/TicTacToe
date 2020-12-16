import math
import random


class Player:
    def __init__(self, letter):
        # X or O
        self.letter = letter
    
    # Players to get their next move
    def get_move(self, game):
        pass



class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    
    def get_move(self, game):
        square = random.choice(game.avaible_moves())
        return square



class  HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    
    def get_move(self, game):
        valid_square = False
        val = None

        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9):' )
            """
            We are going to check that this is a correct value by trying to cast it
            to an integer, and if it's not, then we say it's invalid. If that spot 
            is not available on the board, we also sat it is invalid
            """
            try:
                val = int(square)
                if val not in game.avaible_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try again.")
            
        return val




