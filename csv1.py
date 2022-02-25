import csv#importing the csv 
f=open('student.csv','r')#opening the file open(file,mode)
data=csv.reader(f)#reading the csv file with reader() method 
print(data)
for s in data:
	print(s[])


