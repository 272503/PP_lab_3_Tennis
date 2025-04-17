# Original code:


#class TennisGame1:
#     def __init__(self, player1_name, player2_name):
#         self.player1_name = player1_name
#         self.player2_name = player2_name
#         self.p1points = 0
#         self.p2points = 0

#     def won_point(self, player_name):
#         if player_name == "player1":
#             self.p1points += 1
#         else:
#             self.p2points += 1

#     def score(self):
#         result = ""
#         temp_score = 0
#         if self.p1points == self.p2points:
#             result = {
#                 0: "Love-All",
#                 1: "Fifteen-All",
#                 2: "Thirty-All",
#             }.get(self.p1points, "Deuce")
#         elif self.p1points >= 4 or self.p2points >= 4:
#             minus_result = self.p1points - self.p2points
#             if minus_result == 1:
#                 result = "Advantage player1"
#             elif minus_result == -1:
#                 result = "Advantage player2"
#             elif minus_result >= 2:
#                 result = "Win for player1"
#             else:
#                 result = "Win for player2"
#         else:
#             for i in range(1, 3):
#                 if i == 1:
#                     temp_score = self.p1points
#                 else:
#                     result += "-"
#                     temp_score = self.p2points
#                 result += {
#                     0: "Love",
#                     1: "Fifteen",
#                     2: "Thirty",
#                     3: "Forty",
#                 }[temp_score]
#         return result

class TennisGame1:

    #nazwy powtarzały się
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    def point_name(self, point):
        #aby nie odnosić się ciągle do listy
        return self.SCORE_NAMES[point]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.p1points += 1
        else:
            self.p2points += 1

    def equal_points(self):
        if self.p1points < 3:
            #korzystanie z listy
            return f"{self.point_name(self.p1points)}-All"
        return "Deuce"

    def adventage_or_win(self):
        diff = self.p1points - self.p2points
        #zamiana na imiona faktyczne
        if diff == 1:
            result = f"Advantage {self.player1_name}"
        elif diff == -1:
            result = f"Advantage {self.player2_name}"
        elif diff >= 2:
            result = f"Win for {self.player1_name}"
        else:
            result = f"Win for {self.player2_name}"
        return result

    def score(self):

        if self.p1points == self.p2points:
            # oddzielna funkcja
            return self.equal_points()
        if self.p1points >= 4 or self.p2points >= 4:
            #oddzielna funkcja
            return self.adventage_or_win()
        else:
            #Niepotrzebna pętla, warunki sprawdzane wcześniej
            return f"{self.point_name(self.p1points)}-{self.point_name(self.p2points)}"

