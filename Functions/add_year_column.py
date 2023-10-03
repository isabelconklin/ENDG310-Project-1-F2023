import csv

def add_year_column(input_file, output_file, new_column_name, new_column_values):
    """
    Add a year column to an existing csv file

    Parameters:
        input_file (pd.DataFrame): The DataFrame containing the data.
        output_file (pd.DataFrame): The DataFrame containing the updated data.
        new_column_name (str): The name of the new column.
        new_column_values (str): The value for the new column.
    """
    # Open the input CSV file
    with open(input_file, mode='r') as file:
        reader = csv.reader(file)
        # Read the existing data and headers if necessary
        data = list(reader)

    # Add the new column header
    data[0].append(new_column_name)

    # Add data to the new column for each row
    for i in range(1, len(data)):
        data[i].append(new_column_values)
#[i - 1]
    # Write the updated data back to the output CSV file
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

# # Example usage:
# input_file = 'your_input_file.csv'
# output_file = 'your_output_file.csv'
# new_column_name = 'NewColumn'
# new_column_values = ['Value1', 'Value2', 'Value3', 'Value4']

# add_column_to_csv(input_file, output_file, new_column_name, new_column_values)
