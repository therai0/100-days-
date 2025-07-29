
# Create a custom iterator class named `Countup` that takes a number and counts up to n. Implement the `__iter__` and `__next__` methods. Test the iterator by using it in a for loop.

class Countup:

    def __init__(self,num):
            self.num = num
    
    def __iter__(self):
          self.current = self.num
          return self 

    def __next__(self):

           if self.current > 20:
                 raise StopIteration
           else:
                 x = self.current
                 self.current += 1
                 return x

for i in Countup(10):
      print(i,end=" ") 
# output: 10 11 12 13 14 15 16 17 18 19 20  



# Write a generator function named `fibonacci` that yields the Fibonacci sequence. Test the generator by iterating over it and printing the first 10 Fibonacci numbers.

print("") # just to break line

def fibonacci(n):
      a = 0
      b = 1
      for i in range(n):
            c = a + b
            a = b 
            b = c 
            yield c 

for i in fibonacci(10):
      print(i, end= " ")
# output: 1 2 3 5 8 13 21 34 55 89


# Create a generator expression that generates the squares of numbers from 1 to 10. Iterate over the generator and print each value.


sqr = (x**2 for x in range(1,11))  # generator expression
print(type(sqr))

for i in sqr:
      print(i,end=" ")
# output: 1 4 9 16 25 36 49 64 81 100

print("") #just to break line


# Write two generator functions: `even_numbers` that yields even numbers up to a limit, and `squares` that yields the square of each number from another generator. Chain these generators to produce the squares of even numbers up to 20.

# function one
def even_numbers(n):
      for i in range(n):
            if i % 2 == 0:
                  yield i

# function two
def squares(num):
      for i in num:
            yield i**2



for i in squares(even_numbers(10)):
      print(i,end=" ")
# output: 0 4 16 36 64 


