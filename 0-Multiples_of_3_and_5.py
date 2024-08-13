
#!/usr/bin/python
# The below code finds the sum of all the multiples of 3 and 5 below 1000

y=0;
for x in range(1000):
    if x % 3 == 0 or x % 5 == 0:
        y = x + y
print(y)