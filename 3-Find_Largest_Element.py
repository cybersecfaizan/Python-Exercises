# Tasked with Finding the Largest Element of a given List. No built-ins

x = [7, 5, 9, 19, 96, 35]
max_val = x[0]
for i in x:
    if i > max_val:
        max_val = i

print(max_val)