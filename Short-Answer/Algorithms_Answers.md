Add your answers to the Algorithms exercises here.

a.) a = 0  
while (a < n * n * n):   
a = a + n * n            #O(1) constant

    **Because a is a constant this would be a constant complexity function.
    Meaning that it would have a big O of O(1).

b.) sum = 0
    for i in range(n):   #runs n times
      i += 1
      for j in range(i + 1, n):  #runs from i+1 to n 
        j += 1
        for k in range(j + 1, n):  #runs from j+1 to n
          k += 1
          for l in range(k + 1, 10 + k): #runs from k+1 to 10+k
            l += 1
            sum += 1

    **Because of the nested for loops that all have to preform a function on the n
    this would be a function with a quadratic big O complexity I think. It would grow
    exponentially with the change of the value of n. Therefore I think that this would
    be a big O notation of O(n^2)


c.) def bunnyEars(bunnies):  
      if bunnies == 0:       #O(1) constant
        return 0	     #O(1) constant

      return 2 + bunnyEars(bunnies-1)  
      #O(n) because it will have to run multiple times depending on the bunnies value.

    **This is a linear function that will increase with the bunnies value.
    The two O(1)s get dropped because the O(n) is the largest big O notation
    for the function. So that means that this would have a run time of O(n).

