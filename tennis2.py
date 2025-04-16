class TennisGame2:
    SCORE_MAP = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        elif player_name == self.player2_name:
            self.player2_score += 1

    def score(self):
        if self.player1_score == self.player2_score:
            return self._equal_score()
        if self.player1_score >= 4 or self.player2_score >= 4:
            return self._advantage_or_win()
        return self._get_regular_score()

    def _equal_score(self):
        if self.player1_score < 3:
            return f"{self.SCORE_MAP[self.player1_score]}-All"
        return "Deuce"

    def _advantage_or_win(self):
        diff = self.player1_score - self.player2_score
        if diff == 1:
            return f"Advantage {self.player1_name}"
        if diff == -1:
            return f"Advantage {self.player2_name}"
        if diff >= 2:
            return f"Win for {self.player1_name}"
        return f"Win for {self.player2_name}"

    def _get_regular_score(self):
        p1 = self.SCORE_MAP[self.player1_score]
        p2 = self.SCORE_MAP[self.player2_score]
        return f"{p1}-{p2}"

    def set_player1_score(self, number):
        self.player1_score += number

    def set_player2_score(self, number):
        self.player2_score += number
