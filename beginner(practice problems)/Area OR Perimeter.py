
L=int(input())
B=int(input())
Area=L*B
perimeter=2*(L+B)
if Area > perimeter:
    print("Area")
    print(Area)
elif Area == perimeter:
    print("Eq")
    print(Area)
else:
    print("Peri")
    print(perimeter)
    
    
