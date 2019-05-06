# Sample Input 0

# aabbbccde

# Sample Output 0

# b 3
# a 2
# c 2

occr = {}
s = input()
for i in s:
    occr[i] = s.count(i)
data = sorted(sorted(occr.items(), key=lambda v: v[0]), key=lambda v: v[1], reverse = True)
for i in data[:3]:
    print(i[0],i[1])