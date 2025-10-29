# TODO: Fungsi untuk memeriksa apakah sebuah bilangan genap
def is_even(num):
    if num % 2 == 0:
        return True
    return False

# Tes fungsi
print(is_even(4))   # True
print(is_even(7))   # False

# TODO: Fungsi untuk menghitung faktorial
def factorial(n):
    count = 1
    for x in range(1, n+1):
        count *= x
    return count

# Tes fungsi
print(factorial(5))  # 120
print(factorial(0))  # 1
