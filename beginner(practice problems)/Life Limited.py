T=int(input())
for _ in range(T):
    s1=list(input())
    s2=list(input())
    s3=list(input())
    for i in range(2):
        if s1[i]=="l":
            if s2[i]=="l" and s2[i+1]=="l":
                print("yes")
                break
        if s2[i]=="l":
            if s3[i]=="l" and s3[i+1]=="l":
                print("yes")
                break
    else:
        print("no")
