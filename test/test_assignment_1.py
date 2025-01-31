import math

#Cuneiform tablet approximation
def approximate_sqrt_2(initial_guess=1.5, tolerance=1e-10):
  # Starting value
  x = initial_guess
  iteration_count = 0

  while True:
      # Calculate the next approximation
      x_next = (x / 2) + (1 / x)
      iteration_count += 1

      # Check for convergence
      if abs(x_next - x) < tolerance:
          break

      x = x_next

  return x, iteration_count

# Calculate the approximation
approximation, iterations = approximate_sqrt_2()
print(f"Approximate square root of 2: {approximation} (found in {iterations} iterations)")

#bi-section method

def bisection_method(func, a, b, tolerance=1e-3):
    # Check if a and b bracket a root
    if func(a) * func(b) >= 0:
        raise ValueError("The function must have different signs at a and b.")

    # Calculate the minimum number of iterations needed
    def calculate_iterations(a, b, tolerance):
        return math.ceil(math.log2((b - a) / tolerance))

    # Calculate the required number of iterations
    required_iterations = calculate_iterations(a, b, tolerance)
    print(f"Minimum required iterations: {required_iterations}")

    iteration_count = 0
    while (b - a) / 2 > tolerance:
        midpoint = (a + b) / 2
        if func(midpoint) == 0:  # Found exact root
            return midpoint

        # Update the interval
        if func(midpoint) * func(a) < 0:
            b = midpoint
        else:
            a = midpoint

        iteration_count += 1

        # Check if we've reached the required accuracy
        if iteration_count >= required_iterations:
            break

    # Return the midpoint as the approximate root and the number of iterations
    return (a + b) / 2, iteration_count

# Define the function f(x)
def func(x):
    return x**3 + 4*x**2 - 10

# Define the interval [a, b]
a = 1
b = 2

# Calculate the root
approx_root, actual_iterations = bisection_method(func, a, b)
print(f"Approximate root: {approx_root}")
print(f"Actual iterations taken: {actual_iterations}")

#Fixed point iteration
def fixed_point_iteration(g, initial_guess, tolerance=1e-4, max_iterations=1000):
    x_n = initial_guess
    iteration_count = 0

    while iteration_count < max_iterations:
        x_n1 = g(x_n)  # Compute the next iteration

        # Check for convergence
        if abs(x_n1 - x_n) < tolerance:
            return x_n1, iteration_count

        x_n = x_n1
        iteration_count += 1

    raise ValueError("Maximum iterations exceeded without convergence.")

# Define the function g(x) for fixed-point iteration
def g(x):
    return math.tan(x)

# Initial guess (can be any value in the interval [4, 5])
initial_guess = 4.5

# Calculate the fixed-point approximation
approx_root, actual_iterations = fixed_point_iteration(g, initial_guess)
print(f"Approximate root: {approx_root}")
print(f"Actual iterations taken: {actual_iterations}")


#Newton-Raphson method
def newtons_method(func, derivative, initial_guess, tolerance=1e-4, max_iterations=1000):
    x_n = initial_guess
    iteration_count = 0

    while iteration_count < max_iterations:
        f_x_n = func(x_n)
        f_prime_x_n = derivative(x_n)

        # Check if the derivative is not zero to avoid division by zero
        if f_prime_x_n == 0:
            raise ValueError("Derivative is zero. No solution found.")

        # Update the approximation using Newton's formula
        x_n1 = x_n - f_x_n / f_prime_x_n

        # Check for convergence
        if abs(x_n1 - x_n) < tolerance:
            return x_n1, iteration_count

        x_n = x_n1
        iteration_count += 1

    raise ValueError("Maximum iterations exceeded without convergence.")

# Define the function f(x) and its derivative f'(x)
def func(x):
    return math.cos(x) - x

def derivative(x):
    return -math.sin(x) - 1

# Initial guess (can be any value in the interval [0, pi/2])
initial_guess = 0.5

# Calculate the root using Newton's method
approx_root, actual_iterations = newtons_method(func, derivative, initial_guess)
print(f"Approximate root: {approx_root}")
print(f"Actual iterations taken: {actual_iterations}")
