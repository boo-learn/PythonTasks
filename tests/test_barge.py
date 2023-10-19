import pytest

from solutions.barge import Barge


def test_add_barrel():
    barge = Barge(10)
    container = 1
    barge.add_barrel(container, 'A')
    barge.check_empty()
    assert barge.check_mistakes()

@pytest.mark.parametrize(
    'container_num,barrel_type,result',
    [
        (1, 'a', False),
        (1, 'b', True),
    ]
)
def test_remove_barrel(container_num, barrel_type, result):
    barge = Barge(10)
    barge.add_barrel(container_num, barrel_type)
    barge.remove_barrel(1, 'a')
    barge.check_empty()
    assert barge.check_mistakes() == result

def test_check_empty():
    barge = Barge(10)
    barge.check_empty()
    assert not barge.check_mistakes()
    barge.add_barrel(1, 'a')
    barge.check_empty()
    assert barge.check_mistakes()