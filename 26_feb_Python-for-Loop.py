#BASIC LEVEL:

# 1. Print numbers from 1 to 10 using a for loop
print("1. Print numbers from 1 to 10:")
for i in range(1, 11):
    print(i)

# 2. Calculate the sum of all numbers in a list using a for loop
print("\n2. Calculate the sum of all numbers in a list:")
numbers = [1, 2, 3, 4, 5]
sum = 0
for num in numbers:
    sum += num
print("Sum:", sum)

# 3. Print the characters of a string in reverse order using a for loop
print("\n3. Print characters of a string in reverse order:")
string = "hello"
for char in reversed(string):
    print(char)

# 4. Find the factorial of a given number using a for loop
print("\n4. Find factorial of a given number:")
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, ":", factorial)

# 5. Print the multiplication table of a given number using a for loop
print("\n5. Print multiplication table of a given number:")
num = 7
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# 6. Count the number of even and odd numbers in a list using a for loop
print("\n6. Count even and odd numbers in a list:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)

# 7. Print squares of numbers from 1 to 5 using a for loop
print("\n7. Print squares of numbers from 1 to 5:")
for i in range(1, 6):
    print("Square of", i, ":", i*i)

# 8. Find length of a string without using len() function
print("\n8. Find length of a string without using len() function:")
string = "hello"
length = 0
for char in string:
    length += 1
print("Length of string:", length)

# 9. Calculate average of a list of numbers using a for loop
print("\n9. Calculate average of a list of numbers:")
numbers = [1, 2, 3, 4, 5]
sum = 0
for num in numbers:
    sum += num
average = sum / len(numbers)
print("Average:", average)

# 10. Print the first n Fibonacci numbers using a for loop
print("\n10. Print the first n Fibonacci numbers:")
n = 10
fibonacci = [0, 1]
for i in range(2, n):
    next_number = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(next_number)
print("Fibonacci numbers:", fibonacci)






#INTERMIDIATE LEVEL
# 11. Check if a given list contains any duplicates using a for loop.
def has_duplicates(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return True
        seen.add(item)
    return False

# 12. Print prime numbers in a given range using a for loop.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes_in_range(start, end):
    print("Prime numbers in the range", start, "to", end, ":")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")

# 13. Count the number of vowels in a string using a for loop.
def count_vowels(string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

# 14. Find the maximum element in a 2D list using a nested for loop.
def find_max_in_2d_list(matrix):
    max_element = float('-inf')
    for row in matrix:
        for item in row:
            if item > max_element:
                max_element = item
    return max_element

# 15. Remove all occurrences of a specific element from a list using a for loop.
def remove_all_occurrences(lst, element):
    return [x for x in lst if x != element]

# 16. Generate a multiplication table for numbers from 1 to 5 using a nested for loop.
def multiplication_table():
    for i in range(1, 6):
        print("Multiplication table for", i)
        for j in range(1, 11):
            print(i, "x", j, "=", i*j)
        print()

# 17. Convert a list of Fahrenheit temperatures to Celsius using a for loop.
def fahrenheit_to_celsius(fahrenheit_list):
    celsius_list = []
    for fahrenheit in fahrenheit_list:
        celsius = (fahrenheit - 32) * 5 / 9
        celsius_list.append(celsius)
    return celsius_list

# 18. Print the common elements from two lists using a for loop.
def find_common_elements(list1, list2):
    common_elements = []
    for item in list1:
        if item in list2 and item not in common_elements:
            common_elements.append(item)
    return common_elements

# 19. Print the pattern of right-angled triangles using a for loop. Use ‘*’ to draw the pattern.
def print_right_triangle_pattern(rows):
    for i in range(1, rows + 1):
        print('*' * i)

# 20. Find the greatest common divisor (GCD) of two numbers using a for loop.
def gcd(num1, num2):
    for i in range(min(num1, num2), 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i
    return 1






#ADVANCED LEVEL

# 21. Calculate the sum of the digits of numbers in a list using list comprehension.
def sum_of_digits(numbers):
    return [sum(int(digit) for digit in str(num)) for num in numbers]

# 22. Find the prime factors of a given number using a for loop and list comprehension.
def prime_factors(num):
    factors = []
    divisor = 2
    while num > 1:
        while num % divisor == 0:
            factors.append(divisor)
            num //= divisor
        divisor += 1
    return factors

# 23. Extract unique elements from a list and store them in a new list using list comprehension.
def unique_elements(lst):
    return list(set(lst))

# 24. Generate a list of all palindromic numbers up to a specified limit using list comprehension.
def palindromic_numbers(limit):
    return [num for num in range(limit) if str(num) == str(num)[::-1]]

# 25. Flatten a nested list using list comprehension.
def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

# 26. Compute the sum of even and odd numbers in a list separately using list comprehension.
def sum_even_odd(numbers):
    even_sum = sum(num for num in numbers if num % 2 == 0)
    odd_sum = sum(num for num in numbers if num % 2 != 0)
    return even_sum, odd_sum

# 27. Generate a list of squares of odd numbers between 1 and 10 using list comprehension.
def squares_of_odd():
    return [num**2 for num in range(1, 11) if num % 2 != 0]

# 28. Combine two lists into a dictionary using list comprehension.
def lists_to_dictionary(keys, values):
    return {keys[i]: values[i] for i in range(min(len(keys), len(values)))}

# 29. Extract vowels from a string and store them in a list using list comprehension.
def extract_vowels(string):
    vowels = 'aeiouAEIOU'
    return [char for char in string if char in vowels]

# 30. Remove all non-numeric characters from a list of strings using list comprehension.
def remove_non_numeric(strings):
    return [''.join(char for char in string if char.isdigit()) for string in strings]







#CHALLENGE LEVEL

import math
from itertools import product

# 31. Generate a list of prime numbers using the Sieve of Eratosthenes algorithm and list comprehension.
def sieve_of_eratosthenes(n):
    sieve = [True] * (n+1)
    sieve[0:2] = [False, False]
    for i in range(2, int(math.sqrt(n))+1):
        if sieve[i]:
            sieve[i*i:n+1:i] = [False] * len(sieve[i*i:n+1:i])
    return [i for i in range(n+1) if sieve[i]]

# 32. Generate a list of all Pythagorean triplets up to a specified limit using list comprehension.
def pythagorean_triplets(limit):
    return [(a, b, c) for c in range(1, limit)
            for b in range(1, c)
            for a in range(1, b)
            if a**2 + b**2 == c**2]

# 33. Generate a list of all possible combinations of two lists using list comprehension.
def all_combinations(list1, list2):
    return [(x, y) for x in list1 for y in list2]

# 34. Calculate the mean, median, and mode of a list of numbers using list comprehension.
def calculate_statistics(numbers):
    mean = sum(numbers) / len(numbers)
    sorted_numbers = sorted(numbers)
    mid_index = len(numbers) // 2
    median = sorted_numbers[mid_index] if len(numbers) % 2 != 0 else (sorted_numbers[mid_index - 1] + sorted_numbers[mid_index]) / 2
    mode = max(set(numbers), key=numbers.count)
    return mean, median, mode

# 35. Generate Pascal's triangle up to a specified number of rows using list comprehension.
def pascals_triangle(rows):
    triangle = [[1]]
    for _ in range(rows - 1):
        previous_row = triangle[-1]
        next_row = [1] + [previous_row[i] + previous_row[i+1] for i in range(len(previous_row) - 1)] + [1]
        triangle.append(next_row)
    return triangle

# 36. Calculate the sum of the digits of a factorial of numbers from 1 to 5 using list comprehension.
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def sum_of_factorial_digits(n):
    return sum([int(digit) for digit in str(factorial(n))])

# 37. Find the longest word in a sentence using list comprehension.
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

# 38. Filter a list of strings to include only those with more than three vowels using list comprehension.
def filter_strings_with_vowels(strings):
    vowels = 'aeiouAEIOU'
    return [s for s in strings if sum(1 for char in s if char in vowels) > 3]

# 39. Calculate the sum of the digits of numbers from 1 to 1000 using list comprehension.
def sum_of_digits_up_to(n):
    return sum(sum(int(digit) for digit in str(num)) for num in range(1, n+1))

# 40. Generate a list of prime palindromic numbers using list comprehension.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime_palindromic_numbers(limit):
    return [num for num in range(limit) if str(num) == str(num)[::-1] and is_prime(num)]

# Test the functions
if __name__ == "__main__":
    # Test each function here
    pass



