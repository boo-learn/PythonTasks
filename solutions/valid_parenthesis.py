def isValid(self, s: str) -> bool:
    bracket_matches = {
        '[': ']',
        '{': '}',
        '(': ')',
    }
    opened_brackets = []
    for bracket in s:
        if bracket in bracket_matches:
            opened_brackets.append(bracket)
            continue

        if bracket in bracket_matches.values():
            if not opened_brackets:
                return False
            if not bracket_matches[opened_brackets[-1]] == bracket:
                return False
            opened_brackets.pop()

    if not opened_brackets:
        return True
    return False

