import math
def find_lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

print("LCM:", find_lcm(12, 18))