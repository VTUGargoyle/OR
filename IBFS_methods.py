# Three methods for finding initial BFS:
# North-west corner rule, least cost and vogel's approximation method

def nwcr(cost, sup, dem):
    ncol = cost.ncols()
    nrow = cost.nrows()
    res = zero_matrix(nrow,ncol)
    i=j=0
    while true:
        res[i,j] = min(dem[0,j],sup[0,i])
        sup[0,i] -= res[i,j]
        dem[0,j] -= res[i,j]
        if sup[0,i] == 0:
            i += 1
        else:
            j += 1
        if i == nrow-1 and j == ncol-1:
            res[i,j] = max(dem[0,j],sup[0,i])
            break
    aa = vector(flatten(res.list()))
    bb = vector(flatten(cost.list()))
    print aa.dot_product(bb)            
    print res

def leastcost(cost, sup, dem):
    tot=sum(dem)
    ncol = cost.ncols()
    nrow = cost.nrows()
    res = zero_matrix(nrow,ncol)
    minn = 100
    vrows = range(nrow)
    vcols = range(ncol)
    imin = 10
    jmin = 10
    while true:
        for i in vrows:
            for j in vcols:
                if minn > cost[i,j]:
                    minn = cost[i,j]
                    imin = i
                    jmin = j
        res[imin,jmin] = min(sup[0,imin],dem[0,jmin])
        sup[0,imin] -= res[imin,jmin]
        dem[0,jmin] -= res[imin,jmin]
        if sup[0,imin] == 0:
            vrows.remove(imin)
        else:
            vcols.remove(jmin)
        if len(vrows) == 0:
            break
        minn = 100
    aa = vector(flatten(res.list()))
    bb = vector(flatten(cost.list()))
    print aa.dot_product(bb)        
    print res
        
def vogel(cost, sup, dem):
    tot=sum(dem)
    ncol = cost.ncols()
    nrow = cost.nrows()
    res = zero_matrix(nrow,ncol)
    
    vrows = range(nrow)
    vcols = range(ncol)
    
    while len(vrows) > 0 and len(vcols) > 0:
        minn = 100
        imin = 10
        jmin = 10
        
        curr = -1   # current row or current column used by looking at the max difference
        curc = -1
        
        rowd = []  # the row differences 
        cold = []  # the col diffs
    
        for i in vrows:
            lst = sorted(cost[i,vcols].list())
            if len(lst) > 1:
                cold.append(lst[1]-lst[0])
            else:
                cold.append(lst[0])
        for i in (vcols):
            lst = sorted(cost[vrows,i].list())
            if len(lst) > 1:
                rowd.append(lst[1]-lst[0])
            else:
                rowd.append(lst[0])
        if max(rowd) >= max(cold):
            curc = vcols[rowd.index(max(rowd))]
            curr = -1
        else:
            curr = vrows[cold.index(max(cold))]
            curc = -1
        if curr != -1:
            for j in vcols:
                if cost[curr,j] < minn:
                    minn = cost[curr,j]
                    jmin = j
                    imin = curr
        else:
            for i in vrows:
                if cost[i,curc] < minn:
                    minn = cost[i,curc]
                    imin = i
                    jmin = curc
        minsd = min(sup[0,imin], dem[0,jmin]) # minimum of supply and demand
        res[imin,jmin] = minsd
        sup[0,imin] -= minsd
        dem[0,jmin] -= minsd   
        if sup[0,imin] == 0:
            vrows.remove(imin)
        if dem[0,jmin] == 0:
            vcols.remove(jmin)    
    aa = vector(flatten(res.list()))
    bb = vector(flatten(cost.list()))
    print aa.dot_product(bb)
    print res    
    
cost = matrix([
[1,2,6],
[0,4,2],
[3,1,5]
])
sup = matrix([7,12,11])
dem = matrix([10,10,10])    
nwcr(copy(cost), copy(sup), copy(dem))
leastcost(copy(cost), copy(sup), copy(dem)) 
vogel(copy(cost), copy(sup), copy(dem)) 