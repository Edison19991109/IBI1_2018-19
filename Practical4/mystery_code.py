# What does this piece of code do?
# Answer: this piece of code is used to get a prime number.

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

#Use a variable to control the loop. If it is 'False', it means that it has not found a prime number yet.
#If it equals to 'True', then it suggests that it has got a prime number.
p=False

#Use a loop to try until it gets a prime number.
while p==False:
    
    #If it finds a prime number, it won't change the value of p from 'True' to 'False'.
    #Then it will break from the loop.
    p=True
    
    #Try to get a random number greater than 1 but less than 100.
    n = randint(1,100)
    
    #To get the ceiling of suqare root of that random number.
    #According to mathmatics, if there is not a factor after trying to suqare root of a number, then this number is a prime number.
    u = ceil(n**(0.5))
    for i in range(2,u+1):
        # To see whether it has factor
        # Try until the ceiling number of the square number. 
        # If it still doesn't have a factor, it means it's a prime number
        if n%i == 0:
            p=False


#Then print out the number it finds.
print(n)
