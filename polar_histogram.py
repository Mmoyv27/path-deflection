# polar_histogram.py

import numpy as np
import matplotlib.pyplot as plt
from math import pi
from preprocessor import process_lidar_file  # Importing preprocessor

# Constants
a = 1.0  # Arbitrary constant
b = 0.1  # Arbitrary constant
confidence_value = 0.9  # Example confidence value
threshold = 0.5  # Define a meaningful threshold for object density

# Function to calculate object densities based on LiDAR readings
def calculate_object_densities(lidar_readings):
    num_sectors = 68  # Assuming 5 degree resolution (-170 to 170 degrees)
    object_densities = np.zeros(num_sectors)
    
    for distance, angle in lidar_readings:
        if distance >= 654:  # Ignore out-of-range readings for obstacle density
            continue
        
        # Adjust angle range to fit -170° to +170°
        angle = (angle - 180) if angle > 170 else angle
        
        # Convert angle to sector index (for -170° to +170° range)
        sector_index = int((angle + 170) / 5)  # Map -170 to 0, and 170 to num_sectors - 1
        sector_index = min(sector_index, num_sectors - 1)  # Boundary check
        
        # Calculate obstacle vector magnitude m_ij
        distance_factor = a - b * distance
        m_ij = (confidence_value ** 2) * distance_factor
        
        # Accumulate obstacle densities in corresponding sector
        object_densities[sector_index] += max(m_ij, 0)  # Avoid negative densities

    return object_densities

# Function to plot the polar histogram with full sector coloring
def plot_polar_histogram(object_densities, threshold):
    num_sectors = len(object_densities)
    # Adjust the theta range for -170 to +170 degrees
    theta = np.linspace(-170 * pi / 180, 170 * pi / 180, num_sectors, endpoint=False)
    
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

    # No need for theta offset; we're already handling the angle mapping
    ax.set_theta_zero_location("N")  # Set 0° to be directly ahead
    ax.set_theta_direction(-1)  # Ensure clockwise angles go right (like a compass)

    # Customizing the sectors to fill with color based on the threshold
    for i, density in enumerate(object_densities):
        # Set color based on threshold
        color = 'red' if density > threshold else 'green'
        
        # Plot filled sectors instead of bars
        ax.fill_between([theta[i], theta[i] + 2 * pi / num_sectors], 0, 1, color=color, alpha=0.6)

    plt.title(f"Polar Histogram - Obstacle Densities (Threshold: {threshold})")
    plt.show()

# New function to handle everything for external calls
def process_and_plot_histogram(lidar_file):
    # Use the preprocessor to get LiDAR data
    lidar_readings = process_lidar_file(lidar_file)

    # Step 1: Calculate object densities
    object_densities = calculate_object_densities(lidar_readings)

    # Step 2: Plot the polar histogram with full sector coloring
    plot_polar_histogram(object_densities, threshold)

