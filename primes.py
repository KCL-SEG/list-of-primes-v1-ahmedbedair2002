"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    count = 2
    while number_of_primes != 0:
        for x in range(2,count):
            if count % x == 0:
                break
        else:
            list.append(count)
            number_of_primes -= 1
        count += 1
    return list
