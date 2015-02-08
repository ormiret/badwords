#!/usr/bin/env python
#word compile and sort
#usage: mergelists.py firstlistfile secondlistfile
import sys

with open(sys.argv[1],'r') as f:
	first = f.readlines()

with open(sys.argv[2],'r') as f:
	second = f.readlines()

final_list = sorted(list(set(first) | set(second)))

new_file_name = sys.argv[1].replace('.txt','') + "-" + sys.argv[2].replace('.txt','') + ".txt"

with open(new_file_name,'w') as f:
	[f.write(x) for x in final_list]


