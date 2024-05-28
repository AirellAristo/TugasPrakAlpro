#Latihan 13-1

def is_prime_recursive(n, divisor=None):
    if n <= 1:
        return False
    if n == 2:
        return True
    if divisor is None:
        divisor = int(n ** 0.5) 
    if divisor == 1:
        return True
    if n % divisor == 0:
        return False
    print(divisor)
    return is_prime_recursive(n, divisor - 1)

# Contoh penggunaan
print(is_prime_recursive(97))  
print(is_prime_recursive(30))  