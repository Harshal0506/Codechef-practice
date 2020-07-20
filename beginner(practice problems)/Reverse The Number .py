#https://www.codechef.com/problems/FLOW007
T=int(input())
for _ in range(T):
	i=list(input())
	i.reverse()
	print("".join(i).lstrip("0"))
