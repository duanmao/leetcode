remove = 4
remap = dict((str(i), str(i + 1)) for i in range(remove, 9)[::-1])
# print(remap)

def base9(n):
    res = 0
    digit = 1
    while (n):
        res += (n % 9) * digit
        n //= 9
        digit *= 10
    return res

def valid(num):
    if (str(remove) not in str(num)): return True
    return False

def convert(nums):
    for i, num in enumerate(nums):
        s = str(num)
        for k in remap:
            s = s.replace(k, remap[k])
        nums[i] = int(s)

base9s = []
for i in range(1, 10005001):
    base9s.append(base9(i))

gnums = []
cur = 1
while (len(gnums) < 10005000):
    while (not valid(cur)): cur += 1
    gnums.append(cur)
    cur += 1

assert(len(base9s) == len(gnums))

convert(base9s)

print(len(base9s), base9s[-1], len(gnums), gnums[-1])

for i in range(len(gnums)):
    if (base9s[i] != gnums[i]):
        print(i, base9s[:i+1], gnums[:i+1])
        break
assert(base9s == gnums)

print("all same")
