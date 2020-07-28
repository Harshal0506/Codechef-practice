from numpy import array
def check(A,B,C):
    if A==[0]*3 or B==[0]*3 or C==[0]*3:
        return 0

    else:
        if (all(item >= 0 for item in A) or all(item <= 0 for item in A) )and (all(item >= 0 for item in B) or all(item <= 0 for item in B) ) and (all(item >= 0 for item in C) or all(item <= 0 for item in C) ):
            return 1
        return 0

T=int(input())
for _ in range(T):
    mem1=array(list(map(int,input().split())))
    mem2 = array(list(map(int, input().split())))
    mem3 = array(list(map(int, input().split())))
    Diff1=list(mem1-mem2)
    Diff2=list(mem2-mem3)
    Diff3=list(mem3-mem1)
    if check(Diff1,Diff2,Diff3):
        print("yes")
    else:
        print("no")

