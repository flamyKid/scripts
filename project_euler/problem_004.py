"""             Largest palindrome product
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""


def largest_palindrome_product(start_num, limit_num):
    nums = []

    for i in range(start_num, limit_num)[::-1]:
        for j in range(start_num, limit_num)[::-1]:
            if str(i * j) == str(i * j)[::-1]:
                nums.append(i * j)

    return max(nums)


if __name__ == '__main__':
    print(largest_palindrome_product(100, 1000))  # output: 906609
