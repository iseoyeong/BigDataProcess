#!usr/bin/python3

import math
import openpyxl

#total 
wb = openpyxl.load_workbook("student.xlsx")
ws = wb['Sheet1']
total_dict = dict()

row_id = 1
for row in ws:
	if row_id != 1:
		total = ws.cell(row = row_id, column = 3).value * 0.3
		total += ws.cell(row = row_id, column = 4).value * 0.35
		total += ws.cell(row = row_id, column = 5).value * 0.34
		total += ws.cell(row = row_id, column = 6).value 	
		ws.cell(row = row_id, column = 7).value = total
		id = ws.cell(row = row_id, column = 1).value
		total_dict[row_id] = total
	row_id += 1

wb.save("student.xlsx")

#grade
#임의로 동점 데이터 만들기
total_dict[2] = 50
total_dict[3] = 50

len = len(total_dict) #학생 수 
#print('len: ' + str(len))
sorted_list = sorted(total_dict.items(), key = lambda item: item[1], reverse=True) #내림차순 정렬

key = [] #정렬된 순서대로 key list 저장
for i in range(len):
	key.append(sorted_list[i][0])

#등수 매기기
rank = dict()
for i in range(len): 
	if total_dict[key[i]] == total_dict[key[i-1]]: #동점인 경우
		rank[key[i]] = rank[key[i-1]]
	else:
		rank[key[i]] = i + 1
#print(rank)

#등급별 최대 등수
maxAA = int(len * 0.3 * 0.5)
maxA0 = int(len * 0.3)
maxBB =	int(maxA0 + (len * 0.7 - maxA0) * 0.5) 
maxB0 = int(len * 0.7)
maxCC =	int(maxB0 + (len - maxB0) * 0.5) 
maxC0 = len

#grade caculation
#아직 동점 고려x
grade_dict = dict()
for i in rank:
	if rank[i] <= maxAA: grade_dict[i] = 'A+'
	elif rank[i] <= maxA0: grade_dict[i] = 'A0'
	elif rank[i] <= maxBB: grade_dict[i] = 'B+'
	elif rank[i] <= maxB0: grade_dict[i] = 'B0'
	elif rank[i] <= maxCC: grade_dict[i] = 'C+'
	else: grade_dict[i] = 'C0'

print(grade_dict)
	 

