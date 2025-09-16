def longest_odd_even_subarray(arr):
    max_len = curr_len = 1
    for i in range(1, len(arr)):
        if (arr[i] % 2) != (arr[i - 1] % 2):
            curr_len += 1
            max_len = max(max_len, curr_len)
        else:
            curr_len = 1
    return max_len

print("Longest odd-even subarray:", longest_odd_even_subarray([5, 10, 21, 4, 7, 8, 9]))