index =0 
def z(n,r,c):
    global index
    if n == 1:
        if r == 0:
            index += c
        else:
            index += c+2
        return

    a = 2**(n-1)
    #1
    if r<a and c<a:
        z(n-1, r,c)
    #2
    elif r<a and c>=a:
        index += a*a
        z(n-1, r,c-a)
    #3
    elif r>=a and c<a:
        index += 2*a*a    
        z(n-1, r-a,c)
    #4
    else:
        index += 3*a*a    
        z(n-1, r-a,c-a)
        
n,r,c = map(int, input().split())
z(n,r,c)
print(index)