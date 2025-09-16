def is_power_of_8(n):
    if n < 1: return False
    while n % 8 == 0:
        n //= 8
    return n == 1

print("Is power of 8:", is_power_of_8(512))