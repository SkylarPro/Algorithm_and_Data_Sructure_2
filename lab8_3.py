from lab8 import BM_search

def max_len_pref(string1: str, string2: str) -> int:
    for idx in reversed(range(len(string1))):
        substring = string1[:idx]
        if BM_search(string2, substring) is not None:
            return len(substring)
    return 0


if __name__ == '__main__':
    string1 = "abcdefghijklmnopqrstuvwxyz"
    string2 = "Abcd?aBcd!abCd.abcD!?"
    print(f"Test string:\n{string1}\n{string2}")
    print(f"Result: {max_len_pref(string1, string2)}")
