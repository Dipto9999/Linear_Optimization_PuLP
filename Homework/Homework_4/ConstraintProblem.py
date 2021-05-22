# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# # Homework 4 (Question 2)

# %%
import sys
get_ipython().system('{sys.executable} -m pip install pulp')


# %%
import pulp
from pulp import *


# %%
"""
Constraint Problem

Author : Muntakim Rahman 2021
"""

# %% [markdown]
# ## Homework Problem
#
# Consider the $m\times n$-matrix $A$ and the vector $\vec b \in R^m$ that are given by
#
# \begin{align*}
#     A= [a_{ij}],
#     \qquad \vec b = [ b_i]
# \end{align*}
#
# where
#
# \begin{align*}
#     a_{ij} = (-2)^{i+j} (i^2 - j^2),
#     \qquad b_i = (-2)^i
#     \quad \hbox {for $i=1, \cdots m$ and $j=1, \cdots , n$.}
# \end{align*}
#
# Note that $a_{ij}$ is the entry of $A$ at the $i$-th row and the $j$-th column.
#
# Consider the following condition on vectors $\vec x \in R^n$:
#
# \begin{align*}
#     {\rm (Condition1)} &
#     \quad \quad A \vec x \le \vec b
#     \quad \&
#     \quad \vec x \ge \vec 0.
# \end{align*}
#
# Check whether there is a vector $\vec x \in R^n$ that satisfies (Condition1), when $m=n=10$, and when $m=n=20$.
# If the vector exists, solve for it.
# %% [markdown]
# ### Constraint Problem
#
# \begin{align*}
#     {\rm Maximize} \quad -w_o \\
#     {\rm Subject \hspace{1mm} to} \quad \quad A \vec x  + \vec w_o \le \vec b \\
#                                     \quad \vec x \ge \vec 0 \\
#                                     \quad \vec w_o \ge 0. \\
# \end{align*}
#
# <br/>
#
# \begin{align*}
#     {\rm Where}
#         \qquad A= [a_{ij}], \qquad \vec b = [ b_i], \\
#         \qquad a_{ij} = (-2)^{i+j} (i^2 - j^2), \\
#         \qquad b_i = (-2)^i, \\
#         \quad \hbox {$i=1, \cdots , m \qquad j=1, \cdots , n$.} \\ \\
#         \qquad \vec w_o = [{w_o}_i] \hspace{1mm} represents \hspace{1mm} auxiliary \hspace{1mm} variable. \\
# \end{align*}
# %% [markdown]
# ### Check if Constraint Satisfied When M = N = 10

# %%
M = 10
N = 10


# %%
A = [[(-2)**(i+j) * (i**2 - j**2) for j in range(1, N + 1)] for i in range(1, M + 1)]
b = [(-2)**i for i in range(1, M + 1)]


# %%
## Print Condition Variables -> Mainly for Debugging Purposes.
print('Matrix A')
for i in range(M) :
    print(A[i])

print('\n')

print('Vector b')
print(b)


# %%
decision_variables = []

for i in range(1, M + 1) :
    current_variable = LpVariable(name = 'x_' + str(i), lowBound = 0, cat = LpContinuous)
    decision_variables.append(current_variable)

## Print Decision Variables -> Mainly for Debugging Purposes.
print(decision_variables)

aux_variable = LpVariable(name = 'Auxiliary_Variable', lowBound = 0)


# %%
# Check if there is a feasible solution to the LP Problem by using Phase One of the Two Phase Simplex Method.
LP_Prob_Aux = LpProblem(name = 'Constraint_Problem', sense = LpMaximize)

# The Objective Function is Added to 'LP_Prob_Aux' First.
LP_Prob_Aux += - aux_variable, 'Auxiliary_Problem'


# %%
# The Constraints are Added to 'LP_Prob_Aux'
for i in range(M) :
    LP_Prob_Aux += lpSum([A[i][j] * decision_variables[j] for j in range(N)]) + aux_variable <= b[i], f'Constraint_{i + 1}'


# %%
print(LP_Prob_Aux)


# %%
LP_Prob_Aux.writeLP('ConstraintProblem_M_N_10.lp')


# %%
# The Problem is Solved Using PuLP's Choice of Solver.
LP_Prob_Aux.solve()


# %%
print(f'Status: {LpStatus[LP_Prob_Aux.status]} \n')

for variable in LP_Prob_Aux.variables() :
    print(f'{variable.name} = {variable.varValue}')
print('\n')

if (LpStatus[LP_Prob_Aux.status] == 'Optimal') :
    print(f'Optimal Value : Z = {value(LP_Prob_Aux.objective)}')
    if (value(LP_Prob_Aux.objective) == 0) :
        print ('The Original LP Problem is feasible.')
    else :
        print ('The Original LP Problem is not feasible.')
else :
    print(f'No Optimal Value. Status Code : {value(LP_Prob_Aux.objective)}')

# %% [markdown]
# ### Check if Constraint Satisfied When M = N = 20
#

# %%
M = 20
N = 20


# %%
A = [[(-2)**(i+j) * (i**2 - j**2) for j in range(1, N + 1)] for i in range(1, M + 1)]
b = [(-2)**i for i in range(1, M + 1)]


# %%
decision_variables = []

for i in range(1, M + 1) :
    current_variable = LpVariable(name = 'x_' + str(i), lowBound = 0, cat = LpContinuous)
    decision_variables.append(current_variable)

## Print Decision Variables -> Mainly for Debugging Purposes.
print(decision_variables)

aux_variable = LpVariable(name = 'Auxiliary_Variable', lowBound = 0)


# %%
# Check if there is a feasible solution to the LP Problem by using Phase One of the Two Phase Simplex Method.
LP_Prob_Aux = LpProblem(name = 'Constraint_Problem', sense = LpMaximize)

# The Objective Function is Added to 'LP_Prob_Aux' First.
LP_Prob_Aux += - aux_variable, 'Auxiliary_Problem'


# %%
# The Constraints are Added to 'LP_Prob_Aux'
for i in range(M) :
    LP_Prob_Aux += lpSum([A[i][j] * decision_variables[j] for j in range(N)]) + aux_variable <= b[i], f'Constraint_{i + 1}'


# %%
print(LP_Prob_Aux)


# %%
LP_Prob_Aux.writeLP('ConstraintProblem_M_N_20.lp')


# %%
# The Problem is Solved Using PuLP's Choice of Solver.
LP_Prob_Aux.solve()


# %%
print(f'Status: {LpStatus[LP_Prob_Aux.status]} \n')

for variable in LP_Prob_Aux.variables() :
    print(f'{variable.name} = {variable.varValue}')
print('\n')

if (LpStatus[LP_Prob_Aux.status] == 'Optimal') :
    print(f'Optimal Value : Z = {value(LP_Prob_Aux.objective)}')
    if (value(LP_Prob_Aux.objective) == 0) :
        print ('The Original LP Problem is feasible.')
    else :
        print ('The Original LP Problem is not feasible.')
else :
    print(f'No Optimal Value. Status Code : {value(LP_Prob_Aux.objective)}')
