# main.py

from polar_histogram import process_and_plot_histogram

def main():
    # Path to the LiDAR data file
    lidar_file = "lidar2.txt"  # Replace with actual path

    # Call the function to process the LiDAR data and plot the histogram
    process_and_plot_histogram(lidar_file)

if __name__ == "__main__":
    main()
