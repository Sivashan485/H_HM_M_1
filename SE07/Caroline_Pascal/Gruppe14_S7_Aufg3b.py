import numpy as np
import matplotlib.pyplot as plt

# Data from the table
years = [1997, 1999, 2006, 2010]
days = [150, 104, 172, 152]

# Shift the years for a better conditioned system
shifted_years = np.array(years) - years[0]

# Fit a third-degree polynomial
coefficients = np.polyfit(shifted_years, days, 3)

# Create a polynomial function
polynomial = np.poly1d(coefficients)

# Plot the data and the polynomial
plt.plot(years, days, 'o', label='Data')
plt.plot(np.linspace(years[0], years[-1], 100), polynomial(np.linspace(shifted_years[0], shifted_years[-1], 100)), label='Polynomial')

# Predict values for 2003 and 2004
predicted_2003 = polynomial(2003 - years[0])
predicted_2004 = polynomial(2004 - years[0])
print(f"Predicted UV Days for 2003: {predicted_2003:.2f}")
print(f"Predicted UV Days for 2004: {predicted_2004:.2f}")

# Plot
plt.xlabel('Year')
plt.ylabel('Number of Days')
plt.title('UV Radiation Days in Hawaii')
plt.legend()
plt.show()
