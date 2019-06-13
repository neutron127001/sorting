l=[14,33,27,35,10,100,10,0,4,5,6]
def bubblesort(n):
    while n>=0:
        for i in range(n):
            if l[i]<=l[(i+1)]:
                pass
            else:
                l[i],l[(i+1)]=l[(i+1)],l[i]
        n-=1
    return l
print(bubblesort((len(l))-1))
