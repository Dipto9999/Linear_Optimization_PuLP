# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# # Homework 2 (Vanderbei Exercise 1.1)

# %%
import sys
get_ipython().system('{sys.executable} -m pip install pulp ')


# %%
import pulp
from pulp import *


# %%
"""
The Steel Company Band and Coil Production Problem

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

# %%



# %%
# Create a LP Maximization Problem.
LP_Prob = LpProblem('Steel_Company_Problem', LpMaximize)


# %%
# Create Decision Variables.
bands = pulp.LpVariable(name = 'bands', lowBound = 0, upBound = 6000)
coils = pulp.LpVariable(name = 'coils', lowBound = 0, upBound = 4000)


# %%
# Add Objective Function to LP Problem.
LP_Prob += 25 * bands + 30 * coils, 'Total_Profit'

# Now Add Constraints.
LP_Prob += 140 * bands + 200 * coils == 40 * 200 * 140
LP_Prob += bands <= 6000, 'Upper_Limit_Bands'
LP_Prob += coils <= 4000, 'Upper_Limit_Coils'


# %%
# Write the LP Problem to a File.
LP_Prob.writeLP('SteelCompanyProblem.lp')

# Display the LP Problem.
print(LP_Prob)


# %%
LP_Prob.solve()


# %%
print(f'Status: {LpStatus[LP_Prob.status]}\n')

for variable in LP_Prob.variables() :
    print(f'{variable.name} =  {variable.varValue}')
if (LpStatus[LP_Prob.status] == 'Optimal') :
    print(f'Optimal Value : Z = {value(LP_Prob.objective)}')
else :
    print(f'No Optimal Value. Status Code : {value(LP_Prob.objective)}')
