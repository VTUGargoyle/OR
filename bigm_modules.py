def simplex_ques(am, rm, avars, bvars, neqns, n):
    flagge = 0
    theqn = "Maximize\n\\begin{align*}\n"
    theqn += "Z &= "
    for j in range(n):
        if am[0,j] > 0:
            theqn += "-"+str(am[0,j])+"x_{"+str(j+1)+"}"
        if am[0,j] < 0:
            theqn += "+"+str(-am[0,j])+"x_{"+str(j+1)+"}"
    theqn += "\n\\end{align*}\nSubject to\n\\begin{align*}\n"            
    for i in range(1,neqns):
        for j in range(n):
            if am[i,j] < 0:
                theqn += "-"+str(-am[i,j])+"x_{"+str(j+1)+"}"
            if am[i,j] > 0:
                theqn += "+"+str(am[i,j])+"x_{"+str(j+1)+"}"
        for k in avars:
            if am[i,k-1] == 1:
                theqn += "& \\ge "+str(rm[i,0])+"\\\\\n"
                flagge = 1
                break
        if flagge == 0:
            theqn += "& \\le "+str(rm[i,0])+"\\\\\n"
        flagge = 0
    theqn += "\\end{align*}"
    print theqn    

def simplex_bigm(am, rm, avars, bvars, neqns):
    var('M z')
    assume(M>1000)
    vars = matrix(range(1,10)) # all variables
    dm = matrix([
    [0,1],
    [1,0],
    [2,0],
    [3,0]
    ])
    ncols = 4+am.ncols()
    head = ["\\text{BV}", "\\text{Eqn}", "Z"]
    for i in range(am.ncols()):
        if vars[0,i] in avars:
            head.append("\\overline{x}_{"+str(vars[0,i])+"}")
        else:
            head.append("x_{"+str(vars[0,i])+"}")
    head.append("\\text{RHS}\\\\ \\hline")        
    tbl = [[0]*ncols for i in range(100)]
    for i in range(1,neqns):
        if len(avars) == 0:
            break
        for j in avars:
            if am[i,j-1] > 0:
                if am[0,j-1] > 0:
                    am[0] -= M*am[i]
                    rm[0] -= M*rm[i]
                else:
                    am[0] += M*am[i]
                    rm[0] += M*rm[i]
    print "$\\begin{tabu}{|c|c|c|"+(ncols-4)*"c"+"|c|}\n\\hline"
    print " & & \multicolumn{"+str(am.ncols()+1)+"}{c|}{\\text{Coefficient of}} & \\\\"
    print ' & '.join(head)
    while min(am[0]) < 0:
        pc = list(am[0]).index(min(am[0])) # pivot column
        pr = 0
        minrat = 999
        least = 999
        for i in range(1,neqns):
            if am[i,pc] >0:
                minrat = rm[i]/am[i,pc]
                if minrat < least:
                    least = minrat
                    pr = i #pivot row
                
        if minrat == 999:
            print "no feasible solutions found"
            break
        tbvars = ["Z"]
        for ii in range(1,neqns):
            if bvars[ii] in avars:
                tbvars.append("\\overline{x}_"+str(bvars[ii]))
            else:
                tbvars.append("x_"+str(bvars[ii]))
        tmp = matrix(bvars).transpose().augment(dm[:neqns,:]).augment(am.augment(rm))
        for ii in range(neqns):
            for jj in range(ncols):
                tbl[ii][jj] = str(latex(tmp[ii,jj])) 
        tbl[pr][pc+3] = "$\\fbox{$"+str(latex(tmp[pr,pc+3]))+"$}$"              
        for ii in range(neqns):
            tbl[ii][0] = tbvars[ii]
            print ' & '.join(tbl[ii])+"\\\\"
        print "\\hline"      
        pn = am[pr,pc]
        am[pr] = am[pr]/pn
        rm[pr] /= pn
        for i in range(neqns):
            if i != pr:
                rm[i] -= am[i,pc]*rm[pr]
                am[i] -= am[i,pc]*am[pr]
        bvars[pr] = pc+1
    tbvars = ["Z"]
    for ii in range(1,neqns):
        if bvars[ii] in avars:
            tbvars.append("\\overline{x}_"+str(bvars[ii]))
        else:
            tbvars.append("x_"+str(bvars[ii]))   
    tmp = matrix(bvars).transpose().augment(dm[:neqns,:]).augment(am.augment(rm))
    for ii in range(neqns):
        for jj in range(ncols):
            tbl[ii][jj] = str(latex(tmp[ii,jj]))             
    for ii in range(neqns):
        tbl[ii][0] = tbvars[ii]
        print ' & '.join(tbl[ii])+"\\\\"
    print "\\hline \n\\end{tabu}$"    
    
var('z M')
neqns = 4          # obj func and constraints
avars = [4]        # 4th variable is the artificial one
bvars = [z, 4,5,6] # the basic variables
am = matrix([
[-7,-4, 0, M, 0, 0],
[-8,9,-1,1,0,0],
[3,2,0,0,1,0],
[3,8,0,0,0,1]
])
rm = matrix([
[0*M],
[8],
[7],
[2]
])
simplex_ques(copy(am), copy(rm), copy(avars), copy(bvars), neqns,2)
simplex_bigm(copy(am), copy(rm), copy(avars), copy(bvars), neqns)        
