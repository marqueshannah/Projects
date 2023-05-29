def is_prime(n):
    prime = True
    if n < 3:
        status = False
    else:
        for i in range(3, n):
            if n % i == 0:
                prime = False
    return prime


for n in range(3, 100):
    if is_prime(n):
        if n == 97:
            print(n)
        else:
            print(n)

if __name__ == '__main__':
    is_prime(n)
