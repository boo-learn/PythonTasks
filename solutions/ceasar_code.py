'''
Заглавные
65-90

Прописные
97-122
'''


def ceasar_encode(string: str) -> str:
    encoded_string = ''
    char_exceptions = {
        "x": "a",
        "y": "b",
        "z": "c",
        "X": "A",
        "Y": "B",
        "Z": "C"
    }

    for symbol in string:
        if symbol.isalpha(): # [a-z A-Z]
            if symbol in char_exceptions.keys():
                symbol = char_exceptions[symbol]
            else:
                symbol = chr(ord(symbol) + 3)

        encoded_string += symbol

    return encoded_string


ceasar_encode('a')
