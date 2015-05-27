def simplex_twophase(am, rm, dm, avars, bvars, obj, neqns):
    vars = matrix(range(1,8)) # all variables
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
                    am[0] -= am[i]
                    rm[0] -= rm[i]
                else:
                    am[0] += am[i]
                    rm[0] += rm[i]
    print "Phase 1\\\\[5pt]" 
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
                    pr = i                 # pivot row
                
        if minrat == 999:
            print am[0]
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
    
    # Delete the artificial variable columns and replace with the objective function
    print "\\\\[5pt]\nPhase 2\\\\[10pt]"
    am = am.delete_columns([a-1 for a in avars])
    vars = vars.delete_columns([a-1 for a in avars])
    for i in range(am.ncols()):
        am[0,i] = obj[i]
    ncols = am.ncols()+4
    tbl = [[0]*ncols for i in range(100)]
    lst = [] # if 1,5,6 are BV and 3,4 are AV; after del AV, 1,3,4 are new BV. lst stores it after correcting the offset by 1.
    for i in bvars[1:]:
        dec = 0
        for j in avars:
            if i>j:
                dec += 1
        lst.append(i-dec-1)
    
    # Restore to proper form
    for i in range(1,neqns):
        for j in lst:
            if am[i,j] == 1 and am[0,j] != 0:
                rm[0] -= am[0,j]*rm[i]
                am[0] -= am[0,j]*am[i]
    head = ["\\text{BV}", "\\text{Eqn}", "Z"]
    for i in range(am.ncols()):
        if vars[0,i] in avars:
            head.append("\\overline{x}_{"+str(vars[0,i])+"}")
        else:
            head.append("x_{"+str(vars[0,i])+"}")
    head.append("\\text{RHS}\\\\ \\hline")             
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
                    pr = i                 # pivot row
                
        if minrat == 999:
            print am[0]
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
        bvars[pr] = vars[0,pc]
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
    
def simplex_ques(am, rm, avars, bvars, obj, neqns, n):
    flagge = 0
    am = matrix(obj).stack(am.delete_rows([0]))
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

var('z x1 x2 x3 x4 x5 x6 x7 M')
neqns = 4            # obj func and constraints
avars = [4]          # 4th variable is the artificial one
bvars = [-z,4,5,6]
obj = [-3,1,0,0,0,0] # This list contains the actual coefficients for maximization
am = matrix([
[0,0, 0, 1/1, 0, 0],
[2,1,-1, 1, 0,0],
[1,3,0,  0, 1, 0],
[0,1,0,0,0,1]
])
rm = matrix([
[0],
[2],
[2],
[4]
])
dm = matrix([
[0,1],
[1,0],
[2,0],
[3,0]
])
simplex_ques(copy(am), copy(rm),copy(avars),copy(bvars),copy(obj), neqns,2)        
simplex_twophase(copy(am), copy(rm),copy(dm),copy(avars),copy(bvars),copy(obj),copy(neqns))