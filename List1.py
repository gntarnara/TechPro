ar = [15, 10, 25, 65]

min = ar[0]
total = 0

for a in ar:
    if min > a:
        min = a
    total += a

av = total/len(ar)
print("Minimum: ", min, "Sum: ", total, "Average: ", av)
