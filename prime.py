num = 12


def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False


output = num
while (isPrime(output) == False):
    output += 1

print("Next Prime to", num, "is", output)
