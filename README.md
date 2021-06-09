DarinaT - a library of algorithms for one-dimensional minimization and stochastic minimization methods. It includes 9 optimization algorithms and each can be used to solve a specific optimization problem. Below are the principles of their work.

###Provides:
  <br>-Algorithms for optimizing zero, first and second order. <br>
  <br>-Algorithms for stochastic optimization methods. <br>
  <br>-Test functions for algorithms.<br>
  
###Algorithm has arguments listed below:
 <br> n: number of agents<br>
 <br> function: test function<br>
 <br> lb: lower limits for plot axes<br>
 <br> ub: upper limits for plot axes<br>
 <br> dimension: space dimension<br>
 <br> k: number of iterations<br>
 <br> eps: accuracy of calculations<br>
  
###This module implements the following methods: 
  <br>-Dichotomy method<br>
  <br>-Gold Section Method<br>
  <br>-Quadratic approximation method<br>
  <br>-Midpoint Method<br>
  <br>-Chord method<br>
  <br>-Newton Method<br>
  <br>-Simulated Annealing<br>
  <br>-Particle Swarm Optimization<br>
  <br>-Grey Wolf Optimizer<br>
  
###Then there is a brief description of these methods.

####Dichotomy method

Bisection method is the simplest among all the numerical schemes to solve the transcendental equations. This scheme is based on the intermediate value theorem for continuous functions. Consider a transcendental equation f (x) = 0  which has a zero in the interval [a,b] and f (a) * f (b) < 0. Bisection scheme computes the zero, say c, by repeatedly halving the interval [a,b]. That is, starting with m= (a+b) / 2 the interval [a,b] is replaced either with [c,b] or with [a,c] depending on the sign of f (a) * f (m) . This process is continued until the zero is obtained. Since the zero is obtained numerically the value of m may not exactly match with all the decimal places of the analytical solution of f (x) = 0 in the interval [a,b]. Hence any one of the following mechanisms can be used to stop the bisection iterations :

  -Fixing a priori the total number of bisection iterations N i.e., the length of the interval or the maximum error after N iterations in this case is less than | b-a | / 2N.
  -By testing the condition  | mi - m i-1| (where i are the iteration number) less than some tolerance limit, say epsilon, fixed a priori. 
  -By testing the condition | f (mi ) | less than some tolerance limit alpha again fixed a priori.




####Golden Section Method

The golden section search method in one dimension is used to find a minimum for a unimodal continuous function of a single variable over an interval without using derivatives. Unimodal in  [a;b] means having only one extremum in [a;b]. The idea is similar to the bisection method for finding a zero: narrowing the interval containing the minimum (being called a bracketing interval) until a specified accuracy is reached. When doing so, we want two things:

  -an optimal reduction of the size of the bracketing interval and
  -a minimal number of function calls.
  
  
  
  
####Quadratic approximation method

The simplest version of polynomial interpolation is quadratic approximation based on the fact that the function taking the minimum the value at the inside point of the interval must be at least quadratic. If the function is linear, then its optimal value can be achieved only in one of the two interval limit points. Thus, when implementing the method estimating and using a quadratic approximation is assumed to be bounded interval can be approximated by the function quadratic a polynomial, and then use the plotted  approximation scheme for estimating the coordinate of the true minimum point of the function.




####Midpoint Method

The midpoint method is a variant of the bisection method. Successive reductions of the uncertainty interval are made based on an estimate of the derivative of the minimized function at the center of the current interval.

Start stage To start the method, you must specify [a1, b1] - the initial localization interval of the minimum, at the boundaries of which the characters of the derivatives are different. Next, set the counter of the number of iterations k = 1.

Basic Step Take the trial point x at the center of the current interval and check the search termination criteria. Then shorten the current interval




####Chord method

If an interpolating curve follows very closely to the data polygon, the length of the curve segment between two adjacent data points would be very close to the length of the chord of these two data points, and the the length of the interpolating curve would also be very close to the total length of the data polygon. In the figure below, each curve segment of an interpolating polynomial is very close to the length of its supporting chord, and the length of the curve is close to the length of the data polygon. Therefore, if the domain is subdivided according to the distribution of the chord lengths, the parameters will be an approximation of the arc-length parameterization. This is the merit of the chord length or chordal method.





####Newton Method

In numerical analysis, Newton's method, also known as the Newton–Raphson method, named after Isaac Newton and Joseph Raphson, is a root-finding algorithm which produces successively better approximations to the roots (or zeroes) of a real-valued function. The most basic version starts with a single-variable function f defined for a real variable x, the function's derivative f ′, and an initial guess x0 for a root of f. If the function satisfies sufficient assumptions and the initial guess is close, then:  x1 = x0 - f(x0)/df(x0)  is a better approximation of the root than x0. Geometrically, (x1, 0) is the intersection of the x-axis and the tangent of the graph of f at (x0, f (x0)): that is, the improved guess is the unique root of the linear approximation at the initial point. The process is repeated as  x(n+1) = x(n) - f(x(n))/df(x(n))  until a sufficiently precise value is reached. This algorithm is first in the class of Householder's methods, succeeded by Halley's method. The method can also be extended to complex functions and to systems of equations.





####Simulated Annealing

Simulated annealing (SA) is a probabilistic technique for approximating the global optimum of a given function. Specifically, it is a metaheuristic to approximate global optimization in a large search space for an optimization problem. It is often used when the search space is discrete (e.g., the traveling salesman problem). For problems where finding an approximate global optimum is more important than finding a precise local optimum in a fixed amount of time, simulated annealing may be preferable to exact algorithms such as gradient descent or branch and bound.

The name of the algorithm comes from annealing in metallurgy, a technique involving heating and controlled cooling of a material to increase the size of its crystals and reduce their defects. Both are attributes of the material that depend on their thermodynamic free energy. Heating and cooling the material affects both the temperature and the thermodynamic free energy or Gibbs energy. Simulated annealing can be used for very hard computational optimization problems where exact algorithms fail; even though it usually achieves an approximate solution to the global minimum, it could be enough for many practical problems.

The problems solved by SA are currently formulated by an objective function of many variables, subject to several constraints. In practice, the constraint can be penalized as part of the objective function.





####Particle Swarm Optimization

In computational science, particle swarm optimization (PSO)[1] is a computational method that optimizes a problem by iteratively trying to improve a candidate solution with regard to a given measure of quality. It solves a problem by having a population of candidate solutions, here dubbed particles, and moving these particles around in the search-space according to simple mathematical formula over the particle's position and velocity. Each particle's movement is influenced by its local best known position, but is also guided toward the best known positions in the search-space, which are updated as better positions are found by other particles. This is expected to move the swarm toward the best solutions.

PSO is originally attributed to Kennedy, Eberhart and Shi[2][3] and was first intended for simulating social behaviour,[4] as a stylized representation of the movement of organisms in a bird flock or fish school. The algorithm was simplified and it was observed to be performing optimization. The book by Kennedy and Eberhart[5] describes many philosophical aspects of PSO and swarm intelligence. An extensive survey of PSO applications is made by Poli.[6][7] Recently, a comprehensive review on theoretical and experimental works on PSO has been published by Bonyadi and Michalewicz.[8]

PSO is a metaheuristic as it makes few or no assumptions about the problem being optimized and can search very large spaces of candidate solutions. Also, PSO does not use the gradient of the problem being optimized, which means PSO does not require that the optimization problem be differentiable as is required by classic optimization methods such as gradient descent and quasi-newton methods. However, metaheuristics such as PSO do not guarantee an optimal solution is ever found.





####Grey Wolf Optimizer

This work proposes a new meta-heuristic called Grey Wolf Optimizer (GWO) inspired by grey wolves (Canis lupus). The GWO algorithm mimics the leadership hierarchy and hunting mechanism of grey wolves in nature. Four types of grey wolves such as alpha, beta, delta, and omega are employed for simulating the leadership hierarchy. In addition, the three main steps of hunting, searching for prey, encircling prey, and attacking prey, are implemented. The algorithm is then benchmarked on 29 well-known test functions, and the results are verified by a comparative study with Particle Swarm Optimization (PSO), Gravitational Search Algorithm (GSA), Differential Evolution (DE), Evolutionary Programming (EP), and Evolution Strategy (ES). The results show that the GWO algorithm is able to provide very competitive results compared to these well-known meta-heuristics. The paper also considers solving three classical engineering design problems (tension/compression spring, welded beam, and pressure vessel designs) and presents a real application of the proposed method in the field of optical engineering. The results of the classical engineering design problems and real application prove that the proposed algorithm is applicable to challenging problems with unknown search spaces.
