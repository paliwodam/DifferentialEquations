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
![equation](http://latex.codecogs.com/svg.latex?%20%20%20%20%20%20%5Cleft%5C%7B%20%20%20%20%20%20%5Cbegin%7Barray%7D%7Bll%7D%20%20%20%20%20%20%20%20%20%20%20%20%5Cfrac%7B-d%5E2u(x)%7D%7Bdx%5E2%7D-u=sinx%20%5C%5C%20%20%20%20%20%20%20%20%20%20%20%20u(0)=0%5C%5C%20%20%20%20%20%20%20%20%20%20%20%20%5Cfrac%7Bdu(2)%7D%7Bdx%7D-u(2)=0%5C%5C%20%20%20%20%20%20%5Cend%7Barray%7D%20%20%20%20%20%20%20%5Cright.%20%20)
### The above function can be transformed into the form:

$$
u(2)v(2) -  \int_{0}^{2} u'(x)v'(x) - u(x)v(x) \,dx = - \int_{0}^{2} v(x)sin(x) \,dx 
$$

### Remaining steps and calculations are done with *numpy*, *scipy* and *matplotlib* libraries.

![Result graph](/result.PNG)
