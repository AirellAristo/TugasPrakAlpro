def kombinasi(n, x):
    if n == 0 or x == 0 or n == x:
        return 1
    else:
        return kombinasi(n - 1, x - 1) * n // x

print(kombinasi(5, 2))  # Output: 10