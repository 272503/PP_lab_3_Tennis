#Original code:

# class TennisGame2:
#     def __init__(self, player1_name, player2_name):
#         self.player1_name = player1_name
#         self.player2_name = player2_name
#         self.p1points = 0
#         self.p2points = 0

#     def won_point(self, player_name):
#         if player_name == "player1":
#             self.p1_score()
#         else:
#             self.p2_score()

#     def score(self):
#         result = ""
#         if self.p1points == self.p2points and self.p1points < 3:
#             if self.p1points == 0:
#                 result = "Love"
#             if self.p1points == 1:
#                 result = "Fifteen"
#             if self.p1points == 2:
#                 result = "Thirty"
#             result += "-All"
#         if self.p1points == self.p2points and self.p1points > 2:
#             result = "Deuce"

#         p1res = ""
#         p2res = ""
#         if self.p1points > 0 and self.p2points == 0:
#             if self.p1points == 1:
#                 p1res = "Fifteen"
#             if self.p1points == 2:
#                 p1res = "Thirty"
#             if self.p1points == 3:
#                 p1res = "Forty"

#             p2res = "Love"
#             result = p1res + "-" + p2res
#         if self.p2points > 0 and self.p1points == 0:
#             if self.p2points == 1:
#                 p2res = "Fifteen"
#             if self.p2points == 2:
#                 p2res = "Thirty"
#             if self.p2points == 3:
#                 p2res = "Forty"

#             p1res = "Love"
#             result = p1res + "-" + p2res

#         if self.p1points > self.p2points and self.p1points < 4:
#             if self.p1points == 2:
#                 p1res = "Thirty"
#             if self.p1points == 3:
#                 p1res = "Forty"
#             if self.p2points == 1:
#                 p2res = "Fifteen"
#             if self.p2points == 2:
#                 p2res = "Thirty"
#             result = p1res + "-" + p2res
#         if self.p2points > self.p1points and self.p2points < 4:
#             if self.p2points == 2:
#                 p2res = "Thirty"
#             if self.p2points == 3:
#                 p2res = "Forty"
#             if self.p1points == 1:
#                 p1res = "Fifteen"
#             if self.p1points == 2:
#                 p1res = "Thirty"
#             result = p1res + "-" + p2res

#         if self.p1points > self.p2points and self.p2points >= 3:
#             result = "Advantage player1"

#         if self.p2points > self.p1points and self.p1points >= 3:
#             result = "Advantage player2"

#         if (
#             self.p1points >= 4
#             and self.p2points >= 0
#             and (self.p1points - self.p2points) >= 2
#         ):
#             result = "Win for player1"
#         if (
#             self.p2points >= 4
#             and self.p1points >= 0
#             and (self.p2points - self.p1points) >= 2
#         ):
#             result = "Win for player2"
#         return result

#     def set_p1_score(self, number):
#         for i in range(number):
#             self.p1_score()

#     def set_p2_score(self, number):
#         for i in range(number):
#             self.p2_score()

#     def p1_score(self):
#         self.p1points += 1

#     def p2_score(self):
#         self.p2points += 1

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
