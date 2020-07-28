T=int(input())
for _ in range(T):
    practical_obs=[0]
    hardness,carbon,tensile=list(map(int,input().split()))
    if hardness>50:
        practical_obs.append(1)
    else:
        practical_obs.append(0)
    if carbon<0.7:
        practical_obs.append(1)
    else:
        practical_obs.append(0)
    if tensile>5600:
        practical_obs.append(1)
    else:
        practical_obs.append(0)

    if sum(practical_obs)==3:
        print(10)
    elif sum(practical_obs)==0:
        print(5)
    elif sum(practical_obs)==1:
        print(6)
    elif practical_obs[1] and practical_obs[2]:
        print(9)
    elif practical_obs[2] and practical_obs[3]:
        print(8)
    else:
        print(7)