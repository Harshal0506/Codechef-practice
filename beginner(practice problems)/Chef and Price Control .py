#https://www.codechef.com/problems/PRICECON
from numpy import array
T=int(input())
for _ in range(T):
	E,K=list(map(int,input().split()))


	A=array(list(map(int,input().split())))

	S=sum(A)
	A[A>K]=K
	AS=sum(A)
	print(S-AS)