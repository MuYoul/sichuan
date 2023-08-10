import random
import time
import os

class SichuanGame:
    def __init__(self, board_size=10, tile_types=["A", "B", "C"], pairs_count=18):
        self.board_size = board_size
        self.tile_types = tile_types
        self.pairs_count = pairs_count

    def initialize_board(self):
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        tiles = self.tile_types * self.pairs_count
        random.shuffle(tiles)

        for tile in tiles:
            x, y = random.randint(0, self.board_size - 1), random.randint(0, self.board_size - 1)
            while self.board[y][x] != ' ':
                x, y = random.randint(0, self.board_size - 1), random.randint(0, self.board_size - 1)
            self.board[y][x] = tile

    def find_and_match_tiles(self):
        for y in range(self.board_size):
            for x in range(self.board_size):
                if self.board[y][x] != ' ':
                    # Find matching pair logic
                    for match_y in range(self.board_size):
                        for match_x in range(self.board_size):
                            if (match_y != y or match_x != x) and self.board[match_y][match_x] == self.board[y][x]:
                                # Matching pair found, remove them
                                self.board[y][x] = ' '
                                self.board[match_y][match_x] = ' '
                                return
        # No matching pairs found
        print("No more matching pairs. Game Over!")
        exit()


    def check_game_over(self):
        for y in range(self.board_size):
            for x in range(self.board_size):
                if self.board[y][x] != ' ':
                    return False # Tiles still remain, game continues
        return True # No tiles left, game over

    def draw_board(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        for row in self.board:
            print(' '.join(row))
        print()

    def start_game(self):
        self.initialize_board()
        while True:
            self.draw_board()
            self.find_and_match_tiles()
            if self.check_game_over():
                print("Game Over!")
                break
            time.sleep(0.3)

game = SichuanGame()
game.start_game()
