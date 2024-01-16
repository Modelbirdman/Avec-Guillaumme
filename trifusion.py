def trimerge(L):
    if len(L)==1:
        return L
    else:
        L1=trimerge(L[:len(L)//2])
        L2=trimerge(L[len(L)//2:])
        return merge(L1,L2)

def merge(L1,L2):
    i=0
    j=0
    res=[]
    while i<len(L1) and j<len(L2):
        if L1[i]>L2[j]:
            res.append(L2[j])
            j=j+1
        else:
            res.append(L1[i])
            i=i+1
    if i==len(L1):
        for k in range(j,len(L2)):
            res.append(L2[k])
    else:
        for k in range(i,len(L1)):
            res.append(L1[k])
    return res
    
