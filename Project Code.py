# Name: Kristen May
# Student ID:
# Email: maykrist@umich.edu
# Collaborators: Carmela Taylor, Katia Hemphill
# Who Wrote What:
# AI Usage: 

import csv 

def read_csv(filename):
    superstore_data = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            superstore_data.append(row)
    return superstore_data 

def avg_furniture_sales_central(superstore_data):
    central_furniture = []
    for row in superstore_data:
        if row['Category'] == 'Furniture' and row['Region'] == 'Central':
            central_furniture.append(row)

    total = 0
    for row in central_furniture:
        total += float(row['Sales'])

    if len(central_furniture) == 0:
        return 0
        
    average = total / len(central_furniture)
    return average

def percent_binders_in_california(superstore_data):
    office_supplies_california = 0
    binders_california = 0

    for row in superstore_data:
        if row['State'] == 'California' and row['Category'] == 'Office Supplies':
            office_supplies_california += 1
            if row['Sub-Category'] == 'Binders':
                binders_california += 1

    if office_supplies_california == 0:
            return 0
        
    percentage_binders = (binders_california / office_supplies_california) * 100
    return percentage_binders

data = read_csv('SampleSuperstore.csv')
result = percent_binders_in_california(data)
print(f"Percentage of office supplies in CA that are binders: {result:.2f}%")


def write_results(results, filename):
    with open(filename, 'w') as file:
        file.write("Project 1 Results\n")

        # Used Claude for this, I'm very confused 
        file.write(f"Average Central Furniture Sales: ${results['calc1']:.2f}\n")
        file.write(f"Percent of California Office Supplies that are Binders: {results[calc2]:.2f}%\n")

#Come back to this function
#def main():
 #   data = read_csv('SampleSuperstore.csv')

  #  calc1 = avg_furniture_sales_central(data)
   # print(f"Result: ${calc1:.2f}\n")


#    calc2 = percent_binders_in_california(data)
 #   print(f"Results: {calc2:.2f}%\n")
    
    #This line wrong 
  #  write_results_to_file(calc1, calc2, 'results.txt')

#main()