#word compile and sort
#usage = word-merge.py firstlistfile secondlistfile
import sys

first = open(sys.argv[1],'r')
first_file = first.readlines()
first.close()

second = open(sys.argv[2],'r')
second_file = second.readlines()
second.close()

new_list = []

for x in first_file:
	if x not in new_list:
		new_list.append(x)

for x in second_file:
	if x not in new_list:
		new_list.append(x)

final_list = sorted(new_list)

new_file_name = sys.argv[1].replace('.txt','') + "-" + sys.argv[2].replace('.txt','') + ".txt"

new_list_file = open(new_file_name,'w')
for x in final_list:
	new_list_file.write(x)
new_list_file.close()
