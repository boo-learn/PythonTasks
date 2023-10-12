import pytest

from solutions.barge import Barge


def test_barge_creation():
    barge = Barge(10)
    assert not barge.containers[0]


def test_add_barrel():
    barge = Barge(10)
    container = 1
    barge.add_barrel(container, 'A')
    assert barge.containers[1] == ['A']


def test_remove_barrel():
    barge = Barge(10)
    barge.add_barrel(1, 'a')
    assert barge.remove_barrel(1) == 'a'
    assert not barge.remove_barrel(1)

def test_check_empty():
    barge = Barge(10)
    barge.check_empty()
    assert not barge.mistakes
    barge.add_barrel(1, 'a')
    barge.check_empty()
    assert barge.mistakes