def longest_consecutive(arr):

    s = set(arr)
    longest = 0

    for num in s:

        if num - 1 not in s:

            length = 1

            while num + length in s:
                length += 1

            longest = max(longest, length)

    return longest


arr = list(map(int, input("Enter numbers: ").split()))

print(longest_consecutive(arr))