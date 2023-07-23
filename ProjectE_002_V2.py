
class FibSeq:
    """ This is a class that have methods to produce Fibonacci Sequence
    & solve related Fibonacci Sequence problem """

    def __init__(self, first_term, second_term):
        """ Instance variables:
        -> first_term = first term
        -> second_term = second term
        """
        self.first_term = first_term
        self.second_term = second_term
        #self.num_term = num_term
        #self.max_term = max_term



    def fib_sequencer(self, num_term):
        """ Method for creating Fibonacci Sequence
        -> num_term = number of terms
        """
        num1 = self.first_term # 1st term
        num2 = self.second_term # 2nd term
        i = 0 # Initialising while loop.
        num_list = [num1, num2] # 1st & 2nd term added into the list
        while i < num_term:
            num3 = num1 + num2 # Third term is the sum of first two terms
            num_list.append(num3) # The sum of the value is then added onto the list via append()
            num1 = num2 # Then we shift to the next terms e.g. 1st term is now 2nd term
            num2 = num3 # 2nd term is now 3rd term
            i = i + 1 # This 'shifting' will continue until we reach 'n'
        return num_list



    # ---------- Method Underconstruction ---------- #
    """
    def fib_even_term_sum(self):
        # Method for findind and obtaining the sum of 'even valued' terms.
        #This is only efficient if n < 10000

        input_list = tuple(self.fib_sequencer()) # Store the fib seq. that was acquired by the above method
        even_list = [] # Initialise an empty list for 'even valued' term
        i = 0
        for i in input_list: # For a variable 'i' in the list,
            if i % 2 == 0: # If the element is even, Store the the index number into the list above.
                even_list.append(input_list.index(i))
        t_even_list = tuple(even_list)
        return sum(t_even_list)
    """



    def fibEvenTermSum_v2(self, max_term):
        """ This method is method is more efficient than above
        -> max_term = maximum number of term
        """
        num1 = self.first_term # 1st term
        num2 = self.second_term # 2nd term
        #max_term = self.max_term # Max term
        even_term = 0
        while num2 <= max_term:
            num1, num2 = num2, num1 + num2
            if num2 % 2 == 0:
                even_term += num2
            #print(even_term)
        return even_term


# Instantiate object:

fibseq_1 = FibSeq(0,1)
#print(fibseq_1.first_term) # To show the first term
#print(fibseq_1.second_term) # To show the second term
#print(fibseq_1.fib_sequencer(15)) # To show Fibonacci Sequence
#print(fibseq_1.fib_even_term_sum())
print(fibseq_1.fibEvenTermSum_v2(4000000))