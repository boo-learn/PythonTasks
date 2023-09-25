from solutions.rle import rle_encode

def test_rle_return_type():
    assert type(rle_encode("hi")) == str

def test_rle_count_symbols():
    assert rle_encode('aaaa') == '4a'

def test_rle_same_letter_in_different_parts_of_string():
    assert rle_encode('aaabbbbcccccaaa') == '3a4b5c3a'

def test_rle_empty_string():
    assert rle_encode('') == ''

def test_rle_not_letter_symbols():
    assert rle_encode('!!!!!!!!!!!') == '11!'

def test_rle_upper_and_lower_case():
    assert rle_encode('AaBBbb') == '1A1a2B2b'

def test_rle_different_non_letter_symbols_and_space():
    assert rle_encode('++++++--          ') == '6+2-10 '