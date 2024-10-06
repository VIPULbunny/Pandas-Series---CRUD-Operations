import pandas as pd
import numpy as np

# C --> CREATION

# Creating an empty series (commented out because it's not used here)
# s = pd.Series()

# Create a series using a NumPy array
data = np.array([12, 45, 36, 89]) # Data to be stored in the series
s = pd.Series(data)
print(s)  # Output: Series with values 12, 45, 36, 89 indexed by default

# Create a series using a dictionary
data = {"a": 10, "b": 40, "c": 90, "d": 95}
s = pd.Series(data)
print(s)  # Output: Series with dictionary values, indexed by keys of the dictionary

# Create a series using a dictionary with custom index
s = pd.Series(data, index=["w", "x", "y", "z"])
print(s)  # Output: Series with custom index replacing the default dictionary keys

# U --> UPDATION

# Create a Series using NumPy array
data = np.array([12, 35, 49, 80, 7, -10, 21, -0.5, -7, -30])
s = pd.Series(data)
print(s[0:3])  # Output: First three elements of the series

# Modify values and print conditional results
data = {"a": 10, "b": 40, "c": 90, "d": 95}
s = pd.Series(data, index=["c", "d", "e", "b", "a"])
print(s[["c", "b"]])  # Output: Series elements with index 'c' and 'b'

s["e"] = 65.5  # Update element 'e'
print(s)  # Output: Updated series

# Print elements greater than 50
print(s[s > 50])

# Print series metadata
print(s.ndim)   # Output: Dimension of the series (1)
print(s.shape)  # Output: Shape of the series
print(s.size)   # Output: Number of elements
print(s.index)  # Output: Index of the series
print(s.values) # Output: Values of the series

# D --> DELETION

# Drop elements by index
print(s.drop(["a"]))     # Output: Series without element 'a'
print(s.drop(["a", "c"]))  # Output: Series without elements 'a' and 'c'

# Print series after operations
print(s + 1)  # Output: Series with each element increased by 1
print(s * 2)  # Output: Series with each element multiplied by 2
print(s / 2)  # Output: Series with each element divided by 2