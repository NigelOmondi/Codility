# A non-empty array A consisting of N integers is given.

# A permutation is a sequence containing each element from 1 to N once, and only once.

# For example, array A such that:

#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
#     A[3] = 2
# is a permutation, but array A such that:

#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
# is not a permutation, because value 2 is missing.

# The goal is to check whether array A is a permutation.

# Write a function:

# def Solution(A)

# that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

# For example, given array A such that:

#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
#     A[3] = 2
# the function should return 1.

# Given array A such that:

#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
# the function should return 0.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [1..1,000,000,000].

def solution(A):
    N = len(A)
    unique_numbers = set()

    for num in A:
        if num < 1 or num > N:
            # Numbers outside the range [1, N] cannot be part of a permutation
            return 0

        if num in unique_numbers:
            # Duplicate number found, not a permutation
            return 0

        unique_numbers.add(num)

    # Check if all numbers from 1 to N are present
    return 1 if len(unique_numbers) == N else 0

# Example usage:
permutation_array = [4, 1, 3, 2]
print(solution(permutation_array))  # Output: 1

non_permutation_array = [4, 1, 3]
print(solution(non_permutation_array))  # Output: 0
