if __name__ == '__main__':
    s = input()
    print(any(c for c in s if c.isalnum()))
    print(any(c for c in s if c.isalpha()))
    print(any(c for c in s if c.isdigit()))
    print(any(c for c in s if c.islower()))
    print(any(c for c in s if c.isupper()))