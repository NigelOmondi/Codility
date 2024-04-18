def solution(A):
    full_array = range(1, len(A) + 2)
    return sum(full_array) - sum(A)

A = [2, 3, 1, 5]
result = solution(A)
print(result)