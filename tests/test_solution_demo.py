from solutions.demo import main_question_universe


def test_main_question_universe():
    result = main_question_universe("Hello?")
    assert result == 42
