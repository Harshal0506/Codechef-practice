t=int(input())
for i in range(t):
  a,b=map(int,input().split())
  c=str(a+b)
  s=0
  for j in range(len(c)):
    if c[j]=="1":
      s+=2
    elif c[j]=="7":
      s+=3
    elif c[j]=="4":
      s+=4
    elif c[j]=="2" or c[j]=="5" or c[j]=="3":
      s+=5
    elif c[j]=="0" or c[j]=="6" or c[j]=="9":
      s+=6
    else:
      s+=7
  print(s)