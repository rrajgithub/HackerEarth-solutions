n=(int)(input())
while(n>0):
    n-=1
    n1=(list)(input())
    n2=n1[::-1]
    if(n1==n2):
        print("YES")
    else:
        print("NO")