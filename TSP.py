# Sage code for Travelling Salesman Problem, gives the path and the total cost of travel
# The least cost must be unique, but there can be multiple valid paths

M = matrix([
 [0,10,25,25,10], 
 [1,0,10,15,2], 
 [8,9,0,20,10], 
 [14,10,24,0,15], 
 [10,8,25,27,0]
])
G=DiGraph(M,format='weighted_adjacency_matrix')
tsp = G.traveling_salesman_problem(use_edge_labels=True)
print sum(tsp.edge_labels())
show(tsp)


# for undirected:
M = matrix([
 [0,20,4,20,0], 
 [0,0,5,6,10], 
 [0,0,0,0,6], 
 [0,0,0,0,20], 
 [0,0,0,0,0]
 ]
);
for i in range(5):
    for j in range(i+1,5):
        if M[i,j] != 0:
            print "("+str(i)+","+str(j)+","+str(M[i,j])+"),", # copy this to the Graph()
G = Graph([(0,1,20), (0,2,4), (0,3,20), (1,2,5), (1,3,6), (1,4,10), (2,4,6), (3,4,20)])
tsp = G.traveling_salesman_problem(use_edge_labels=True)
show(tsp)
print sum(tsp.edge_labels())