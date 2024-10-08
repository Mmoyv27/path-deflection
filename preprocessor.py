import numpy as np

# Function to populate array from file input of LiDAR readings
def process_lidar_file(file_path):
    lidar_readings = []
    
    with open(file_path, 'r') as file:
        for line in file:
            # Try to parse the distance and angle from the line
            try:
                # Split the line by whitespace, assuming it has this format: "distance m angle deg"
                parts = line.split()
                
                if len(parts) != 4:
                    print(f"Skipping malformed line: {line.strip()}")
                    continue
                
                # Extract the distance and angle
                distance = float(parts[0])
                angle = float(parts[2])
                
                # Append the valid reading to the list
                lidar_readings.append((distance, angle))
                
            except Exception as e:
                print(f"Error processing line: {line.strip()} - {e}")
                continue
    
    return np.array(lidar_readings)
