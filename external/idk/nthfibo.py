def findfibo(n,first=0,current=0,next=1):
    if(n == 0):
        return current
    first = current
    current = next
    next = first + current
    return findfibo(n-1,first,current,next)
n = 0
while(n != 67):
    n = int(input("enter term no. : "))
    result = findfibo(n)
    print(result)