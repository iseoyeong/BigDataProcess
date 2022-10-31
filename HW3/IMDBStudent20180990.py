#!/usr/bin/python3
import sys

input_filename = sys.argv[1] 
output_filename = sys.argv[2] 

genre_dic = dict()
genre_list = []

with open(input_filename, "rt") as fp:
	for line in fp:
		genre_list.extend(line.split('::')[2].strip('\n').split('|'))
	genre_dict = { int : 0 for int in genre_list }

genre_set = set(genre_list)

for i in genre_set:
	genre_dic[i] = genre_list.count(i)
print(genre_dic) 

with open(output_filename, "wt") as f:
	for key in genre_dic.keys():
		data = key + ' ' +  str(genre_dic[key]) + '\n'
		f.write(data)

