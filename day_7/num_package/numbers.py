# this is the custom module which contain multiple function


# function to check the number is prime or not
def is_prime(num):
    factor = 0
    orginal_num = num
    while num > 0:
        if orginal_num % num == 0:
            factor += 1
        num -= 1
    
    if factor == 2:
        return "Prime number"
    else:
        return "Not prime number"



