# Since sage6.6, it provides with an interactive LPP module, which displays a neat graph and solve the given problem
# These are the graphs for problems 3.1 to 3.8 in the notes

# 3.1

A = ([2, 1],[1,2])
b = (72,48)
c = (8,6) # obj fn
P = InteractiveLPProblem(A, b, c, ["x1", "x2"], variable_type=">=")
show(P)
print P.optimal_solution(), P.optimal_value()
P.plot().save("/tmp/p3_1.svg")

# 3.2
ge = ">="
le = "<="
A = ([9,5],[7,9],[5,3],[7,9],[2,4])
b = (50,30,150,190,100)
c = (117,111) # obj fn
P = InteractiveLPProblem(A, b, c, ["x1", "x2"], variable_type=">=", constraint_type = [ge,ge,le,le,le])
show(P)
print P.optimal_solution(), P.optimal_value()
P.plot().save("/tmp/p3_2.svg")

# 3.3

A = ([1,1],[2,3])
b = (12,60)
c = (60,60) # obj fn
P = InteractiveLPProblem(A, b, c, ["x1", "x2"], variable_type=">=", constraint_type = [le,ge])
show(P)
print P.optimal_solution(), P.optimal_value()
P.plot().save("/tmp/p3_3.svg")

# 3.4

A = ([1,-1],[1,1])
b = (2,4)
c = (2,3) # obj fn
P = InteractiveLPProblem(A, b, c, ["x1", "x2"], variable_type=">=", constraint_type = [le,ge])
show(P)
print P.optimal_solution(), P.optimal_value()
P.plot().save("/tmp/p3_4.svg")

# 3.5

A = ([10,6],[1,2])
b = (60,10)
c = (15,9) # obj fn
P = InteractiveLPProblem(A, b, c, ["x1", "x2"], variable_type=">=", constraint_type = [le,le])
show(P)
print P.optimal_solution(), P.optimal_value()
P.plot().save("/tmp/p3_5.svg")

# 3.6

A = ([-1,1],[6,4],[1,0],[0,1],[0,1])
b = (1,24,5,4,2)
c = (1,-2) # obj fn
P = InteractiveLPProblem(A, b, c, ["x1", "x2"], variable_type=">=", constraint_type = [le,ge,le,le,ge])
show(P)
print P.optimal_solution(), P.optimal_value()
P.plot().save("/tmp/p3_6.svg")

# 3.7

A = ([-3,4],[2,-1],[2,3],[1,0],[0,1])
b = (12,-2,12,4,2)
c = (3,5) # obj fn
P = InteractiveLPProblem(A, b, c, ["x1", "x2"], variable_type=">=", constraint_type = [le,ge,ge,le,ge],problem_type="min")
show(P)
print P.optimal_solution(), P.optimal_value()
P.plot().save("/tmp/p3_7.svg")

# 3.8

A = ([1,3],[2,1],[1,0])
b = (15,10,4)
c = (3,2) # obj fn
P = InteractiveLPProblem(A, b, c, ["x1", "x2"], variable_type=">=", constraint_type = [le,le,le],problem_type="max")
show(P)
print P.optimal_solution(), P.optimal_value()
P.plot().save("/tmp/p3_8.svg")
