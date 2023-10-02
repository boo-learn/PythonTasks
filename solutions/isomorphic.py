def isIsomorphic(s: str, t: str) -> bool:

    def letter_sequence(string: str) -> list:
        comparison = []
        prev_letter = ''
        for letter in string:
            if prev_letter:
                if letter is not prev_letter:
                    comparison.append(0)
                else:
                    comparison.append(1)
            prev_letter = letter
        return comparison

    for letter_1, letter_2 in zip(s, t):
        if letter_1 == letter_2:
            return False

    sequence_s = letter_sequence(s)
    sequence_t = letter_sequence(t)

    if not sequence_t == sequence_s:
        return False
    return True

print(isIsomorphic("badc", "baba"))