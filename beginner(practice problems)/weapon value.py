#https://www.codechef.com/problems/SC31
T=int(input())
for _ in range(T):
	N=int(input())
	F=[0]*10
	for _ in range(N):
		i=list(map(int,list(input())))
		for j in range(10):
			F[j]=F[j]^i[j]
	print(sum(F))
