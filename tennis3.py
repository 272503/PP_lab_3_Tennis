#Original code:

# class TennisGame3:
#     def __init__(self, player1_name, player2_name):
#         self.p1_n = player1_name
#         self.p2_n = player2_name
#         self.p1 = 0
#         self.p2 = 0

#     def won_point(self, n):
#         if n == "player1":
#             self.p1 += 1
#         else:
#             self.p2 += 1

#     def score(self):
#         if (self.p1 < 4 and self.p2 < 4) and (self.p1 + self.p2 < 6):
#             p = ["Love", "Fifteen", "Thirty", "Forty"]
#             s = p[self.p1]
#             return s + "-All" if (self.p1 == self.p2) else s + "-" + p[self.p2]
#         else:
#             if self.p1 == self.p2:
#                 return "Deuce"
#             s = self.p1_n if self.p1 > self.p2 else self.p2_n
#             return (
#                 "Advantage " + s
#                 if ((self.p1 - self.p2) * (self.p1 - self.p2) == 1)
#                 else "Win for " + s
#             )

class TennisGame3:
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

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
        if self._is_early_game():
            return self._get_regular_score()
        if self.player1_score == self.player2_score:
            return "Deuce"
        return self._get_endgame_score()

    def _is_early_game(self):
        return self.player1_score < 4 and self.player2_score < 4 and (self.player1_score + self.player2_score < 6)

    def _get_regular_score(self):
        p1 = self.SCORE_NAMES[self.player1_score]
        p2 = self.SCORE_NAMES[self.player2_score]
        return f"{p1}-All" if self.player1_score == self.player2_score else f"{p1}-{p2}"

    def _get_endgame_score(self):
        diff = self.player1_score - self.player2_score
        leader = self.player1_name if diff > 0 else self.player2_name
        return f"Advantage {leader}" if abs(diff) == 1 else f"Win for {leader}"
