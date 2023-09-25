from solutions.collatz_algo import collatz_algo


def test_collatz_algo_no_sequence():
    assert collatz_algo(1) == []


def test_collatz_algo_even_num():
    assert collatz_algo(16) == [16, 8]


def test_collatz_algo_odd_num():
    assert collatz_algo(3) == [3, 10, 5, 16, 8]
