def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n: #This is because if n is divisible by any number larger than its square root,
                      #we would have already checked for its divisibility by a smaller factor.
        if n % i == 0 or n % (i + 2) == 0:  #the second part is to efficiently skip over 2 and 3 divisibility
            return False
        i += 6  #this it because every prime number can be expressed as 6k+-1
    return True

for num in range(1, 101):
    if is_prime(num):
        print(num, end=" ")
