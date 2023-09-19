"""
Description: [Python code]
Author: [Simran]
Date: [19/09/2023]
Usage: [Select the code and run]
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
# 1. Declare a list and initialize it to the values 1 through 10 inclusive.
numbers_list = list(range(1, 11))

# 4. Add the name "Simran" to the list between the values of 5 and 6.
numbers_list.insert(5, "Simran")

# 6. Remove the number 9 from the list.
numbers_list.remove(9)

# 8. Create a second list containing the values 'A', 'B', and 'C'.
letters_list = ['A', 'B', 'C']

# 9. Create a third list containing the values of the first and second lists.
combined_list = numbers_list + letters_list

# Print the lists
print("List after adding Simran:", numbers_list)
print("Combined list:", combined_list)


#TUPLES
# 1. Declare a tuple and initialize it to the names of 4 Canadian provinces.
provinces_tuple = ("Ontario", "Quebec", "British Columbia", "Alberta")

# 2. Print the tuple.
print(provinces_tuple)

# 3. Verify a tuple has been created by printing the data type of the tuple.
print(type(provinces_tuple))

#DICTIONARIES
# 1. Declare a dictionary with the specified keys and values.
currency_dict = {
    'nickel': 0.05,
    'dime': 0.10,
    'quarter': 0.25
}

# 2. Print the dictionary.
print(currency_dict)

# 3. Verify a dictionary has been created by printing the data type of the dictionary.
print(type(currency_dict))

# 4. Modify the values of each of the items in the dictionary to use whole numbers.
currency_dict['nickel'] = 5
currency_dict['dime'] = 10
currency_dict['quarter'] = 25

# 5. Print the dictionary.
print(currency_dict)

# 6. Add two items to the dictionary representing the loonie and toonie.
currency_dict['loonie'] = 100
currency_dict['toonie'] = 200

# 7. Print the dictionary.
print(currency_dict)


#SETS

# 1. Declare a set containing even numbers between 2 and 20.
even_numbers_set = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}

# 2. Print the set.
print(even_numbers_set)

# 3. Verify a set has been created by printing the data type of the set.
print(type(even_numbers_set))

# 4. Declare a set containing multiples of 5 between 5 and 20.
multiples_of_5_set = {5, 10, 15, 20}

# 5. Print the set.
print(multiples_of_5_set)

# 6. Declare a set which contains each unique value of the two sets created above.
combined_set = even_numbers_set.union(multiples_of_5_set)

# 7. Print the set.
print(combined_set)

# 8. Declare a set which contains only those values that appear in both sets.
intersection_set = even_numbers_set.intersection(multiples_of_5_set)

# 9. Print the set.
print(intersection_set)

# 10. Declare a set which contains only those values that appear in the first set but not in the second set.
difference_set_1 = even_numbers_set.difference(multiples_of_5_set)

# 11. Print the set.
print(difference_set_1)

# 12. Declare a set which contains only those values that appear in the second set but not in the first set.
difference_set_2 = multiples_of_5_set.difference(even_numbers_set)

# 13. Print the set.
print(difference_set_2)
