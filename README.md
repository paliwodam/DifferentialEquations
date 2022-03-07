# Differential Equations

### Solving **the equation of acoustic vibrations of material layers** using ***the finite element method (FEM)*** and drawing a graph of the obtained function.
<!-- <img src="https://latex.codecogs.com/gif.latex?s=\text {
      $$ \left\{
      \begin{array}{ll}
            \frac{-d^2u(x)}{dx^2}-u=sinx \\
            u(0)=0\\
            \frac{du(2)}{dx}-u(2)=0\\
      \end{array} 
      \right.  $$ 
 } " />  -->
![equation](http://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BWhite%7D%20%5Cleft%5C%7B%20%20%20%20%20%20%5Cbegin%7Barray%7D%7Bll%7D%20%20%20%20%20%20%20%20%20%20%20%20%5Cfrac%7B-d%5E2u(x)%7D%7Bdx%5E2%7D-u=sinx%20%5C%5C%20%20%20%20%20%20%20%20%20%20%20%20u(0)=0%5C%5C%20%20%20%20%20%20%20%20%20%20%20%20%5Cfrac%7Bdu(2)%7D%7Bdx%7D-u(2)=0%5C%5C%20%20%20%20%20%20%5Cend%7Barray%7D%20%20%20%20%20%20%20%5Cright.%20%7D)
### The above function can be transformed into the form:
<!-- 
$$
u(2)v(2) -  \int_{0}^{2} u'(x)v'(x) - u(x)v(x) \,dx = - \int_{0}^{2} v(x)sin(x) \,dx 
$$ -->
![equation2](http://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BWhite%7D%20u(2)v(2)%20-%20%20%5Cint_%7B0%7D%5E%7B2%7D%20u'(x)v'(x)%20-%20u(x)v(x)%20%5C,dx%20=%20-%20%5Cint_%7B0%7D%5E%7B2%7D%20v(x)sin(x)%20%5C,dx%20%7D)
### Remaining steps and calculations are done with *numpy*, *scipy* and *matplotlib* libraries.

## Graph of the obtained function

![Result graph](/result.PNG)
