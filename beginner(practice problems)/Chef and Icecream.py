#https://www.codechef.com/problems/CHFICRM
final=[]
Testcases=int(input())
for i in range(Testcases):
	n5 = 0
	n10 = 0
	n15 = 0
	int(input())
	Customers=list(map(int,input().split()))
	for i in Customers:
		if i==5:
			n5+=1
		elif i==10:
			if n5>0:
				n5-=1
				n10+=1
			else:
				final.append("NO")
				break
		else:
			if n10>0:
				n10-=1
				n15+=1
			elif n5>1:
				n5-=2
				n15+=1
			else:
				final.append("NO")
				break
	else:
		final.append("YES")

for i in final:
	print(i)
