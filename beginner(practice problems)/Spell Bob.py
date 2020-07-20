# cook your dish here
def foo (upper,lower):
    for i in [upper[0],lower[0]]:
        for j in [upper[1],lower[1]]:
            for k in [upper[2],lower[2]]:
                if [i,j,k].count('b')==2 and set([i,j,k])=={'b','o'}:
                        
                        print('yes')
                        return
                        
                        
                        
    else:
        print('no')

T=int(input())
for _ in range(T):
    upper=list(input())
    lower=list(input())
    foo(upper,lower)
    
                        