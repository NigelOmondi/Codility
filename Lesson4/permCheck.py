def solution(A):
    # Convert the array into a set
    s = set(A)

    # Get the length of the array
    n = len(A)

    # Check if the size of the set is equal to the length of the array  
    if len(s) != n:
        return 0
    
    # Check if the maximum value in the array is equal to the length of the array
    if max(A) != n:
        return 0
    
    # if the two conditions are met, then the array is a permutation
    return 1

# Example usage:
permutation_array = [4, 1, 3, 2]
print(solution(permutation_array))  # Output: 1

non_permutation_array = [4, 1, 3]
print(solution(non_permutation_array))  # Output: 0