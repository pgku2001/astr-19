Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # Define function f(x)
... def f(x):
...     return x**3 + 8
... 
... # Define main function
... def main():
...     # Call the function with x = 9
...     result = f(9)
... 
...     # Print result
...     print("Result:", result)
... 
...     # Check if result is greater than 27
...     if result > 27:
...         print("YAY!")
... 
... # Execute main function
... if __name__ == "__main__":
...     main()
