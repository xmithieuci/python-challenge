# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0

# Add more variables to track other necessary financial data
net_change_list = []
months = []
greatest_increase = {"month": "", "amount": float('-inf')}
greatest_decrease = {"month": "", "amount": float('inf')}

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1

    # Track the total and net change
    total_net += int(first_row[1])
    last_net = int(first_row[1])

    # Process each row of data
    for row in reader:

        # Track the total
        total_months += 1
        total_net += int(row[1])
        
        # Calculate the net change for each month
        net_change = int(row[1]) - last_net
        net_change_list.append(net_change)
        months.append(row[0])

        # Calculate the greatest increase in profits (month and amount)
        if net_change > greatest_increase["amount"]:
            greatest_increase["month"] = row[0]
            greatest_increase["amount"] = net_change        

        # Calculate the greatest decrease in losses (month and amount)
        if net_change < greatest_decrease["amount"]:
            greatest_decrease["month"] = row[0]
            greatest_decrease["amount"] = net_change

        # Update last_net for the next iteration
        last_net = int(row[1])

# Calculate the average net change across the months
average_change = sum(net_change_list) / len(net_change_list) if net_change_list else 0

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"\n----------------------------\n"
    f"\nTotal Months: {total_months}\n"
    f"\nTotal: ${total_net}\n"
    f"\nAverage Change: ${average_change:.2f}\n"
    f"\nGreatest Increase in Profits: {greatest_increase['month']} (${greatest_increase['amount']})\n"
    f"\nGreatest Decrease in Profits: {greatest_decrease['month']} (${greatest_decrease['amount']})\n")

# Print the output
print(output)

# Create the output directory if it doesn't exist
output_dir = os.path.dirname(file_to_output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
