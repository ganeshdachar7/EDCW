#sum of 8 from the given list
nums = [1,2,3,4,5,6,7,8,9]
k = 8

seen = set()
pairs = []

for n in nums:
    diff = k - n
    if diff in seen:
        pairs.append((diff, n))
    seen.add(n)

print(pairs)