def solution(N):
    # Convert N to binary and remove the '0b' prefix
    binary_of_N = bin(N)[2:]

    zero_counter = 0
    max_zero_gap = 0

    for digit in binary_of_N:
        # binary digits are strings
        if digit == '0':
            # increment zero_counter
            zero_counter += 1
        else:
            # if digit is 1, find the max number of zeros between max_zero_gap and zero_counter
            max_zero_gap = max(max_zero_gap, zero_counter)
            # reset zero_counter
            zero_counter = 0

    return max_zero_gap

# Example usage:
print(solution(1041))  # Output: 5
print(solution(32))  # Output: 0