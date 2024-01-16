
def tri_a_bulles(L):
    Lc=L.copy() # On évite de modifier la liste donnée en argument 
    triee=False 
    while not(triee):
        triee=True # On commence à remonter la liste et on la suppose alors triee 
        for i in range(len(Lc)-1):
            if Lc[i]>Lc[i+1]: # Lorsque la cellule n'est pas triée
                Lc[i],Lc[i+1]=Lc[i+1],Lc[i] 
                triee=False 
    return L
    


