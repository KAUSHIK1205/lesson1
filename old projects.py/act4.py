def minimum_flips(arr):
    return arr.count(0)

arr = [1, 0, 1, 0, 0, 1]
print("Flips needed:", minimum_flips(arr))