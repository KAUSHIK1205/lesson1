def longest_ones(n):
    return max(len(s) for s in bin(n)[2:].split('0'))

print("Longest 1s:", longest_ones(156))