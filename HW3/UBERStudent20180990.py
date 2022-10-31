#!/usr/bin/python3
import csv
import sys
import datetime

input_filename = sys.argv[1]
output_filename = sys.argv[2]

days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
region=[]
vehicle=[]
trip=[]
day=[]

with open(input_filename, 'r', encoding = 'utf-8') as fp:
	reader = csv.reader(fp)
	for row in reader:
		date = row[1].split('/')
		year = int(date[2])
		month = int(date[0])
		d = int(date[1])
		row[1] = days[datetime.date(year, month, d).weekday()]	
		region.append(row[0])	
		day.append(row[1])
		vehicle.append(row[2])
		trip.append(row[3])


with open(output_filename, 'w', encoding='utf-8') as fp:
	for i in range(len(region)):
		data = region[i] + ',' + day[i] + ' ' + vehicle[i] + ',' + trip[i] + '\n'
		fp.write(data)
