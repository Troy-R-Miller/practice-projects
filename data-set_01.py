#Extract raw data from data-set.txt -> convert to integers
import re
datafile = input("Enter a file name: ")
if len(datafile) < 1:
    datafile = ("data-set.txt")

try:
    dfile = open(datafile)
except:
    print("file not found")
    exit()

#Create list to store values
values = list()

#Extracting values from data-set.txt and adding to values list
for line in dfile:
    nums = re.findall('([0-9]+)', line) #extracting values for integer conversion from data-set.txt
    values = values + nums
print(values)

#Conversion and calculations of integers
total = 0
for numbers in values:
    total=total+int(numbers)
print("Total:" , total)





