'''
Заглавные
65-90

Прописные
97-122
'''
def ceasar_encode(string: str) -> str:

    encoded_string = ''
    capital_start = 65
    capital_end = 90
    lower_start = 97
    lower_end = 122

    for symbol in string:
        ascii_num = ord(symbol)

        if capital_start <= ascii_num <= capital_end or lower_start <= ascii_num <= lower_end:
            new_symbol_ord = ascii_num + 3
            if capital_end < new_symbol_ord < lower_start:
                new_symbol_ord = capital_start + (new_symbol_ord - capital_end - 1)
            elif new_symbol_ord > lower_end:
                new_symbol_ord = lower_start + (new_symbol_ord - lower_end - 1)

            symbol = chr(new_symbol_ord)

        encoded_string += symbol

    return encoded_string

ceasar_encode('a')