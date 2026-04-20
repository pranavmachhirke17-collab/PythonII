import json
import csv


with open('C:\\Users\\DELL\\OneDrive\\Desktop\\Harshproject\\study\\sem 2\\UNIT-4\\data_new.json', 'r') as json_file:
        data = json.load(json_file)

with open('C:\\Users\\DELL\\OneDrive\\Desktop\\Harshproject\\study\\sem 2\\UNIT-4\\output.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['name', 'age', 'city'])
        for item in data:
            writer.writerow([item['name'], item['age'], item['city']])

print("Data has been successfully converted from JSON to CSV.")