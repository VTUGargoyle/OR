# Operations Research

All the python files are to be run on sagemath (http://www.sagemath.org/), which can be run on a linux or mac machine. 

1. `bigm_modules.py`: Given the input in matrix form (after inserting all the artificial and slack/surplus variables), solves using Big-M method and displays the iterations in LaTeX which can be directly copied to the LaTeX files. 

2. `twophase_modules.py`: Same as bigm, but gives the LaTeX output for two-phase method. 

3. `IBFS_methods.py`: Methods for obtaining initial basic feasible solutions for the transportation problem (NWCR, least cost and vogel's approximation methods)

4. `TP_optimal.c`: Implementation of algorithm for obtaining an optimal solution for transportation problem (currently uses only NWCR for the IBFS)

5. `TSP.py`: Solution to the travelling salesman problem, given the weighted adjacency matrix (uses functions provided by sage)
