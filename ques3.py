"""
Question 3: Filtering and Creating a Subset CSV

You have a large customer database in a CSV file, and you need to extract only customers from a specific city.

Functional Requirement:
1. Create a CSV file named customers.csv with the following content:
Code snippet

customers.csv ( create a file with the below rows )

customer_id,name,email,city
C101,John Doe,john@example.com,New York
C102,Jane Smith,jane@example.com,Los Angeles
C103,Peter Jones,peter@example.com,New York
C104,Alice Brown,alice@example.com,Chicago
C105,Robert Green,robert@example.com,New York

2. Write a Python script to open customers.csv in read mode.

3. Filter the customers to only include those from "New York".

4. Write the filtered customer data into a new CSV file named new_york_customers.csv.

This new file should also include the header.

5. Print the content of new_york_customers.csv to confirm the filtering.
"""


import csv

header=["customer_id","name","email","city"]
data=[
    ["C101","John Doe","john@example.com","New York"],
    ["C102","Jane Smith","jane@example.com","Los Angeles"],
    ["C103","Peter Jones","peter@example.com","New York"],
    ["C104","Alice Brown","alice@example.com","Chicago"],
    ["C105","Robert Green","robert@example.com","New York"]
]

with open("customers.csv","w",newline='') as fobj:
    writer=csv.writer(fobj)
    writer.writerow(header)
    writer.writerows(data)


with open("customers.csv","r") as fobj:
    with open("new_york_customers.csv","w",newline="") as newobj:
        reader=csv.reader(fobj)
        writer=csv.writer(newobj)
        writer.writerow(header)
        for line in reader:                    
            if line[3]=="New York":          
                writer.writerow(line)      

with open("new_york_customers.csv","r") as newobj:
    reader=csv.reader(newobj)
    for line in reader:
        print(line)