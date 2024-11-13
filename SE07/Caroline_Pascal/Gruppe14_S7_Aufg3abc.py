import numpy as np
import matplotlib.pyplot as plt

# a) 
# Data points
years = np.array([1997, 1999, 2006, 2010])
days = np.array([150, 104, 172, 152])

# Shift the time axis
shifted_years = years - years[0]

# Create a polynomial of degree 3
poly = np.polyfit(shifted_years, days, 3)

# Calculate the polynomial values for a fine time axis
fine_years = np.arange(0, 13, 0.1)
poly_values = np.polyval(poly, fine_years)

# Plot the data points and the polynomial
plt.plot(shifted_years, days, 'o', label='Data points')
plt.plot(fine_years, poly_values, label='Polynomial')
plt.xlabel('Years (shifted)')
plt.ylabel('Number of days')
plt.title('UV-Radiation in Hawaii')
plt.legend()
plt.show()

# b) 
# Predict the values for years 2003 and 2004
shifted_years_2003 = 2003 - years[0]
shifted_years_2004 = 2004 - years[0]
predicted_days_2003 = np.polyval(poly, shifted_years_2003)
predicted_days_2004 = np.polyval(poly, shifted_years_2004)

print(f"Predicted number of days for 2003: {predicted_days_2003}")
print(f"Predicted number of days for 2004: {predicted_days_2004}")

# c)
# Use numpy.polyfit to calculate the polynomial coefficients
poly_fit = np.polyfit(shifted_years, days, 3)

# Calculate the polynomial values for years 2003 and 2004
predicted_days_fit_2003 = np.polyval(poly_fit, shifted_years_2003)
predicted_days_fit_2004 = np.polyval(poly_fit, shifted_years_2004)

print(f"Predicted number of days for 2003 using numpy.polyfit: {predicted_days_fit_2003}")
print(f"Predicted number of days for 2004 using numpy.polyfit: {predicted_days_fit_2004}")

# Plotting for comparison
plt.plot(shifted_years, days, 'o', label='Data points')
plt.plot(fine_years, poly_values, label='Original Polynomial Fit')
plt.plot(fine_years, np.polyval(poly_fit, fine_years), label='Numpy Polyfit', linestyle='--')
plt.axvline(x=shifted_years_2003, color='r', linestyle=':', label='2003 Estimate')
plt.axvline(x=shifted_years_2004, color='g', linestyle=':', label='2004 Estimate')
plt.xlabel('Years (shifted)')
plt.ylabel('Number of days')
plt.title('Comparison of Polynomial Fits')
plt.legend()
plt.show()

