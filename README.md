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
![equation](<img src="http://latex.codecogs.com/svg.latex?&space;&space;&space;&space;&space;&space;\left\{&space;&space;&space;&space;&space;&space;\begin{array}{ll}&space;&space;&space;&space;&space;&space;&space;&space;&space;&space;&space;&space;\frac{-d^2u(x)}{dx^2}-u=sinx&space;\\&space;&space;&space;&space;&space;&space;&space;&space;&space;&space;&space;&space;u(0)=0\\&space;&space;&space;&space;&space;&space;&space;&space;&space;&space;&space;&space;\frac{du(2)}{dx}-u(2)=0\\&space;&space;&space;&space;&space;&space;\end{array}&space;&space;&space;&space;&space;&space;&space;\right.&space;&space;" title="http://latex.codecogs.com/svg.latex? \left\{ \begin{array}{ll} \frac{-d^2u(x)}{dx^2}-u=sinx \\ u(0)=0\\ \frac{du(2)}{dx}-u(2)=0\\ \end{array} \right. " />)
### The above function can be transformed into the form:

$$
u(2)v(2) -  \int_{0}^{2} u'(x)v'(x) - u(x)v(x) \,dx = - \int_{0}^{2} v(x)sin(x) \,dx 
$$

### Remaining steps and calculations are done with *numpy*, *scipy* and *matplotlib* libraries.

<p align="center">
![Result graph](/result.PNG)
</p>
