import math
def is_repeated(s, ss):
    ss = ss * math.ceil(len(s) / len(ss))
    ss = ss[:len(s)]

    return s == ss


def min_substring(string):
    min_length, max_length = 1, len(string)

    while min_length + 1 < max_length:
        mid = (min_length + max_length) // 2

        first_substring = string[:mid]

        if is_repeated(string, first_substring):
            max_length = mid
        else:
            min_length = mid

    if is_repeated(string, string[:min_length]):
        return min_length

    return max_length


if __name__ == '__main__':
    print(min_substring("okok"))
    print(min_substring("yeyek"))
    print(min_substring("akpakp"))
    print(min_substring("abababa"))
