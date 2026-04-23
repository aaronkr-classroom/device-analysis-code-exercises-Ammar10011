from lib.room_sensor import RoomSensor

# Create sensor objects
sensor1 = RoomSensor("Kitchen", 31, 72, 180)
sensor2 = RoomSensor("Bedroom", 24, 50, 300)
sensor3 = RoomSensor("Balcony", 28, 65, 220)

# Store sensors in a list
sensors = [sensor1, sensor2, sensor3]

# Counters for bonus
comfortable_count = 0
normal_count = 0
warning_count = 0

# Loop through sensors
for sensor in sensors:
    sensor.show_info()

    comfort = sensor.comfort_level()
    light = sensor.light_status()

    print(f"Comfort Level: {comfort}")
    print(f"Light Status: {light}")
    print()

    # Count categories
    if comfort == "Comfortable":
        comfortable_count += 1
    elif comfort == "Warning":
        warning_count += 1
    else:
        normal_count += 1

# Print totals
print("Summary:")
print(f"Comfortable: {comfortable_count}")
print(f"Normal: {normal_count}")
print(f"Warning: {warning_count}")