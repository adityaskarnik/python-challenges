def swap_case(s):
    case_s = ""
    for i in s:
        if i.islower():
            case_s += i.upper()
        else:
            case_s += i.lower()
    return case_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)