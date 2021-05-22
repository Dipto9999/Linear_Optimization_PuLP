# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# # Homework 1 (Question 1)

# %%
import sys
get_ipython().system('{sys.executable} -m pip install pulp')


# %%
import pulp
from pulp import *


# %%
"""
Linear Programming Problem 1.0

Author : Muntakim Rahman 2021
"""

# %% [markdown]
# ## Linear Programming Problem 1.0
#
# \begin{align*}
#     {\rm Minimize} \hspace{5mm} x_1 - 3x_2 - x_3 \\
#     {\rm Subject \hspace{1mm} to} \hspace{5mm} x_1 + x_2 + x_3 = 3 \\
#                                 -x_1 + x_2 	\leq 1 \\
#                                 x_1 \geq 0 \\
#                                 x_2 {\hspace{1mm} unconstrained} \\
#                                 x_3 \geq 0 \\
# \end{align*}

# %%
decision_variables = {}
for i in range(3) :
    decision_variables['x_' + str(i + 1)] = LpVariable(name = 'x_' + str(i + 1), cat = LpContinuous)

## Print Decision Variables -> Mainly for Debugging Purposes.
print(decision_variables)


# %%
LP_Prob = LpProblem(name = 'LP_Problem_1.0', sense = LpMinimize)

# The Objective Function is Added to 'LP_Prob' First.
LP_Prob += decision_variables['x_1'] - 3 * decision_variables['x_2'] - decision_variables['x_3']


# %%
# The Constraints are Added to 'LP_Prob'
LP_Prob += decision_variables['x_1'] + decision_variables['x_2'] + decision_variables['x_3'] == 3
LP_Prob += - decision_variables['x_1'] + decision_variables['x_2'] <= 1
LP_Prob += decision_variables['x_1'] >= 0
LP_Prob += decision_variables['x_3'] >= 0


# %%
print(LP_Prob)


# %%
LP_Prob.writeLP('LP_Problem.lp')


# %%
# The Problem is Solved Using PuLP's Choice of Solver.
LP_Prob.solve()


# %%
print(f'Status: {LpStatus[LP_Prob.status]} \n')

for variable in LP_Prob.variables() :
    print(f'{variable.name} = {variable.varValue}')
print('\n')

if (LpStatus[LP_Prob.status] == 'Optimal') :
    print(f'Optimal Value : Z = {value(LP_Prob.objective)}')
else :
    print(f'No Optimal Value. Status Code : {value(LP_Prob.objective)}')
