Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
... 
... def main():
...     x = np.linspace(0, 2, 1000)
...     y = np.sin(x)
... 
...     print("x       sin(x)")
...     for i in range(len(x)):
...         print(f"{x[i]:.5f}   {y[i]:.5f}")
... 
... if __name__ == "__main__":
...     main()
