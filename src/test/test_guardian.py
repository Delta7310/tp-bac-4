from src.laxleague.guardian import Guardian


def test_guardian():
    g = Guardian('mary','jones')
    assert  'mary' == g.first_name
    assert  'jones' == g.lastname