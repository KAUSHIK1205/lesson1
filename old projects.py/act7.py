def rightmost_set_bit(n):
    return (n & -n).bit_length() if n != 0 else 0

print("Rightmost set bit:", rightmost_set_bit(18))