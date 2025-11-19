# List Comprehension
nums = [x*x for x in range(5)]
print(nums)  # Output: [0,1,4,9,16]


# List
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0,2,4,6,8]


# List
names = ["marjani", "eilert"]
upper = [n.upper() for n in names]
print(upper)  # Output: ['MARJANI','EILERT']


# List Comprehension
words = ["apple", "an", "banana"]
long = [w for w in words if len(w) > 2]
print(long)  # Output: ['apple','banana']
