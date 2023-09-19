"""
Description: [A brief description of the file's purpose]
Author: [Your name]
Date: [Creation or modification date]
Usage: [How to use or run the file, if applicable]
"""


#SIMPLE DATA TYPES
# Declare and initialize the variable with a name
name = "Simran"  # Replace "John" with your first name

# Print the value and datatype of the variable
print(f"value: {name} type: {type(name).__name__}")
# Declare and initialize the variable for Manitoba Driver's Licence status
has_licence = True  # Change to False if you don't have a valid licence

# Print the value and datatype of the variable
print(f"value: {has_licence} type: {type(has_licence).__name__}")

# Declare and initialize the variable for the current year
current_year = 2023  

# Print the value and datatype of the variable
print(f"this year: {current_year} type: {type(current_year).__name__}")


# Add 1 to the year to get the next year
next_year = current_year + 1

# Print the value and datatype of the next year
print(f"next year: {next_year} type: {type(next_year).__name__}")

#CALCULATIONS
# Constants for Canadian GST and Manitoba PST rates
GST_RATE = 0.05  # Assuming 5% for GST. Please update this if the rate has changed.
PST_RATE = 0.07  # Assuming 7% for Manitoba PST. Please update this if the rate has changed.

# Declare a variable for the vehicle price and initialize it
vehicle_price = 80000.50  # Sample value, you can adjust this as needed

# Calculate GST and PST tax values for the vehicle
gst_value = vehicle_price * GST_RATE
pst_value = vehicle_price * PST_RATE

# Determine the total cost of the vehicle
total_cost = vehicle_price + gst_value + pst_value

# Print results using an f-string for formatted output
output = f"pre-tax value: ${vehicle_price:,.2f} PST: ${pst_value:,.2f} GST: ${gst_value:,.2f} total: ${total_cost:,.2f}"
print(output)


#LISTS


#TUPLES

#DICTIONARIES

#SETS

