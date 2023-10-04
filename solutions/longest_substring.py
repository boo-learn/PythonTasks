def lengthOfLongestSubstring(s: str) -> int:
    substring: str = ''
    substrings: list = []

    for letter in s:
        if letter in substring:
            substrings.append(substring)
            substring = letter
        elif letter not in substring:
            substring += letter

    substrings.append(substring)
    longest_substring = max(substrings, key=len)

    return len(longest_substring)
