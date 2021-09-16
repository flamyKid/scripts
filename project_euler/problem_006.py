"""             Sum square difference
The sum of the squares of the first ten natural numbers is,
1² + 2² + ... + 10² = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)² = 55² = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def sum_square_difference(limit):
    numbers = range(1, limit)

    sum_squares = sum(list(map(lambda n: n ** 2, numbers)))
    square_sum = (sum(numbers)) ** 2

    return square_sum - sum_squares


if __name__ == '__main__':
    print(sum_square_difference(101))  # output: 25164150
