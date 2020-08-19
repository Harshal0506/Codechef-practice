T=int(input())
for _ in range(T):
    Feedback=input()
    if "010" in Feedback or "101" in Feedback:
        print("Good")
    else:
        print("Bad")