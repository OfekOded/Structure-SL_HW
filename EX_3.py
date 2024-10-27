# Oded Ofek 215348145
# Ziv Farajun 323920603

# 1. יצירת Tuple של המספרים מ-1 עד 1000
def create_tuple(n, current=1):
    if current > n:
        return ()
    return (current,) + create_tuple(n, current + 1)

# קריאה לפונקציה
numbers_tuple = create_tuple(1000)
print(numbers_tuple)

# 2. חישוב סכום איברי ה-Tuple בצורה רקורסיבית
def sum_tuple(tup, index=0):
    if index == len(tup):
        return 0
    return tup[index] + sum_tuple(tup, index + 1)

# קריאה לפונקציה
total_sum = sum_tuple(numbers_tuple)
print(f"Sum of elements: {total_sum}")

# 3. חישוב LCM (מכפלה משותפת מינימלית)
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# דוגמה לחישוב LCM
print(lcm(4, 6))  # Output: 12

# 4. בדיקת פלינדרום רקורסיבית
def is_palindrome(num):
    num_str = str(num)
    if len(num_str) <= 1:
        return True
    if num_str[0] != num_str[-1]:
        return False
    return is_palindrome(num_str[1:-1])

# דוגמה לשימוש
print(is_palindrome(123454321))  # Output: True

# 5. מיון רשימות ב-zip באמצעות רקורסיה
def sorted_zip(lists):
    if not lists:
        return []
    first_elements = [lst[0] for lst in lists]
    rest_elements = [lst[1:] for lst in lists]
    sorted_first = sorted(first_elements)
    return [tuple(sorted_first)] + sorted_zip(rest_elements)

# דוגמה לשימוש
result = sorted_zip([[3, 1, 2], [5, 6, 4], ['a', 'b', 'c']])
print(result)  # Output: [(1, 4, 'a'), (2, 5, 'b'), (3, 6, 'c')]

# Lazy Evaluation: יצירת מערכים ובדיקת ביצועים
import time
import sys

# יצירת מערך רגיל
start_time = time.time()
regular_array = list(range(10001))
end_time = time.time()

print(f"Time to create regular array: {end_time - start_time} seconds")
print(f"Size of array: {sys.getsizeof(regular_array)} bytes")

# מערך עם 5000 המספרים הראשונים
start_time = time.time()
first_5000 = regular_array[:5000]
end_time = time.time()

print(f"Time to create sliced array: {end_time - start_time} seconds")
print(f"Size of sliced array: {sys.getsizeof(first_5000)} bytes")
print(f"Type of sliced array: {type(first_5000)}")

# גנרטור למספרים ראשוניים
def prime_generator():
    num = 2
    while True:
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            yield num
        num += 1

# דוגמה לשימוש בגנרטור
primes = prime_generator()
print(next(primes))  # 2
print(next(primes))  # 3
print(next(primes))  # 5
print(next(primes))  # 7

# גנרטור לחישוב טור טיילור של e^2
def taylor_series_e2():
    n = 0
    result = 0
    while True:
        term = (2 ** n) / factorial(n)
        result += term
        yield result
        n += 1

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# דוגמה לשימוש בגנרטור
e2_gen = taylor_series_e2()
for _ in range(8):
    print(next(e2_gen))
