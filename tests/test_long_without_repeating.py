from solutions.long_without_repeating import length_longest_subst
import pytest


@pytest.mark.parametrize(
    'string,length',
    [
        ("abc_abcd_ab", 5),
        ("pwawkepwaaw", 4),
        ("", 0),
        ("aaaaa", 1),
    ]
)
def test_length(string, length):
    assert length_longest_subst(string) == length
