#!/usr/bin/python3
import csv
import sys
import datetime

input_filename = sys.argv[1]
output_filename = sys.argv[2]

days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
key_list=[]
elements=[]
sum_dic = dict()

with open(input_filename, 'rt') as fp:
	reader = csv.reader(fp)
	for row in reader:
		#날짜 -> 요일 변환
		date = row[1].split('/')
		year = int(date[2])
		month = int(date[0])
		d = int(date[1])
		row[1] = days[datetime.date(year, month, d).weekday()]	
		
		key_list.append(row[0]+','+row[1])
		element = (row[0], row[1], row[2], row[3])
		elements.append(element)

key_list = set(key_list)
key_list = list(key_list)
print(len(key_list))

sum_dic = { int : 0 for int in key_list }
sum_vehicle = { int : 0 for int in key_list }
sum_trip = { int : 0 for int in key_list }

for i in range(len(elements)): 
	s = elements[i][0]+','+elements[i][1]
	for j in range(len(key_list)):
		if s == key_list[j]:
			sum_vehicle[key_list[j]] += int(elements[i][2])
			sum_trip[key_list[j]] += int(elements[i][3])
			sum_dic[key_list[j]] = str(sum_vehicle[key_list[j]])+','+str(sum_trip[key_list[j]]) 

with open(output_filename, 'wt') as fp:
	for i in range(len(key_list)):
		data = key_list[i] + ' ' + sum_dic[key_list[i]] +'\n'
		fp.write(data)
