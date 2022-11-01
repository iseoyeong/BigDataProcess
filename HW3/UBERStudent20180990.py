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

with open(input_filename, 'r', encoding = 'utf-8') as fp:
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

sum_dic = { int : 0 for int in key_list }
sum_vehicle = { int : 0 for int in key_list }
sum_trip = { int : 0 for int in key_list }

for i in range(len(elements)):
	s = elements[i][0]+','+elements[i][1]
	if s == key_list[i]:
		print(1)
		sum_vehicle[key_list[i]] += int(elements[i][2])
		sum_trip[key_list[i]] += int(elements[i][3])
		sum_dic[key_list[i]] = str(sum_vehicle[key_list[i]])+','+str(sum_trip[key_list[i]]) 

print(sum_dic)

with open(output_filename, 'w', encoding='utf-8') as fp:
	for i in range(len(key_list)):
		data = key_list[i] + ' ' + sum_dic[key_list[i]] +'\n'
		print(data)
		fp.write(data)
