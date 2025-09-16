def implement_circuit(a, b, c):
    return (a & b) | (~c & 1)

print("Circuit output:", implement_circuit(1, 1, 0))