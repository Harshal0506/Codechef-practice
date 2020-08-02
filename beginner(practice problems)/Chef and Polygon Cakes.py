import fractions

T=int(input())
for _ in range(T):
    N,A,K=list(map(int,input().split()))
    d=(360*(N-2)-2*A*N)/(N*(N-1))
    X=fractions.Fraction(A + (K - 1) * d).limit_denominator()
    print(X.numerator,X.denominator )
