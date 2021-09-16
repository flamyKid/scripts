"""             Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""


def largest_prime_factor(num):
    i = 2

    while i <= num // 2:
        if num % i == 0:
            num /= i
        i += 1

    return num


if __name__ == '__main__':
    print(largest_prime_factor(600851475143))  # output: 6857
