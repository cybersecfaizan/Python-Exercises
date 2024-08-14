#!/usr/bin/python
# The below code generates the first 10 Fibonacci Numbers

y = 0
z = 1
i = 0
for x in range(10):
    i = y + z
    y = z
    z = i
    print(i)