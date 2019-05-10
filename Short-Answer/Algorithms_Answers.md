Add your answers to the Algorithms exercises here.

Exercise I

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


Exercise II

Things that we can infer from the problem are:
  - that at point f whether the eggs get broken or not when dropped changes.
So at floors f (and f+) eggs break, but at floors f- they don't.
So we want to find, the first floor (f - 1) at which eggs won't break at.
I think the best way to do this is by creating a binary search tree from whatever value
n (our building height) is. 
That means that we'd have to continually split the positional value of where
we throw our eggs into smaller and smaller portions by halving the height from which we're
throwing the eggs until we find the floor at which an dropped egg doesn't break.


Our building height is equal to n. #(I'm using 15 stories as a visual example)

If we find the the building's midpoint floor level.
    midpoint = (n // 2)     #(7th floor)

And then drop an egg from there
    def drop_egg(midpoint):
        egg_breaks = True

Because the egg still broke we will still need to go lower in the building
so we'll create a new midpoint variable value
    half_of_midpoint = (midpoint // 2)  #(3rd)

We then try to drop the egg from there
    def drop_egg(half_of_midpoint):
        egg_break = False

So we know know that somewhere in between midpoint and half_of_midpoint
is the floor in which the eggs start to not break (f-1).
So we will then use that to find the correct floor by continuing to split the
value and test our egg_drop function.
    def drop_egg((half_of_midpoint + (half_of_midpoint // 2)):  #(5th floor)
        egg_break = True

So we now know that the floor between half_of_midpoint (3) and 
((half_of_midpoint + (half_of_midpoint // 2)) (5) is the magic sweet spot
where dropped eggs don't break. (In the instance here it would be floor 4.
Those are some crazy strong eggs!)


This function would be a binary search tree and would therefore, have the
big O notation of O(log(n)).


