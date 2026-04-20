import csv
row_count = 0

with open("C:\\Users\\DELL\\OneDrive\\Desktop\\Harshproject\\study\\sem 2\\data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        row_count += 1
        print(row)
print(f"Total rows: {row_count}")