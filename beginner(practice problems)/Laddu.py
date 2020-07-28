t=int(input())
for j in range(0,t):
	list1=list(input().split())
	ladoo=0
	for i in range(0,int(list1[0])):
		list2=list(input().split())
		if list2[0]== 'CONTEST_WON':
			if int(list2[1]) <20:
					ladoo=ladoo + 300 + (20-int(list2[1]))
			else:
				ladoo=ladoo+300
		elif list2[0]== 'TOP_CONTRIBUTOR':
			ladoo=ladoo+300
		elif list2[0]== 'BUG_FOUND':
			ladoo=ladoo+ int(list2[1])
		else:
			ladoo=ladoo +50

	if list1[1] == 'INDIAN':
		print(ladoo//200)
	else:
		print(ladoo//400)
