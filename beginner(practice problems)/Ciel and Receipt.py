#https://www.codechef.com/problems/CIELRCPT
menu=[2048,1024,512,256,128,64,32,16,8,4,2,1]
T=int(input())
for _ in range(T):
	i=int(input())
	c=0
	order=0
	while i!=0:
		order+=i//menu[c]

		i=i%menu[c]
		c+=1
	print(order)


