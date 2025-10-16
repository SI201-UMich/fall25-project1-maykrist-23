# Name: Kristen May
# Student ID: 98342405
# Email: maykrist@umich.edu
# Collaborators: No collaborators 
# AI Usage: Used Claude to help me debug, structure test cases, and break down project instructions.
# When debugging, would provide Claude with the snippet of my code that's having issues and ask it to explain what the code is currently doing.
# When structuring test cases, would ask Claude the differnce between general and edge test cases.
# When breaking down project tasks, would provide Claude with a snippet of the instructions and ask me to explain it to me like I'm five. Helped me understand the task much easier.

import csv
import unittest

def get_data(file):
    # Opens csv file for reading
    with open(file) as fn:
        csv_reader = csv.DictReader(fn)
        data = []
        # Loops through each row in csv file
        for row in csv_reader:
            # Changes numeric values from strings to floats
            for key in ['Sales', 'Quantity', 'Discount', 'Profit']:
                try:
                    # Checks if column exists and has a correspoinding value
                    if row.get(key):
                        # Converts string value to float
                        row[key] = float(row[key])
                except ValueError:
                    # If conversion doesn't work, set value to 0.0
                    row[key] = 0.0
            # Adds row to data list 
            data.append(row)
    # Returns complete list of dictionaries 
    return data 


def avg_furniture_sales_central(superstore_data):
    total = 0.0
    count = 0.0
    # Loop through rows in dataset
    for row in superstore_data:
        # Checks if row meets all conditions 
        if (
            row.get('Category') == 'Furniture'
            and row.get('Region') == 'Central'
            and row.get('Sales') not in (None, '')
        ):
            # Add item's sales to total 
            total += row['Sales']
            count += 1
    # Return 0.0 if no matching items were found 
    if count == 0:
        return 0.0
    # Returns average 
    return total / count


def percent_binders_in_california(superstore_data):
    office_supplies_california = 0
    binders_california = 0
    
    # Loops through each row in dataset 
    for row in superstore_data:
        # Checks if row is office supply item in California 
        if (
            row.get('State') == 'California'
            and row.get('Category') == 'Office Supplies'
        ):
            office_supplies_california += 1
            # Checks if office supply is a binder 
            if row.get('Sub-Category') == 'Binders':
                binders_california += 1
    # Return 0.0 if there are no office supplies in California 
    if office_supplies_california == 0:
            return 0.0 
    # Finds and returns percentage 
    percentage_binders = (binders_california / office_supplies_california) * 100
    return percentage_binders


def write_results(calc1, calc2, filename):
    # Opens file for writing 
    with open(filename, 'w') as file:
        # Writes title, "Project 1 Results:"
        file.write("Project 1 Results:\n")
        # Writes first calculation restul rounded to 2 decimals 
        file.write("Average Central Furniture Sales: $" + str(round(calc1, 2)) + "\n")
        # Writes second calculation result rounded to 2 decimals 
        file.write("Percent of Binders in California: " + str(round(calc2, 2)) + "%\n")

def main():
    # Reads csv file and gets data as list of dictionaries 
    data = get_data('SampleSuperstore.csv')
    
    # Calculates average furniture sales in Central region by accessing dataset
    calc1 = avg_furniture_sales_central(data)
    # Calculates percentage of binders in California by accessing dataset 
    calc2 = percent_binders_in_california(data)
   
    # Writes both results to text file 
    write_results(calc1, calc2, 'results.txt')

    print('Results written to results.txt!')


# Test Cases
class Test_Project_Code(unittest.TestCase):
    def setUp(self):
        self.sample_data = [
            {'Category': 'Furniture', 'Region': 'Central', 'Sales': 100},
            {'Category': 'Furniture', 'Region': 'Central', 'Sales': 200},
            {'Category': 'Furniture', 'Region': 'West', 'Sales': 500},
            {'Category': 'Office Supplies', 'Region': 'Central', 'Sales': 0.0},
            {'Category': 'Furniture', 'Region': 'Central', 'Sales': None}
    ]


    def test_avg_furniture_central_1(self):
        result = avg_furniture_sales_central(self.sample_data)
        expected = 150.0
        self.assertEqual(result, expected)


    def test_avg_funiture_central_2(self):
        data = [
            {'Category': 'Furniture', 'Region': 'Central', 'Sales': 300},
            {'Category': 'Technology', 'Region': 'Central', 'Sales': 400}
        ]
        result = avg_furniture_sales_central(data)
        expected = 300.0
        self.assertEqual(result, expected)


    def test_avg_furniture_central_3(self):
        data = [
            {'Category': 'Office Supplies', 'Region': 'Central', 'Sales': 100},
            {'Category': 'Furniture', 'Region': 'West', 'Sales': 200}
        ]
        result = avg_furniture_sales_central(data)
        expected = 0.0
        self.assertEqual(result, expected)


    def test_avg_furniture_central_4(self):
        result = avg_furniture_sales_central([])
        expected = 0.0
        self.assertEqual(result, expected)


    def test_percent_binders_in_california_1(self):
        data = [
            {'State': 'California', 'Category': 'Office Supplies', 'Sub-Category': 'Binders'},
            {'State': 'California', 'Category': 'Office Supplies', 'Sub-Category': 'Paper'},
            {'State': 'California', 'Category': 'Office Supplies', 'Sub-Category': 'Binders'},
            {'State': 'California', 'Category': 'Office Supplies', 'Sub-Category': 'Pens'}
        ]
        result = percent_binders_in_california(data)
        expected = 50.0
        self.assertEqual(result, expected)


    def test_percent_binders_in_california_2(self):
        data = [
            {'State': 'California', 'Category': 'Office Supplies', 'Sub-Category': 'Binders'},
            {'State': 'Texas', 'Category': 'Office Supplies', 'Sub-Category': 'Binders'},
            {'State': 'California', 'Category': 'Office Supplies', 'Sub-Category': 'Paper'}
        ]
        result = percent_binders_in_california(data)
        expected = 50.0
        self.assertEqual(result, expected)

    def test_percent_binders_in_california_3(self):
        data = [
            {'State': 'Texas', 'Category': 'Office Supplies', 'Sub-Category': 'Binders'},
            {'State': 'California', 'Category': 'Furniture', 'Sub-Category': 'Chairs'}
        ]
        result = percent_binders_in_california(data)
        expected = 0.0
        self.assertEqual(result, expected)

    def test_percent_binders_in_california_4(self):
        data = [
            {'State': 'California', 'Category': 'Office Supplies', 'Sub-Category': 'Binders'},
            {'State': 'California', 'Category': 'Office Supplies', 'Sub-Category': 'Binders'} 
        ]
        result = percent_binders_in_california(data)
        expected = 100.0
        self.assertEqual(result, expected)

if __name__ == '__main__':
    main()
    unittest.main()
