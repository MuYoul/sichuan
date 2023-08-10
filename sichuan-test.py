import sichuan
from sichuan import SichuanGame

class TestSichuanGame:
    def test_initialize_board(self):
        game = SichuanGame()
        game.initialize_board()
        assert sum(row.count(' ') for row in game.board) == game.board_size * game.board_size - game.pairs_count * len(game.tile_types)

    def test_find_and_match_tiles(self):
        game = SichuanGame(tile_types=["A"], pairs_count=1)
        game.initialize_board()
        game.find_and_match_tiles()
        assert sum(row.count('A') for row in game.board) == 0

    def test_check_game_over(self):
        game = SichuanGame(tile_types=["A"], pairs_count=0)
        game.initialize_board()
        assert game.check_game_over() == True

        game = SichuanGame(tile_types=["A"], pairs_count=1)
        game.initialize_board()
        assert game.check_game_over() == False
