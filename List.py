ar = ["a", "b", "c"]

for i in range(len(ar)):
    print(i, ar[i])

# for a in ar:
# print(a)

print("Reversed")

for i in range(len(ar)-1, -1, -1):
    print(i, ar[i])
