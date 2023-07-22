
class FibonacciSeq:
    """ This is a class that have methods that can solve fibonacci sequence problem """
    
    def fib_seq(x, y, n):
        """ This function will use while loop so we can specify how many terms we can do """
        num1 = x # 1st term
        num2 = y # 2nd term
        i = 0 # Initialising while loop.
        lst = [num1, num2] # 1st & 2nd term added into the list
        while i < n:
            num3 = num1 + num2 # Third term is the sum of first two terms
            lst.append(num3) # The sum of the value is then added onto the list via append()
            num1 = num2 # Then we shift to the next terms e.g. 1st term is now 2nd term 
            num2 = num3 # 2nd term is now 3rd term 
            i = i + 1 # This 'shifting' will continue until we reach 'n' 
        return lst

res2 = fib_seq2(0,1,5)
print(res2)


def fib_even(z):
    for num in z:
        lst_new = []
        if num % 2 == 0:
            lst_new.append(num)
    return lst_new