
# Count Even Numbers
def count_evens(nums):
    return len([n for n in nums if n % 2 == 0])

# Tests
print(count_evens([2, 1, 2, 3, 4]) == 3)
print(count_evens([2, 2, 0]) == 3)
print(count_evens([1, 3, 5]) == 0)

# Dicts and Sets
food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}

print('{0} is from {1}, and he likes {2}, {3}, {4}, and {5}'.format(prefs) for prefs in food_prefs)
