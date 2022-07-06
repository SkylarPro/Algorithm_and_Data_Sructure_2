def Direct_search(string: str, substring: str) -> None or int:

    for idx1 in range(len(string) - len(substring) + 1):
        for idx2 in range(len(substring)):
            if string[idx1 + idx2] != substring[idx2]:
                break
        else:
            return idx1
    return None


def BM_search(string: str, substring: str) -> int or None:
    len_substr = len(substring)
    bmt = [len_substr] * 256
    for idx in reversed(range(len_substr)):
        if bmt[ord(substring[idx])] == len_substr:
            bmt[ord(substring[idx])] -= idx + 1

    pos = len_substr - 1
    while pos < len(string):
        if substring[-1] != string[pos]:
            pos += bmt[ord(string[pos])]
        elif len_substr == 1:
            return pos
        else:
            for idx in reversed(range(len_substr - 1)):
                if substring[idx] != string[pos - len_substr + idx + 1]:
                    pos += bmt[ord(string[pos - len_substr + idx + 1])] - 1
                    break
                elif idx == 0:
                    return pos - len_substr + 1
    return None


def KMP_search(string: str, substring: str) -> None or int:
    d = [0] * len(substring)
    d[0] = -1
    idx1, idx2 = 0, -1
    while idx1 < len(substring) - 1:
        while idx2 >= 0 and substring[idx1] != substring[idx2]:
            idx2 = d[idx2]
        idx1, idx2 = idx1 + 1, idx2 + 1
        d[idx1] = d[idx2] if substring[idx1] == substring[idx2] else idx2

    idx1 = idx2 = 0
    while idx1 < len(substring) and idx2 < len(string):
        while idx1 >= 0 and string[idx2] != substring[idx1]:
            idx1 = d[idx1]
        idx1, idx2 = idx1 + 1, idx2 + 1

    if idx1 == len(substring):
        return idx2 - len(substring)
    return None


if __name__ == '__main__':
    test_string = 'bac12345cab'
    test_substring = 'cab'
    print(f"Test string: {test_string} \nTest substring: {test_substring}")
    print(f"Direct search = {Direct_search(test_string, test_substring)} (first intersection)")
    print(f"BM search = {BM_search(test_string, test_substring)} (first intersection)")
    print(f"KMP search = {KMP_search(test_string, test_substring)} (first intersection)")

