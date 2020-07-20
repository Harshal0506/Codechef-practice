
#https://www.codechef.com/problems/XYSTR
import re
T=int(input())
for i in range(T):
	s=len(re.findall(r"(xy|yx)",input()))
	print(s)
	
