The intuition is to form a recurrence relation by building on top of previous solved solutions
at n-1 and n-2 lengths where n must be at least 2 or higher.

1 way for Full[n-1]
______________
           |  |
___________|__|

1 way for Full[n-2]
______________
         |____|
_________|____|

1 way for Upper[n-1] (missing lower part)
______________
         __|  |
________|_____|

1 way for Lower[n-1] (missing upper part)
______________
        |__   |
___________|__|

Therefore the equation becomes:
Full[n] = Full[n-1] + Full[n-2] + Upper[n-1] + Lower[n-2]

Solving for Upper...

1 way for Lower[n-1]
______________
        |_____|
___________|

1 way for Full[n-2]
______________
         |  __|
_________|__|

Therefore the equation becomes:
Upper[n] = Lower[n-1] + Full[n-2]

Similarly, solving for Lower...

1 way for Upper[n-1]
____________
        ___|___
________|_____|

1 way for Full[n-2]
___________
        |  |__
________|_____|

Therefore the equation becomes:
Lower[n] = Upper[n-1] + Full[n-2]
