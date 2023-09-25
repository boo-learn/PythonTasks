def rle_encode(string: str) -> str:
    res_str = ''
    counter = 0
    curr_letter = ''
    for letter in string:
        if not curr_letter:
            curr_letter = letter
        elif curr_letter != letter:
            res_str += f'{counter}{curr_letter}'
            curr_letter = letter
            counter = 0
        counter += 1

    if counter:
        res_str += f'{counter}{curr_letter}'

    return res_str