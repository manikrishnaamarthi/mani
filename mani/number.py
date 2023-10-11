def fibonacci(n):
  """Returns the nth Fibonacci number."""
  if n < 0:
    raise ValueError("Fibonacci numbers are not defined for negative n")
  elif n == 0 or n == 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
  """Prints the first 100 Fibonacci numbers."""
  for i in range(100):
    print(fibonacci(i))

if __name__ == "__main__":
  main()
