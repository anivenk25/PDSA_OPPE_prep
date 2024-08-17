def minmax(a, b):
    n = len (a)
    # Calculate initial max values
    max_a = max(a)
    max_b = max(b)
    if max_a > max_b : 
        flag = 1 
    else : 
        flag=0
    
    for i in range (n):
        if flag == 1 :
            if a[i]<b[i]:
                c= b[i]
                b[i]=a[i]
                a[i]=c
        if flag ==0 : 
            if a[i]>b[i]:
                c= b[i]
                b[i]=a[i]
                a[i]=c
    if flag ==1 : 
        b.sort() 
        return max(a)*max(b)
    else :
        a.sort() 
        return max(a)*max(b)
    
case=int(input())    
for i in range (case):
    n = int (input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(minmax(a,b))
