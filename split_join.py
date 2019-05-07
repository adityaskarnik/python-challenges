def split_and_join(line):
    l = line.split(" ")
    l = "-".join(l)
    return l
    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)