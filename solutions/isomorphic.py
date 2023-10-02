def isIsomorphic(s: str, t: str) -> bool:

    def check_pattern(first_str: str, second_str: str) -> bool:
        letters_map = {}
        for letter_s, letter_t in zip(first_str, second_str):
            if letter_s not in letters_map:
                letters_map[letter_s] = letter_t
            if not letters_map[letter_s] == letter_t:
                return False
        return True

    if not check_pattern(s, t) or not check_pattern(t, s):
        return False
    return True

print(isIsomorphic("badc", "baba"))