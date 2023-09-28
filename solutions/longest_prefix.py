def longestCommonPrefix(strs: list[str]) -> str:
    prefix = min(strs, key=len)

    for word in strs:
        word = word[:len(prefix)]
        if prefix and prefix[0] == word[0]:
            while not word.count(prefix):
                prefix = prefix[:-1]
        else:
            return ''

    return prefix
