#!/usr/bin/python3

import sys
import datetime

input_filename = sys.argv[1]
output_filename = sys.argv[2]

days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
region=[]
vehicle=[]
trip=[]
day=[]

#파일 읽어오기
with open(input_filename, "rt") as fp:
	for line in fp:
		region.append(line.split(',')[0])
		vehicle.append(line.split(',')[2])
		trip.append(line.split(',')[3])
		
		#날짜 -> 요일 변환
		date = line.split(',')[1].split('/')
		year = int(date[2])
		month = int(date[0])
		d = int(date[1])
		day.append(days[datetime.date(year, month, d).weekday()])

#파일 쓰기
with open(output_filename, "wt") as f:
	for i in range(len(region)):
		data = region[i] + ',' + day[i] + ' ' + vehicle[i] + ',' + trip[i] 
		f.write(data)
