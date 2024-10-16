import matplotlib.pyplot as plt

# Define the points
A = (4, -3)
B = (8, 5)
P = (7, 3)  # Point dividing the segment in the ratio 3:1

# Create the figure and axis
plt.figure(figsize=(8, 6))

# Plot the points A, B, and P
plt.plot(*A, 'ro', label='A(4, -3)')  # Point A in red
plt.plot(*B, 'bo', label='B(8, 5)')    # Point B in blue
plt.plot(*P, 'go', label='P(7, 3)', markersize=10)  # Point P in green

# Draw the line segment AB
plt.plot([A[0], B[0]], [A[1], B[1]], 'k--', label='Line Segment AB')

# Annotate the points
plt.text(A[0], A[1], ' A', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
plt.text(B[0], B[1], ' B', fontsize=12, verticalalignment='bottom', horizontalalignment='left')
plt.text(P[0], P[1], ' P', fontsize=12, verticalalignment='bottom', horizontalalignment='left')

# Set the limits and labels
plt.xlim(2, 10)
plt.ylim(-5, 7)
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.title('Line Segment AB with Dividing Point P')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

# Save the plot as a PNG file
plt.savefig('IMG.png', format='png')

# Show the plot
plt.show()
