# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

total = 0  # keeps track of the sum

for i in range(3, 1000):  # specifies the range of number
    if i % 3 == 0 or i % 5 == 0:  # checks if divisible by 3 or 5
        total += i  # if divisible by 3 or 5 add to total

print(total)  # prints result
