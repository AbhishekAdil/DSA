# Big O Notation
'''
Big O notation is used to measure how running time or space requirements for your 
program grow as input size grows.

Big O is the simplest method of saying, This is how much my program is going to take.
Hence it make sense to keep the fastest growing term.

Measuring running time growth: time complexity

Measuring space growth: space complexity
'''
# Exaple 1

# Program with time complexity = order of n --->  O(n)

def get_squared_numbers(numbers):
    squared_numbers = []
    for i in numbers:         # n iteration
        squared_numbers.append(i * i)   # use append to store value at the end of the list 
    return squared_numbers 

numbers = [2, 5, 8, 9]
print(get_squared_numbers(numbers))    # [4, 25, 64, 81]

# As time will from linearly
# Above program follow --->  time = O(n) because as the size increses time also increses

# Example 2

# time complexity = order of 1 ---->  O(1)

def find_first_pe(prices, eps, index):
    pe = prices[index]/ eps[index]
    return pe
# this is a order of 1 time complexity program
# because we don't have to work on all the values
# we just pick values from the indexes and perform operations on tham
# this is constant so time complexity --> O(1)

# 3) Example 3
# find the duplicate value in the list

numbers = [3, 6, 2, 4, 3, 6, 8, 9]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):     # n^2 iterations
        if numbers[i] == numbers[j]:
            print(numbers[i], "is a duplicate")
            break

# Time complexity for th program is order of n square --> O(n^2), because it has n^2 iteration
# time

# 4) Example

numbers =[3, 6, 2, 4, 3, 6, 8, 9]
duplicate = None

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):     # n^2 iterations
        if numbers[i] == numbers[j]:
            duplicate = numbers[i]

for i in range(len(numbers)):                # n iteration
    if numbers[i] == duplicate:
        print(i)

# Time complexity for the program is order of n^2  ---> O(n^2)
# time = a*n^2 + b*n + c     --->  O(n^2) complexity
# not n^2 + n

# 5) Example of binary search (sorted)

numbers = [4, 9, 15, 21, 34, 57, 68, 91]    # serach for 68

# Itaration method
for i in range(len(numbers)):
    if numbers[i] == 68:          # O(n)   complexity
        print(i)                  # it takes 7 iterations

# Binary search
'''
iteration k = n / 2^k

1 = n / 2^k

k = log n ---> O(log n)  # n -> number of elements, k -> numbers of iterations
complexity of binary search in order of logn
'''
