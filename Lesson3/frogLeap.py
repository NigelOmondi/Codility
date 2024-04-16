import math

def frogJump(X, Y, D):
    total_distance_leapt = Y - X
    number_of_hops = total_distance_leapt / D
    minimal_hops_to_next_whole_number = math.ceil(number_of_hops)

    return minimal_hops_to_next_whole_number

print(frogJump(10, 85, 30))
print(frogJump(15, 200, 7))