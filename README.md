This program can execute gradient descent algorithm for any cost function. Solve_Differential.py uses sympy to find the differentials of the functions which can be used in the Gradient_Descent.py to find the convergence point. Planning to update further improvements as it happens.

What happens here:

1. ∆x := −∇f(x).
2. α is chosen at random in the interval (0,1)
3. 3. Update. x := x + α∆x until stopping criterion is satisfied
4. Stopping Criterion: ‖∇f(x)‖ < 1e−4
