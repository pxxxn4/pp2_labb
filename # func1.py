# func1.py
from itertools import permutations
from math import pi
from random import randint

def grams_to_ounces(grams):
    return 28.3495231 * grams

def fahrenheit_to_celsius(f):
    return (5 / 9) * (f - 32)

def count_animals(heads, legs):
    for chickens in range(heads + 1):
        rabbits = heads - chickens
        if 2 * chickens + 4 * rabbits == legs:
            print(chickens, rabbits)
            return
    print("No solution")

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_primes(numbers):
    return list(filter(is_prime, numbers))

def print_permutations(string):
    for p in permutations(string):
        print(''.join(p))

def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

def has_33(nums):
    return any(nums[i] == nums[i+1] == 3 for i in range(len(nums) - 1))

def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

def sphere_volume(radius):
    return (4/3) * pi * radius**3

def unique_elements(lst):
    return list(dict.fromkeys(lst))  # Быстрый способ убрать дубликаты

def is_palindrome(string):
    return string == string[::-1]

def draw_histogram(values):
    for v in values:
        print('*' * v)

def guess_number():
    target = randint(1, 20)
    name = input("Hello! What is your name?\n")
    print(f'Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess.')

    attempts = 0
    while True:
        guess = int(input())
        attempts += 1
        if guess < target:
            print('Too low. Try again:')
        elif guess > target:
            print('Too high. Try again:')
        else:
            print(f'Good job, {name}! You guessed my number in {attempts} tries!')
            break

print("\ntest\n")

# 1. conv
print("grams_to_ounces(10) =>", grams_to_ounces(10))  # 283.495231

# 2. cels
print("fahrenheit_to_celsius(100) =>", fahrenheit_to_celsius(100))  # 37.7778

# 3. rabbits and chickens
print("count_animals(35, 94):")
count_animals(35, 94)  # 23 12

# 4. filter_prime
print("filter_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) =>", 
      filter_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # [2, 3, 5, 7]

# 5. permutatuios
print('print_permutations("abc"):')
print_permutations("abc")  # abc, acb, bac, bca, cab, cba

# 6. change order
print('reverse_words("We are ready") =>', reverse_words("We are ready"))  
# "ready are We"

# 7. 33
print("has_33([1, 3, 3]) =>", has_33([1, 3, 3]))  # True
print("has_33([1, 3, 1, 3]) =>", has_33([1, 3, 1, 3]))  # False

# 8. 007
print("spy_game([1,2,4,0,0,7,5]) =>", spy_game([1,2,4,0,0,7,5]))  # True
print("spy_game([1,0,2,4,0,5,7]) =>", spy_game([1,0,2,4,0,5,7]))  # True
print("spy_game([1,7,2,0,4,5,0]) =>", spy_game([1,7,2,0,4,5,0]))  # False

# 9. sphere
print("sphere_volume(3) =>", sphere_volume(3))  # 113.097

# 10. unique list
print("unique_elements([1,2,3,3,4,5,5]) =>", unique_elements([1,2,3,3,4,5,5]))  
# [1, 2, 3, 4, 5]

# 11. is pal
print('is_palindrome("madam") =>', is_palindrome("madam"))  # True
print('is_palindrome("hello") =>', is_palindrome("hello"))  # False

# 12. hist
print("draw_histogram([4, 9, 7]):")
draw_histogram([4, 9, 7])  

# 13. guess
# guess_number()

