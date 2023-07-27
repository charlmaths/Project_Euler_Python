# Prime numbers:

""" Prime number is only divisible by 1 or it self, it also must be greater than 1
so 2, is only divisible by 1 x 2, 3 is only divisible by 1 x 3, 4 is divisible by 1 x 4 and 2 x 2
so 4 is not a prime number. """

num = 8

""" We will start at 2 because every number is divisible by 1,
so we use 2 which is also the smallest prime number. We will also use
'Else', a keyword for 'for'. 'Else' only triggers when the loop finishes,
if break is present, it doesn trigger at all. """

for i in range(2, number):
    if num % i == 0:
        print("not prime")
        break
else:
    print("prime")