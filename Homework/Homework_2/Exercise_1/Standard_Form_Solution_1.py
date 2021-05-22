# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# # Homework 2 (Vanderbei Exercise 1.1 : Standard Form)

# %%
import sys
get_ipython().system('{sys.executable} -m pip install pulp')


# %%
import pulp
from pulp import *


# %%
"""
The Steel Company Band and Coil Production Problem (Standard Form)

Author: Muntakim Rahman 2020
"""

# %% [markdown]
# ## Textbook Problem
#
# <img src = "Vanderbei_Exercise_1.1.JPG" alt = "Exercise 1.1 Problem Description" height = "400" width = "350"/>
# %% [markdown]
# ## Steel Company Band and Coil Production Problem
#
# \begin{align*}
#     {\rm Maximize} \hspace{3mm} 25 * bands + 30 * coils \\
#     {\rm Subject \hspace{1mm} to} \hspace{3mm} 140 * bands + 200 * coils = 40 * 200 * 140 \\
#                                 0 \leq bands \leq 6000 \\
#                                 0 \leq coils \leq 4000 \\
# \end{align*}
#
# ### Standard Inequality Form
#
# \begin{align*}
#     {\rm Maximize} \hspace{3mm} -25 * bands - 30 * coils \\
#     {\rm Subject \hspace{1mm} to} \hspace{3mm} -7 * bands - 10 * coils \leq -26000 \\
#                                 7 * bands + 10 * coils \leq 26000 \\
#                                 bands \geq 0 \\
#                                 coils \geq 0 \\
# \end{align*}

# %%
# Create a LP Maximization Problem.
LP_Prob_St = LpProblem('Steel_Company_Problem_St', LpMaximize)


# %%
# Create Prime Decision Variables.
bands__ = LpVariable(name = 'bands__', lowBound = 0)
coils__ = LpVariable(name = 'coils__', lowBound = 0)


# %%
# Add Objective Function to LP Problem.
LP_Prob_St += -25 * bands__ - 30 * coils__

# Now Add Constraints.
LP_Prob_St += -7 * bands__ - 10 * coils__ <= -26000
LP_Prob_St += 7 * bands__ + 10 * coils__ <= 26000
LP_Prob_St += bands__ >= 0
LP_Prob_St += coils__ >= 0


# %%
# Write the LP Problem to a File.
LP_Prob_St.writeLP('SteelCompanyProblemStandardForm.lp')

# Display the LP Problem.
print(LP_Prob_St)


# %%
LP_Prob_St.solve()


# %%
print(f'Status: {LpStatus[LP_Prob_St.status]}\n')

decision_variables__ = {}
for variable in LP_Prob_St.variables() :
    print(f'{variable.name} = {variable.varValue}')
    decision_variables__[variable.name] = variable.varValue
if (LpStatus[LP_Prob_St.status] == 'Optimal') :
    print(f'Optimal Value : z = {value(LP_Prob_St.objective)}')
else :
    print(f'No Optimal Value. Status Code : {value(LP_Prob_St.objective)}')


# %%
print('Prime Decision Variables : ', str(decision_variables__))


# %%
bands = 6000 - decision_variables__['bands__']
coils = 4000 - decision_variables__['coils__']


# %%
print(f'Bands from Original Problem = {bands}')
print(f'Coils from Original Problem = {coils}')
