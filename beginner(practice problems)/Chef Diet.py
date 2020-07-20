#https://www.codechef.com/problems/DIET
T=int(input())
for _ in range(T):
	Total=0
	i=list(map(int,input().split()))
	L=list(map(int,input().split()))
	for z in range(i[0]):
		Total+=L[z]
		if Total<i[1]:
			print("NO {}".format(z+1))
			break
		Total-=i[1]
	else:
		print("YES")



		


