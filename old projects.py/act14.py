def reverse_bits(n):
    return int(bin(n)[2:][::-1], 2)

print("Reversed bits:", reverse_bits(13))