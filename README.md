
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

Now, depending on which condition occurs, we define a new interval around the minimum indicated by 2 new points: ![formula](https://render.githubusercontent.com/render/math?math=x_{1}^(new)  ) and ![formula](https://render.githubusercontent.com/render/math?math=x_{2}^(new)  )

So:
> 1. if ![formula](https://render.githubusercontent.com/render/math?math=f(x_{3})  ) < ![formula](https://render.githubusercontent.com/render/math?math=f(x_{3})  ):

   ![formula](https://render.githubusercontent.com/render/math?math=x_{1}^(new)  )=![formula](https://render.githubusercontent.com/render/math?math=x_{1}  )   
   ![formula](https://render.githubusercontent.com/render/math?math=x_{2}^(new)  )=![formula](https://render.githubusercontent.com/render/math?math=x_{4}  )
   
> 2. if ![formula](https://render.githubusercontent.com/render/math?math=f(x_{3})  ) > ![formula](https://render.githubusercontent.com/render/math?math=f(x_{3})  ):

   ![formula](https://render.githubusercontent.com/render/math?math=x_{1}^(new)  )=![formula](https://render.githubusercontent.com/render/math?math=x_{3}  )     
   ![formula](https://render.githubusercontent.com/render/math?math=x_{2}^(new)  )=![formula](https://render.githubusercontent.com/render/math?math=x_{2}  )
    
    
and so forth, we iterate until the convergence is not reached.
## Golden section Search
    
    
  



