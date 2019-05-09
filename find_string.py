def count_substring(string, sub_string):
    end = len(sub_string)
    count = 0
    for i in range(0, len(string)):
        s = string[i:end]
        if sub_string in s:
            count = count + 1
        end = end + 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)