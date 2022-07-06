from typing import List
class Prepstring:
    def __init__(self):
        self.p_pow = [31**i for i in range(10**4)]

    def hash_func(self, str):
        hashh = 0
        for idx, symb in enumerate(str):
            hashh += (ord(symb) - ord('a') + 1)*self.p_pow[idx]
        return hashh

    def find_same_string(self, strings: List[str]):
        hash_strings = [(string, idx) for idx, string in enumerate(map(self.hash_func, strings))]
        hash_strings.sort()
        name_group = ""
        for n_group, idx in hash_strings:
            if n_group != name_group:
                name_group = n_group
                print("Name Group: ", name_group)
            print(strings[idx])

class RabinKarp:
    def __init__(self,):
        self.p_pow = None

    def hash_func(self, string):
        hashh = 0
        for idx, symb in enumerate(string):
            hashh += (ord(symb) - ord('a') + 1)*self.p_pow[idx]
        return hashh

    def do_rabinkarp(self, string, pattern):
        s, p = len(string), len(pattern)
        self.p_pow = [31 ** i for i in range(max(s,p))]
        hp = self.hash_func(pattern)
        count = 0
        for i in range(len(string) - len(pattern) + 1):
            hs = self.hash_func(string[i:i+p])
            if hp == hs:
                if string[i:i+p] == pattern:
                    count += 1
        return count

if __name__ == "__main__":
    proc = Prepstring()
    data = ["aaa", "aaa", "abc", "ab", "abc"]
    proc.find_same_string(data)

    print("\nRabinKarp")
    proc = RabinKarp()
    print("hello how you // number:", proc.do_rabinkarp("hello how you", "he"))
    print("hello how youho // number:",proc.do_rabinkarp("hello how youho", "ho"))



