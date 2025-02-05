n = int(input('Enter the number: '))
for i in range(2, n):
    if (n % i) == 0:
        print('It is not prime number.')
        break
else:
    print('It is a prime number.')
