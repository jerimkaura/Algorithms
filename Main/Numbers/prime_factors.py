def prime_factors(n):
    factors = []
    # we divide the n by 2 until n becomes an odd n
    while n % 2 == 0:
        factors.append(2)
        n = n//2

    divisor = 3  # the next prime number used for division after 2
    while n != 1 and divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            """since 2 is the only even prime number,
            the rest prime numbers are obtained by adding 2 to the divisor"""
            divisor += 2
    print("The prime factord are:")
    for i in range(len(factors)):
        print(factors[i], end=' ')


if __name__ == "__main__":
    n = int(input("Enter the number to find its prime factors:"))
    prime_factors(n)
