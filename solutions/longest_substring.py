def lengthOfLongestSubstring(s: str) -> int:

    substring: str = ''
    longest_substring = 0
    i = 0

    while i < len(s):
        for letter in s[i:]:
            if letter in substring:
                if longest_substring < len(substring):
                    longest_substring = len(substring)
                substring = ''
            else:
                substring += letter
        i += 1

    return longest_substring

print(lengthOfLongestSubstring("abcabcbb"))
