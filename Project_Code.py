# Name: Kristen May
# Student ID: 98342405
# Email: maykrist@umich.edu
# Collaborators: Carmela Taylor, Katia Hemphill
# Who Wrote What: 
# AI Usage:  

import csv
import unittest

def get_data(file):
    with open(file) as fn:
        csv_reader = csv.DictReader(fn)
        data = [row for row in csv_reader]
    return data 


def avg_furniture_sales_central(superstore_data):
    total = 0.0
    count = 0.0
    for row in superstore_data:
        if (
            row.get('Category') == 'Furniture'
            and row.get('Region') == 'Central'
            and row.get('Sales') not in (None, '')
        ):
            try:
                total += float(row['Sales'])
                count += 1
            except ValueError:
                continue

    if count == 0:
        return 0.0
    return total / count

def percent_binders_in_california(superstore_data):
    office_supplies_california = 0
    binders_california = 0

    for row in superstore_data:
        if (
            row.get('State') == 'California'
            and row.get('Category') == 'Office Supplies'
        ):
            office_supplies_california += 1
            if row.get('Sub-Category') == 'Binders':
                binders_california += 1

    if office_supplies_california == 0:
            return 0.0
        
    percentage_binders = (binders_california / office_supplies_california) * 100
    return percentage_binders


def write_results(calc1, calc2, filename):
    with open(filename, 'w') as file:
        file.write("Project 1 Results\n")
        file.write("Average Central Furniture Sales: $" + str(calc1) + "\n")
        file.write("Percent of Binders in California: " + str(calc2) + "%\n")

#Come back to this function
def main():
    data = get_data('SampleSuperstore.csv')
    
    calc1 = avg_furniture_sales_central(data)
    calc2 = percent_binders_in_california(data)

    write_results(calc1, calc2, 'results.txt')

    print('Results written to results.txt!')


# Test Cases
class Test_Project_Code(unittest.TestCase):
    def setUp(self):
        self.sample_data = [
            {'Category': 'Furniture', 'Region': 'Central', 'Sales': '100'},
            {'Category': 'Furniture', 'Region': 'Central', 'Sales': '200'},
            {'Category': 'Furniture', 'Region': 'West', 'Sales': '500'},
            {'Category': 'Office Supplies', 'Region': 'Central', 'Sales': ''},
            {'Category': 'Furniture', 'Region': 'Central', 'Sales': None}
    ]


    def test_avg_furniture_central_1(self):
        result = avg_furniture_sales_central(self.sample_data)
        expected = 150.0
        self.assertEqual(result, expected)


    def test_avg_funiture_central_2(self):
        data = [
            {'Category': 'Furniture', 'Region': 'Central', 'Sales': '300'},
            {'Category': 'Technology', 'Region': 'Central', 'Sales': '400'}
        ]
        result = avg_furniture_sales_central(data)
        expected = 300.0
        self.assertEqual(result, expected)


    def test_avg_furniture_central_3(self):
        data = [
            {'Category': 'Office Supplies', 'Region': 'Central', 'Sales': '100'},
            {'Category': 'Furniture', 'Region': 'West', 'Sales': '200'}
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
