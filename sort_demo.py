# Sort demo

# 1. sort() - the verb
# in-place: the original list will be modified
numbers = [5, 10, 2, 9, 7]

#def sort(self, reverse=False, key =...):
# Two parameters:
# 1. reverse - either True or False (Boolean)
# 2. key - the name of a function (NOT a string, a function)

# key argument
numbers.sort(reverse=True) # sort the list numbers in non-decreasing order
print(numbers)


# 2. sorted() - the adj.
# return a sorted version of the list
numbers = [5, 7, 10, 2, 9, 2, 7]
numbers_sorted = sorted(numbers)
print(f"orignal list: {numbers}")
print(f"sorted version: {numbers_sorted}")

# Sort by words in alphabetical order
words = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "a", "bc"]
words_sorted_v1 = sorted(words)
print(f"v1: {words_sorted_v1}")

# How to get the length of a string: len()
words_sorted_v2 = sorted(words, key=len) # sort the list by the length of the words
print(f"v2: {words_sorted_v2}")

products = [ ["orange", 0.99, "grocery"],
             ["apple", 0.91, "grocery"],
             ["desk", 199, "office"] ]
products_sorted_v1 = sorted(products)
print(f"v1: {products_sorted_v1}")

def get_second_element(l):
    return l[1]

# sort the list by unit price, which is the second element in the lists
products_sorted_v2 = sorted(products, key = get_second_element)
print(f"v2: {products_sorted_v2}")

# nameless function
products_sorted_v3 = sorted(products, key = lambda l:l[1])
print(f"v3: {products_sorted_v3}")