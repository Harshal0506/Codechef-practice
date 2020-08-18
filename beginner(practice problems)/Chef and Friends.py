N=int(input())
Count=0
for _ in range(N):
    F=input()
    if ('ch'in F)or('he'in F)or('ef'in F):
        Count+=1
print(Count)