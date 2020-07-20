#https://www.codechef.com/problems/CNDLOVE
T=int(input())
for _ in range(T):
	input()
	i=sum(list(map(int,input().split())))
	if i%2:
		print("YES")
	else:
		print("NO")
