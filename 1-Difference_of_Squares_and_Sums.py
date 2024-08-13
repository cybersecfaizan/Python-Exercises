#!/usr/bin/python
# The Below Code Finds the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# Adds the first 100 Natural Numbers, then squares that sum
i = 0;
for j in range(101):
    i = i + j
i = i*i

# Squares each of the first 100 natural numbers, then adds each term
y = 0
for x in range(101):
    y = y + x*x

print(i-y)