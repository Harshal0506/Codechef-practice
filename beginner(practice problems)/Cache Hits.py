#https://www.codechef.com/problems/CACHEHIT
T=int(input())
for _  in range(T):
	N,B,M=list(map(int,input().split()))
	M=list(map(int,input().split()))
	prev=-1
	count=0

	for i in M:
		c=i//B
		if c!=prev:
			count+=1
			prev=c
	print(count)

