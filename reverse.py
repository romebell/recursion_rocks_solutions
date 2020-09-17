# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# Write a recursive function called `reverse` that accepts a ss and returns a reversed ss.

def reverse(string):
    # Write code here

    # base case
    if len(string) == 0:
        return ""
    
    print(string[-1] + reverse(string[:-1]))
    
    # recursive step
    return string[-1] + reverse(string[:-1]) # retu + reverse("comp")


# print(reverse("")) 
# => ""
# print(reverse("a")) 
# => "a"
# print(reverse("ab")) 
# => "ba"
# print(reverse("computer")) 
# => "retupmoc"
print(reverse("computer"))
# => "computer"


# r + reverse('compute')
        # e + reverse('comput')

# re + 
                # t + reverse('compu')
                            # u + reverse('comp')
                                        # p + reverse('com')
                                                    # m + reverse('co')
                                                            # o + reverse('c')
                                                                        # c + reverse('')

# retupmoc