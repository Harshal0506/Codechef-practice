T=int(input())
for _ in range(T):
    N=int(input())
    words_occured={}
    Total=0
    for _ in range(N):
        Word=input()

        if Word not in words_occured:
            s=2
            for i in range(1,len(Word)):
                if Word[i-1] in "df" and Word[i] in "df":
                    s+=2
                if Word[i-1] in "jk" and Word[i] in "jk":
                    s+=2
                s+=2
            Total+=s
            words_occured[Word]=s



        else:
            Total+=words_occured[Word]/2
    print(int(Total))

