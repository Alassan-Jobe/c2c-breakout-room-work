#Identify if an inputted number is even or odd. Return is boolean. If even, return true. Otherwise, return false. No edge cases
#if num == even:
    #return true
#else:
    #return false


def is_even(num):
    return num % 2 == 0

#testing the solution
print(is_even(5)) #returns false
print(is_even(8)) #returns true
print(is_even(0)) #returns true
print(is_even(2)) #returns true
