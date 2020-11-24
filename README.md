
# Optimization algorithms for find minima of functions

I am going to present the two first, very basic, optimization methods for 1 parameter:
> Tri-section method
> Golden Section Search


Then i will introduce 'Bracketing' and present how to implement it. It will be usend in combination with:
> Steepest descent or gradient descent
> Newton-Raphson method

## Tri-section

How tri-section work? Let's say that the minima of ![formula](https://render.githubusercontent.com/render/math?math=f(x)  ) is beetween ![formula](https://render.githubusercontent.com/render/math?math=x_{1}  ) and ![formula](https://render.githubusercontent.com/render/math?math=x_{2}  ) with ![formula](https://render.githubusercontent.com/render/math?math=x_{1} ) < ![formula](https://render.githubusercontent.com/render/math?math=x_{2} ). So we divide the interval ![formula](https://render.githubusercontent.com/render/math?math=x_{1} ) --- ![formula](https://render.githubusercontent.com/render/math?math=x_{2} ) in three part of same size:
> 1. ![formula](https://render.githubusercontent.com/render/math?math=x_{3}  ) = ![formula](https://render.githubusercontent.com/render/math?math=x_{1}  )+ ![formula](https://render.githubusercontent.com/render/math?math=(x_{2}  )- ![formula](https://render.githubusercontent.com/render/math?math=x_{1})  )/3
> 2. ![formula](https://render.githubusercontent.com/render/math?math=x_{4}  )=![formula](https://render.githubusercontent.com/render/math?math=x_{2}  )-![formula](https://render.githubusercontent.com/render/math?math=(x_{2}  )-![formula](https://render.githubusercontent.com/render/math?math=x_{1})  )/3

Let's compute the function in this two points and evaluate the following:
> 1. ![formula](https://render.githubusercontent.com/render/math?math=f(x_{3})  )<![formula](https://render.githubusercontent.com/render/math?math=f(x_{4})  )
> 2. ![formula](https://render.githubusercontent.com/render/math?math=f(x_{3})  )>![formula](https://render.githubusercontent.com/render/math?math=f(x_{4})  )

Now, depending on which condition occurs, we define a new interval around the minimum indicated by 2 new points: ![formula](https://render.githubusercontent.com/render/math?math=x_{1}^{new}  ) and ![formula](https://render.githubusercontent.com/render/math?math=x_{2}^{new}  )

So:
> 1. if ![formula](https://render.githubusercontent.com/render/math?math=f(x_{3})  ) < ![formula](https://render.githubusercontent.com/render/math?math=f(x_{3})  ):

   ![formula](https://render.githubusercontent.com/render/math?math=x_{1}^{new}  )=![formula](https://render.githubusercontent.com/render/math?math=x_{1}  )   
   ![formula](https://render.githubusercontent.com/render/math?math=x_{2}^{new}  )=![formula](https://render.githubusercontent.com/render/math?math=x_{4}  )
   
> 2. if ![formula](https://render.githubusercontent.com/render/math?math=f(x_{3})  ) > ![formula](https://render.githubusercontent.com/render/math?math=f(x_{3})  ):

   ![formula](https://render.githubusercontent.com/render/math?math=x_{1}^{new}  )=![formula](https://render.githubusercontent.com/render/math?math=x_{3}  )     
   ![formula](https://render.githubusercontent.com/render/math?math=x_{2}^{new}  )=![formula](https://render.githubusercontent.com/render/math?math=x_{2}  )
    
and so forth, we iterate until the convergence is not reached.

## Golden section Search

 The Golden search algorithm is a faster version of the tri-section algorithm and use the 'Golden Ratio' for enanching it. Recall that the golden ratio R is degined as $$ R = \(sqrt{5}+1)/2 = 1.618034 $$
 
 ## Bracketing
 
 Let's find now, instead of a value for the minima, a range of values where the minima could be contained with bracketing.  L'ets try to find an interval 0 --- alpha where the minima is located. 
 
We are supposing that in the point x= 0 the derivative is negative, follows that there is a step size delta in which: f(delta) < f(0). Note that we are still using the R golden section value.
The following is how the algorithm work:
step 0:

 j=1
 
 step 1:

![formula](https://render.githubusercontent.com/render/math?math=x_{1}  ) = ![formula](https://render.githubusercontent.com/render/math?math=x_{1}  ) + ![formula](https://render.githubusercontent.com/render/math?math=delta  ) and ![formula](https://render.githubusercontent.com/render/math?math=f(x_{1})  ) = ![formula](https://render.githubusercontent.com/render/math?math=f_{1}  )

step 2:

![formula](https://render.githubusercontent.com/render/math?math=x_{2}  ) = ![formula](https://render.githubusercontent.com/render/math?math=delta*R^{j}  ) and ![formula](https://render.githubusercontent.com/render/math?math=f(x_{2})  ) = ![formula](https://render.githubusercontent.com/render/math?math=f_{2}  )
 
step 3:

if ![formula](https://render.githubusercontent.com/render/math?math=f_{2}  ) >= ![formula](https://render.githubusercontent.com/render/math?math=f_{1}  ) the minimum is in the range 0 --  ![formula](https://render.githubusercontent.com/render/math?math=x_{2}  )

step 4:

if ![formula](https://render.githubusercontent.com/render/math?math=f_{2}  ) < ![formula](https://render.githubusercontent.com/render/math?math=f_{1}  ) --> j=j+1 ,  ![formula](https://render.githubusercontent.com/render/math?math=x_{1}  ) = ![formula](https://render.githubusercontent.com/render/math?math=x_{2}  )  , ![formula](https://render.githubusercontent.com/render/math?math=f(x_{1})  ) = ![formula](https://render.githubusercontent.com/render/math?math=f(x_{2})  ) and go to step 2.

and so forth, we iterate until the convergence is not reached.

## Steepest Descent ( Gradient descent)

Gradient descent methods starts with an inital points ![formula](https://render.githubusercontent.com/render/math?math=x_{0}  ) and the iteratively generates a sequence of points ![formula](https://render.githubusercontent.com/render/math?math=x_{k}  ) defined by the following expression: 
![formula](https://render.githubusercontent.com/render/math?math=x_{k+1}  ) = ![formula](https://render.githubusercontent.com/render/math?math=x_{k}  ) + ![formula](https://render.githubusercontent.com/render/math?math=alpha_{k}  ) * ![formula](https://render.githubusercontent.com/render/math?math=p_{k}  )

Here, ![formula](https://render.githubusercontent.com/render/math?math=p_{k}  ) is the search direction and ![formula](https://render.githubusercontent.com/render/math?math=alpha_{k}  ) is the step length that indicates how big is the step along the ![formula](https://render.githubusercontent.com/render/math?math=p_{k}  ) direction.

For the seek of purpose we choose for now alpha constant and  ![formula](https://render.githubusercontent.com/render/math?math=p_{k}  ) = ![formula](https://render.githubusercontent.com/render/math?math=-f^{'}  ) ; that's it! The we iterate again until covergence is reached

## Backtracking
Do not be confused with 'bracketing' !!

Is an iterative maethod used to find  the most adapt step length ![formula](https://render.githubusercontent.com/render/math?math=alpha_{k}  ). 

Obviously it cane be placed in the steepest descent method, as shown in backtracking.py. 
So, we start with a value of alpha between 0 and 1, we assign to beta the value of the R golden section and be ![formula](https://render.githubusercontent.com/render/math?math=x_{0}  ) a random starting point, it follows: 

step 1:

![formula](https://render.githubusercontent.com/render/math?math=f_{1}  ) = ![formula](https://render.githubusercontent.com/render/math?math=f(x_{0})  ) + ![formula](https://render.githubusercontent.com/render/math?math=alpha  ) * ![formula](https://render.githubusercontent.com/render/math?math=p  ) 

step 2:

if ![formula](https://render.githubusercontent.com/render/math?math=f_{2}  )  < ![formula](https://render.githubusercontent.com/render/math?math=f ) we stop; else
 
step 3:

![formula](https://render.githubusercontent.com/render/math?math=alpha  ) = ![formula](https://render.githubusercontent.com/render/math?math=beta ) * ![formula](https://render.githubusercontent.com/render/math?math=alpha  )  then go back to step 1 and iterate until convergence is reached.

## Newton - Raphson

