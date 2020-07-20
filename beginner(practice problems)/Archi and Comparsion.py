


for _ in range( int(input())):
    
    a,b,n = input().split()
    a = int(a)
    b = int(b)
    n = int(n)
    
    if(a==b):
        print("0")
    
    elif a>= 0 and b>=0 :
        if(a>b):
            print("1")
        else:
            print("2")
    
    elif a>=0 and b<0:
        
        if(n%2==0):
            if(abs(b) > a):
                print("2")
            elif abs(b) == a:
                print("0")
            else:
                print("1")
            
        else:
            print("1")
    
    elif a < 0 and b >= 0:
        
        if( n%2==0 ):
            if( abs(a) > b):
                print("1")
            elif abs(a)==b:
                print("0")
            else:
                print("2")
        
        else:
            print("2")
                
                
    elif a<0 and b<0:
        
        if( n%2==0):
            if(abs(a) > abs(b)):
                print("1")
            elif(abs(a) == abs(b)):
                print("0")
            else:
                print("2")
        
        else:
            if(abs(a) > abs(b)):
                print("2")
            elif(abs(a)==abs(b)):
                print("0")
            else:
                print("1")