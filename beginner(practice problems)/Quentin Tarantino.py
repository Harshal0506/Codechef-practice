import copy
T=int(input())
for _ in range(T):
    n=int(input())
    chapter=list(map(int,input().split()))
    possible=list(map(int,range(1,n+1)))
    
    
    
    
    if chapter!=possible and chapter.sort()==None and chapter==possible:
        print("yes")
    else:
        print('no')