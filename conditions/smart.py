# Problem: Smart Thermostat Alert System
# If device status is "active" AND temperature > 35, show "High temperature alert!"
# Else if device is active but temp <= 35, show "Temperature is normal"
# If device is offline, show "Device is offline"

# Device configuration
device_status = "active"  # Can be "active" or "offline"
temp = 38  # Current temperature

# Nested conditional statements
if device_status == "active":
    # Device is active, now check temperature
    if temp > 35:
        print("High temperature alert!")
    else:
        print("Temperature is normal")
else:
    # Device is not active
    print("Device is offline")

