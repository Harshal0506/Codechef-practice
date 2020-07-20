#https://www.codechef.com/problems/HRDSEQ
T=int(input())
for i in range(T):
	N=int(input())
	L=[]
	x=0
	for _ in range(N-1):
		if x not in L:
			L.append(x)
			x=0
		else:
			a=x
			L.reverse()
			x=(L.index(x)+1)
			L.reverse()
			L.append(a)
	print(L.count(x)+1)
			


