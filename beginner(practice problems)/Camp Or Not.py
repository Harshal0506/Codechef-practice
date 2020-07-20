# cook your dish here
T=int(input())
for _ in range(T):
    D=int(input())
    Day_he_solved=[]
    problem_he_solved=[]
    for _ in range(D):
        d,p=list(map(int,input().split()))
        Day_he_solved.append(d)
        problem_he_solved.append(p)
    Q=int(input())
    
    for _ in range(Q):
        Total=0
        dead,req=list(map(int,input().split()))
        for i in range(len(Day_he_solved)):
            if Day_he_solved[i]>dead:
                continue
            else:
                Total+=problem_he_solved[i]
        if Total>=req:
            print("Go Camp")
        else:
            print("Go Sleep")
                
        