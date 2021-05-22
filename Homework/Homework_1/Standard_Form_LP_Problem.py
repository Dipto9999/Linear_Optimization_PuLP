# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# # Homework 1 (Question 1 : Standard Form)

# %%
import sys
get_ipython().system('{sys.executable} -m pip install pulp')


# %%
import pulp
from pulp import *


# %%
"""
Linear Programming Problem 1.0 (Standard Form)

Author : Muntakim Rahman 2021
"""

# %% [markdown]
# ## Linear Programming Problem 1.0
#
# \begin{align*}
#     {\rm Minimize} \hspace{5mm}
#         x_1 - 3x_2 - x_3 \\
#     {\rm Subject \hspace{1mm} to} \hspace{5mm}
#         x_1 + x_2 + x_3 = 3 \\
#         -x_1 + x_2 	\leq 1 \\
#         x_1 \geq 0 \\
#         x_2 {\hspace{1mm} unconstrained} \\
#         x_3 \geq 0 \\
# \end{align*}
#
# ### Standard Inequality Form
#
# \begin{align*}
#     {\rm Maximize} \hspace{5mm}
#         -x_1 + 3x_2^{+} - 3x_2^{-} + x_3 \\
#     {\rm Subject \hspace{1mm} to} \hspace{5mm}
#         x_1 + x_2^{+} - x_2^{-} + x_3 \leq 3 \\
#         -x_1 - x_2^{+} + x_2^{-} - x_3 \leq -3 \\
#         -x_1 + x_2^{+} - x_2^{-} \leq 1 \\
#         x_1, x_2^{+}, x_2^{-}, x_3 \geq 0 \\
# \end{align*}
# %% [markdown]
#

# %%
decision_variables__ = {}

decision_variables__['x_1'] = LpVariable(name = 'x_1', lowBound = 0, cat = LpContinuous)
decision_variables__['x_2_pos'] = LpVariable(name = 'x_2_pos', lowBound = 0, cat = LpContinuous)
decision_variables__['x_2_neg'] = LpVariable(name = 'x_2_neg', lowBound = 0, cat = LpContinuous)
decision_variables__['x_3'] = LpVariable(name = 'x_3', lowBound = 0, cat = LpContinuous)

## Print Decision Variables -> Mainly for Debugging Purposes.
print(decision_variables__)


# %%
LP_Prob_St = LpProblem(name = 'LP_Problem_1.0_Standard_Form', sense = LpMaximize)

# The Objective Function is Added to 'LP_Prob_St' First.
LP_Prob_St += - decision_variables__['x_1'] + 3 * decision_variables__['x_2_pos'] - 3 * decision_variables__['x_2_neg'] + decision_variables__['x_3']


# %%
# The Constraints are Added to 'LP_Prob_St'
LP_Prob_St += decision_variables__['x_1'] + decision_variables__['x_2_pos'] - decision_variables__['x_2_neg'] + decision_variables__['x_3'] <= 3
LP_Prob_St += - decision_variables__['x_1'] - decision_variables__['x_2_pos'] + decision_variables__['x_2_neg'] - decision_variables__['x_3'] <= -3
LP_Prob_St += - decision_variables__['x_1'] + decision_variables__['x_2_pos'] - decision_variables__['x_2_neg'] <= 1

LP_Prob_St += decision_variables__['x_1'] >= 0
LP_Prob_St += decision_variables__['x_2_pos'] >= 0
LP_Prob_St += decision_variables__['x_2_neg'] >= 0
LP_Prob_St += decision_variables__['x_3'] >= 0


# %%
print(LP_Prob_St)


# %%
LP_Prob_St.writeLP('LP_ProblemStandardForm.lp')


# %%
# The Problem is Solved Using PuLP's Choice of Solver.
LP_Prob_St.solve()


# %%
print(f'Status: {LpStatus[LP_Prob_St.status]} \n')

for variable in LP_Prob_St.variables() :
    print(f'{variable.name} = {variable.varValue}')
print('\n')

if (LpStatus[LP_Prob_St.status] == 'Optimal') :
    print(f'Optimal Value : Z = {value(LP_Prob_St.objective)}')
else :
    print(f'No Optimal Value. Status Code : {value(LP_Prob_St.objective)}')


# %%
# Values of original LP Variables are calculated.
x_1 = decision_variables__['x_1'].varValue
x_2 = decision_variables__['x_2_pos'].varValue - decision_variables__['x_2_neg'].varValue
x_3 = decision_variables__['x_3'].varValue


# %%
print(f'x_1 from Original Problem = {x_1}')
print(f'x_2 from Original Problem = {x_2}')
print(f'x_3 from Original Problem = {x_3}')
