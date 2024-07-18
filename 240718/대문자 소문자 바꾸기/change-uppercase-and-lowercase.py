for string in input():
    if string.isupper():
        print(chr(ord(string)+32), end="")
    else:
        print(chr(ord(string)-32), end="")