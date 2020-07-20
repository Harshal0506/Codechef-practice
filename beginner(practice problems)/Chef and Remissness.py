#https://www.codechef.com/problems/REMISS
T=int(input())
for _ in range(T):
	i=list(map(int,input().split()))
	print("{} {}".format(max(i),sum(i)))