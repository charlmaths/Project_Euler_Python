# Prime numbers:

""" Prime number is only divisible by 1 or it self, it also must be greater than 1
so 2, is only divisible by 1 x 2, 3 is only divisible by 1 x 3, 4 is divisible by 1 x 4 and 2 x 2
so 4 is not a prime number. We will start at 2 because every number is divisible by 1,
so we use 2 which is also the smallest prime number. We will also use
'Else', a keyword for 'for'. 'Else' only triggers when the loop finishes,
if break is present, it doesn trigger at all.
"""

class PrimeNumberSolver():
    """ This is a class that solves prime number related problems """

    def __init__(self,number):
        """ Instance variables """
        self.number = number


    def is_number_prime(self):
        """ Method to check if number is a prime number """
        num = self.number
        for i in range(2, num):
            if num % i == 0:
                return "Not a prime Number"
            else:
                return "Number is prime"

    def prime_factors(self):
        """ Method to find the prime factors of a number
         ******** NOT FINISHED YET **********
         """
        num = self.number
        while num % 2 == 0:
            print(2, end=" ")
            num = num / 2



# Object:

# Instantiate the object

prime_number = PrimeNumberSolver(356)
check_value = prime_number.is_number_prime()
print(check_value)
