def length_longest_subst(s: str) -> int:
    substring = ""
    for char in s:
        if char not in substring:
            substring += char
        else:
            print(f"{substring=}")
            substring = char


if __name__ == "__main__":
    length_longest_subst("abc_abcd_ab")
