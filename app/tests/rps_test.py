import unittest

from models.rps_function import rock_paper_scissors

class testRps(unittest.TestCase):
    
    def test_rps_function__player_1_rock(self):
        self.assertEqual("Player 1 wins with rock!", rock_paper_scissors("rock", "scissors"))

    def test_rps_function__player_1_scissors(self):
        self.assertEqual("Player 1 wins with scissors!", rock_paper_scissors("scissors", "paper"))

    def test_rps_function__player_1_paper(self):
        self.assertEqual("Player 1 wins with paper!", rock_paper_scissors("paper", "rock"))

    def test_rps_function__player_2_rock(self):
        self.assertEqual("Player 2 wins with rock!", rock_paper_scissors("scissors", "rock"))

    def test_rps_function__player_2_scissors(self):
        self.assertEqual("Player 2 wins with scissors!", rock_paper_scissors("paper", "scissors"))

    def test_rps_function__player_2_paper(self):
        self.assertEqual("Player 2 wins with paper!", rock_paper_scissors("rock", "paper"))


    

        