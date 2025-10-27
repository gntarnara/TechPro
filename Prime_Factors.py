input_number = 57


def isPrime(input_number):
    for i in range(2, input_number):
        if input_number % i == 0:
            return False


temporary_number = input_number
while (isPrime(temporary_number) == False):
    for i in range(2, temporary_number):
        if (temporary_number % i == 0):
            print("Prime factor: ", i)
            temporary_number = input_number//i
            break
print("Prime Factor: ", temporary_number)
