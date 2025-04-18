Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # define class to descrbe fav animal
... class Otter:
...     def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
...         self.arm_length = arm_length  # float
...         self.leg_length = leg_length  # float
...         self.num_eyes = num_eyes      # int
...         self.has_tail = has_tail      # bool
...         self.is_furry = is_furry      # bool
... 
...     # member function to print charascteristics 
...     def describe(self):
...         print("Animal: Otter")
...         print("Arm length:", self.arm_length, "inches")
...         print("Leg length:", self.leg_length, "inches")
...         print("Number of eyes:", self.num_eyes)
...         print("Has a tail:", self.has_tail)
...         print("Is furry:", self.is_furry)
... 
... # Create an instance of the Otter class
... my_otter = Otter(6.0, 8.0, 2, True, True)
... 
... # Call the describe function to print the characteristics
... my_otter.describe()
