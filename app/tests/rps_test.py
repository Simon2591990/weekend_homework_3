import unittest

from models.rps_function import rock_paper_scissors
from models.player import Player

class testRps(unittest.TestCase):

    # def test_rps_function__player_1_rock(self):
    #     self.assertEqual("Player 1 wins with rock!", rock_paper_scissors("rock", "scissors"))

    # def test_rps_function__player_1_scissors(self):
    #     self.assertEqual("Player 1 wins with scissors!", rock_paper_scissors("scissors", "paper"))

    # def test_rps_function__player_1_paper(self):
    #     self.assertEqual("Player 1 wins with paper!", rock_paper_scissors("paper", "rock"))

    # def test_rps_function__player_2_rock(self):
    #     self.assertEqual("Player 2 wins with rock!", rock_paper_scissors("scissors", "rock"))

    # def test_rps_function__player_2_scissors(self):
    #     self.assertEqual("Player 2 wins with scissors!", rock_paper_scissors("paper", "scissors"))

    # def test_rps_function__player_2_paper(self):
    #     self.assertEqual("Player 2 wins with paper!", rock_paper_scissors("rock", "paper"))


    def setUp(self):
        self.rock_player = Player("Mr Rock", "rock")
        self.scissors_player = Player("Mr Scissors", "scissors")
        self.paper_player = Player("Mr Paper", "paper")

    def test_rock_player_wins_1(self):
         self.assertEqual("Player 1 wins with rock!", rock_paper_scissors(self.rock_player, self.scissors_player))

    def test_rock_player_wins_2(self):
         self.assertEqual("Player 2 wins with rock!", rock_paper_scissors(self.scissors_player, self.rock_player))

    def test_scissors_player_wins_1(self):
        self.assertEqual("Player 1 wins with scissors!", rock_paper_scissors(self.scissors_player, self.paper_player))

    def test_scissors_player_wins_2(self):
        self.assertEqual("Player 2 wins with scissors!", rock_paper_scissors(self.paper_player, self.scissors_player))

    def test_paper_player_wins_1(self):
        self.assertEqual("Player 1 wins with paper!", rock_paper_scissors(self.paper_player, self.rock_player))

    def test_paper_player_wins_2(self):
        self.assertEqual("Player 2 wins with paper!", rock_paper_scissors(self.rock_player, self.paper_player))

    


        