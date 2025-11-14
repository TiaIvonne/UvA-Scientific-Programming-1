# car_ride
# Ivonne Mendoza
# ivonne@imendoza.io

import matplotlib.pyplot as plt


with open("CarRideData.csv", 'r', errors='replace') as f:
    # read first line of code this is my header for this file
    header = f.readline().strip().split(',')
    # Gets the current numeric index for some columns that I need
    speed_index = header.index('speed')
    timestamp_index = header.index('timestamp')
    latitude_index = header.index('lat')
    longitude_index = header.index('long')
    #Initiates empty list to save data
    time:list = []
    speed:list = []
    latitude:list = []
    longitude:list = []

    #Traverses every line of file and does some operations
    for line in f:
        # Clean and split by commas
        values = line.strip().split(',')
        # Security check
        if len(values) > speed_index:
            #Extracts data contains in the index 6 for speed
            speed_values = values[speed_index]
            # Append every speed values and converts to km/hr
            speed.append(round(float(speed_values) * 3.60, 2))
        if len(values) > timestamp_index:
            #Extracts data from the timestamp index
            timestamp_values = values[timestamp_index]
            time.append(float(timestamp_values))
        if len(values) > latitude_index:
            # same as latitude
            latitude_values = float(values[latitude_index])
            latitude.append(latitude_values)
        if len(values) > longitude_index:
            longitude_values = float(values[longitude_index])
            longitude.append(longitude_values)

    # Calculates total distance
    total_distance:float = 0.0
    for i in range(1, len(time)):
        # Calculates difference between current index - previous one
        time_interval = time[i] - time[i-1]
        # speed is in km/h, so we need to convert back to m/s
        calculate_speed_ms = speed[i] / 3.6 
        total_distance += calculate_speed_ms * time_interval

    print(f'Total distance: {total_distance:.2f} meters')


# Graph 
plt.figure(figsize=(10, 6))
plt.plot(time, speed, label='Speed')
plt.xlabel('Time (seconds)')
plt.ylabel('Speed (km/h)')
plt.title('Car Speed Over Time')
plt.legend()
plt.grid(True)
plt.show()


# Graph 2
# Asign colors depend on some conditions
colors = []
for i in speed:
    if i > 50:
        colors.append('green')
    else:
        colors.append('red')

plt.figure(figsize=(10, 6))
plt.scatter(longitude, latitude, color = colors, s=15)
plt.plot(longitude, latitude)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Car Ride')
plt.legend()
plt.grid(True)
plt.show()

# Close the file
f.close()