# ===========================================
# SET METHODS
# ===========================================

numbers = {10, 20, 30, 40, 40, 30}
print(numbers)

# add()
numbers.add(50)
print(numbers)

# update()
numbers.update([60, 70])
print(numbers)

# remove()
numbers.remove(20)
print(numbers)

# discard()
numbers.discard(100)
print("Discard",numbers)

# pop()
numbers.pop()
print(numbers)

# copy()
new_set = numbers.copy()
print(new_set)

# union()
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))

# intersection()
print(set1.intersection(set2))

# difference()
print(set1.difference(set2))

# symmetric_difference()
print(set1.symmetric_difference(set2))

# issubset()
print({1,2}.issubset({1,2}))

# issuperset()
print(set1.issuperset({1,2}))

# len()
print(len(set1))

# max()
print(max(set1))

# min()
print(min(set1))

# sum()
print(sum(set1))

# clear()
temp = {1, 2, 3}
temp.clear()
print(temp)