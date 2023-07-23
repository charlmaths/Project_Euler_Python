
class FibSeq:
    """ This is a class that have methods that can solve fibonacci sequence problem """

    def __init__(self, first_term, second_term, num_term):
        """ Instance variables:
        x -> first term
        y -> second term
        n -> number of terms """
        self.first_term = first_term
        self.second_term = second_term
        self.num_term = num_term


    def fib_sequencer(self):
        """ Method for creating Fibonacci Sequence """
        num1 = self.first_term # 1st term
        num2 = self.second_term # 2nd term
        num_term = self.num_term
        i = 0 # Initialising while loop.
        lst = [num1, num2] # 1st & 2nd term added into the list
        while i < num_term:
            num3 = num1 + num2 # Third term is the sum of first two terms
            lst.append(num3) # The sum of the value is then added onto the list via append()
            num1 = num2 # Then we shift to the next terms e.g. 1st term is now 2nd term
            num2 = num3 # 2nd term is now 3rd term
            i = i + 1 # This 'shifting' will continue until we reach 'n'
        return lst


# Instantiate object:

fibseq_1 = FibSeq(0,1,5)
print(fibseq_1.first_term) # To show the first term
print(fibseq_1.second_term) # To show the second term
print(fibseq_1.num_term) # To show the number of term
print(fibseq_1.fib_sequencer()) # To show the method