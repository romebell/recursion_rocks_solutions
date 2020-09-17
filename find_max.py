# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the largest number in a given array.

def find_max(l):
    # Write code here
    pass

# print(find_max([1, 4, 45, 6, -50, 10, 2]))
# => 45


def lizz_find_max(l):
    # base case
    if len(l) == 1:
        return l[0]
    else:
        return max(l[0], lizz_find_max(l[1:]))

print(lizz_find_max([1, 4, 45, 6, -50, 10, 2]))

# 1 vs lizz_find_max(l[1:])
          # 4 vs lizz_find_max(l[1:])
                 # 45 vs lizz_find_max([1:])
                             # 6 vs lizz_find_max([1:])
                                         # -50 vs lizz_find_max([1:])
                                                     # 10 vs lizz_find_max([1:])
                                                                # 2 
                                                                        
