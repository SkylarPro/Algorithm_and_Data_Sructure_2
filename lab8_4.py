
def max_polindrom(string: str) -> int:
    if len(string) <= 1:
        return len(string)

    for length in reversed(range(len(string) // 2 + 1)):
        for idx in range(len(string) - length):
            substring = string[idx:idx + length]
            if string[max(0, idx-length):idx] == substring \
                    or string[idx+length:idx+2*length] == substring:
                return length * 2
            if string[max(0, idx-length+1):idx] == substring[2::-1] \
                    or string[idx+length:idx+2*length-1] == substring[1::-1]:
                return length * 2 - 1
    return 1


if __name__ == '__main__':
    string = "a123bc9e9c321"
    print(f"Input: {string}")
    print(f"Output: {max_polindrom(string)}")
