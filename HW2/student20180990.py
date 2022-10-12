#!usr/bin/python3

import openpyxl

wb = openpyxl.load_workbook("student.xlsx")
ws = wb['sheet1']

total_dict = dict()
row_id = 1
for row in ws:
	if row_id != 1:
		total = ws.cell(row = row_id, column = 3).value * 0.3
		total += ws.cell(row = row_id, column = 4).value * 0.35
		total += ws.cell(row = row_id, column = 5).value * 0.34
		total += ws.cell(row = row_id, column = 6).value 	
		ws.cell(row = row_id, column = 7).value = total
		total_dict[row_id] = total
	#	print(total_dict)
	row_id += 1
wb.save("student.xlsx")

sorted_dict = sorted(total_dict.items(), key = lambda item: item[1], reverse=True)
print(sorted_dict)

print(len(sorted_dict))
