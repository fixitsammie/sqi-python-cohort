# with open('starter_file.txt', 'r') as file:
#     lines = file.readlines()    # Reads file into a list of lines
#     for i in lines:
#         print(i)

with open('machine-readable-business-employment-data-mar-2026-quarter.csv','r') as file:
    lines= file.readlines()
    print(lines[0])
    print(type(lines[0]))
    data = lines[1].split(',')[2]
    print(data)
    # for line in lines:
    #     print(line)
  


# import csv
# with open('machine-readable-business-employment-data-mar-2026-quarter.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row['Data_value'], row['Period'])




#print(row)
