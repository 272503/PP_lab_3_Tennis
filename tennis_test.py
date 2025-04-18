import pytest

from tennis1 import TennisGame1
from tennis2 import TennisGame2
from tennis3 import TennisGame3

from tennis_unittest import play_game, test_cases


@pytest.mark.parametrize(
    "TennisGameClass",
    [
        TennisGame1,
        TennisGame2,
        TennisGame3,

    ],
)
@pytest.mark.parametrize(
    "p1_points p2_points score p1_name p2_name".split(), test_cases
)
def test_get_score_most_games(
    TennisGameClass, p1_points, p2_points, score, p1_name, p2_name
):
    game = play_game(TennisGameClass, p1_points, p2_points, p1_name, p2_name)
    assert score == game.score()

