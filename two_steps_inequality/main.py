import matplotlib.pyplot as plt
import numpy as np

# Define the inequality 10c + 5 <= 45
# We rearrange to c <= 4
x_values = np.linspace(-10, 10, 400)  # Range of x-values for graphing
y_values = 10 * x_values + 5

# Setting up the plot
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label=r'$y = 10c + 5$', color='blue')
plt.axhline(y=45, color='red', linestyle='--', label=r'$y = 45$')
plt.fill_between(x_values, y_values, 45, where=(y_values <= 45), color='blue', alpha=0.2)

# Add labels and title
plt.xlabel('c')
plt.ylabel('y')
plt.title('Graph of 10c + 5 <= 45')
plt.legend(loc="upper left")

# Add the line for c <= 4
plt.axvline(x=4, color='green', linestyle='-.', label=r'$c \leq 4$')
plt.legend()

# Display plot
plt.grid(True)
plt.show()
