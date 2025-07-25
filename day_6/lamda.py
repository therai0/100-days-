""" Lamda function """

# printing squar using lamda function
sqr = lambda x:x**2

print(sqr(10)) #output: 100


# check number is even or odd
even_odd  = lambda x: x%2 ==0

check_even = even_odd(10) # it will return true
if check_even:
    print("Yes Even")
else:
    print("Odd")


# check which number is grater 
check_greater = lambda x,y:x if x > y else y

check_num_grt = check_greater(100,45) 
print(check_num_grt) #100



# using lamda function as a argument in filter method to filter the even number in list
lst = [12,32,545,6,45,7]
new_even_lst = list(filter(lambda x: x%2 == 0,lst))
print(new_even_lst)
