#https://www.codechef.com/problems/CMPRSS
T=int(input())

for i in range(T):
	input()
	L=list(map(int,input().split()))
	L.insert(0,-1)
	L.append(-1)
	L.append(-1)
	final = ""

	prev=L[0]
	curr=L[1]
	Next=L[2]
	count=3
	flag=0
	while(curr!=-1):
		if(prev!=curr-1):
			final+=",{}".format(curr)
		else:
			if Next!=curr+1 and flag==0:
				final+=",{}".format(curr)
			elif Next!=curr+1 and flag==1:
				final+="...{}".format(curr)
				flag=0
			else:
				flag=1

		prev=curr
		curr=Next
		Next=L[count]
		count+=1
		if curr==-1 and flag==1:
			final+=",{}".format(curr)
	print(final[1:])
