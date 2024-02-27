This program can execute gradient descent algorithm for any cost function. Solve_Differential.py uses sympy to find the differentials of the functions which can be used in the Gradient_Descent.py to find the convergence point. Planning to update further improvements as it happens.

Reference:

Convex Optimization by Stephen Boyd and Lieven Vandenberghe

Algorithm 9.3 Gradient descent method. given a starting point x ∈ dom f .
repeat
1. ∆x := −∇f(x).
2. Line search. Choose step size t via exact or backtracking line search. 3. Update. x := x + t∆x.
until stopping criterion is satisfied.
3. Stopping Criterion: ‖∇f(x)‖ < 1e−4
