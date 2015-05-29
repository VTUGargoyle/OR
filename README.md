# Operations Research

Note 1: All the python files are to be run on sagemath (http://www.sagemath.org/), which can be run on a linux or mac machine. 
Otherwise, create an account in https://cloud.sagemath.com , create a new worksheet (new -> sage worksheet), and then run the code. 

Note 2: Recently found out that sagemath actually contains some modules specifically to learn about simplex and graphical methods to solve LPP.
This is highly recommended: http://doc.sagemath.org/html/en/reference/numerical/sage/numerical/interactive_simplex_method.html

1. `bigm_modules.py`: Given the input in matrix form (after inserting all the artificial and slack/surplus variables), solves using Big-M method and displays the iterations in LaTeX which can be directly copied to the LaTeX files. 

2. `twophase_modules.py`: Same as bigm, but gives the LaTeX output for two-phase method. 

3. `IBFS_methods.py`: Methods for obtaining initial basic feasible solutions for the transportation problem (NWCR, least cost and vogel's approximation methods)

4. `TP_optimal.c`: Implementation of algorithm for obtaining an optimal solution for transportation problem (currently uses only NWCR for the IBFS)

5. `TSP.py`: Solution to the travelling salesman problem, given the weighted adjacency matrix (uses functions provided by sage)
