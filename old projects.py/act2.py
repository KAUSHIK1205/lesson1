def linear_recursion(n):
    if n == 0:
        return
    linear_recursion(n - 1)
# Time Complexity: O(n)

def binary_recursion(n):
    if n == 0:
        return
    binary_recursion(n - 1)
    binary_recursion(n - 1)
# Time Complexity: O(2^n)