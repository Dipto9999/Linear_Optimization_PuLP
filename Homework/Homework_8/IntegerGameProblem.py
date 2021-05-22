# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# # Homework 8 (Vanderbei Exercise 11.2)

# %%
import sys
get_ipython().system('{sys.executable} -m pip install pulp ')


# %%
import pulp
from pulp import *


# %%
"""
Integer Game Problem

Author: Muntakim Rahman 2021
"""

# %% [markdown]
# # Textbook Problem
#
# <img src = "Vanderbei_Exercise_11.2.JPG" alt = "Exercise 11.2 Problem Description" height = "300" width = "850"/>
# %% [markdown]
# # Integer Game Problem
#
# Let $1\leq i,j\leq 100$ denote the choices of $Player \hspace{1mm} A$ and $Player \hspace{1mm} B$ respectively.
#
# </br>
#
# Considering $Player \hspace{1mm} A$ to be the $Column$ player and $Player \hspace{1mm} B$ to be the $Row$ player :
#
# Let $P = a_{ij}$ represent the payoff matrix for $Player \hspace{1mm} A$.
#
# where
# \begin{align*}
#     a_{ij} =
#     \begin{cases}
#         0 \hspace{1mm} if \hspace{1mm} i = j \\
#         1 \hspace{1mm} if \hspace{1mm} i = j - 1 \\
#         -1 \hspace{1mm} if \hspace{1mm} i < j - 1 \\
#         -1 \hspace{1mm} if \hspace{1mm} i = j + 1 \\
#         1 \hspace{1mm} if \hspace{1mm} i > j + 1 \\
#     \end{cases}
# \end{align*}
#
# i.e.
# \begin{align*}
#     \begin{bmatrix}
#         \dots
#              & where \hspace{1mm} j = 1 & 2 & 3 & 4 & 5 & \dots & 96 & 97 & 98 & 99 & 100 \\
#             where \hspace{1mm} i = 1 &
#                                         0 & 1 & -1 & -1 & -1 & \dots & -1 & -1 & -1 & -1 & -1 \\
#                                    2 & -1 & 0 & 1 & -1 & -1 & \dots & -1 & -1 & -1 & -1 & -1 \\
#                                    3 & 1 & -1 & 0 & 1 & -1 & \dots & -1 & -1 & -1 & -1 & -1 \\
#                                    4 & 1 & 1 & -1 & 0 & 1 & \dots & -1 & -1 & -1 & -1 & -1 \\
#                                    5 & 1 & 1 & 1 & -1 & 0 & \dots & -1 & -1 & -1 & -1 & -1 \\ \dots \\
#                                   96 & 1 & 1 & 1 & 1 & 1 & \dots & 0 & 1 & -1 & -1 & -1 \\
#                                   97 & 1 & 1 & 1 & 1 & 1 & \dots & -1 & 0 & 1 & -1 & -1 \\
#                                   98 & 1 & 1 & 1 & 1 & 1 & \dots & 1 & -1 & 0 & 1 & -1 \\
#                                   99 & 1 & 1 & 1 & 1 & 1 & \dots & 1 & 1 & -1 & 0 & 1 \\
#                                   100 & 1 & 1 & 1 & 1 & 1 & \dots & 1 & 1 & 1 & -1 & 0 \\
#     \end{bmatrix}
# \end{align*}
#
# </br>
#
# Let $Player \hspace{1mm} A$'s strategy be given by the probability $x_{j}$, and optimal expected payoff be given by $E$ :
#
# ## Linear Programming Problem
#
# \begin{align*}
#     {\rm Maximize} \quad E \\
# \end{align*}
#
# \begin{align*}
#     {\rm Subject \hspace{1mm} to} \quad E -  \sum_{j = 1}^{100}a_{ij}*x_j \leq 0 \qquad i \leq 1 \hspace{1mm} \dots \hspace{1mm} 100 \\
#                                   \quad x_j \geq 0 \qquad j \leq 1 \hspace{1mm} \dots \hspace{1mm} 100 \\
#                                   \sum_{j = 1}^{100}x_j \geq 1 \\
# \end{align*}
#
#
#
#
#
#

# %%
MAX = 100
MIN = 1


# %%
strategy_probability = {}

for j in range(MIN, MAX + 1) :
    strategy_probability[j] = LpVariable(name = 'x_' + str(j), lowBound = 0, cat = LpContinuous)

optimal_expected_payoff = LpVariable(name = 'E', cat = LpContinuous)


# %%
LP_Prob = LpProblem(name = 'Integer_Game_Problem', sense = LpMaximize)

# The Objective Function is Added to 'LP_Prob' First.
LP_Prob += optimal_expected_payoff, 'Objective_Function'


# %%
# The Constraints are Added to 'LP_Prob'
for i in range (MIN, MAX + 1) :
    current_expected_payoff = 0
    for j in range(MIN, MAX + 1) :
        # a is Assigned based on the Following Cases.
        if (i == j) :
            a = 0
        elif (i == (j - 1) or i > (j + 1)) :
            a = 1
        elif (i == (j + 1) or i < (j - 1)) :
            a = -1
        current_expected_payoff += a*strategy_probability[j]

    LP_Prob += optimal_expected_payoff - lpSum(current_expected_payoff) <= 0, f'Payoff_Difference_{i}'
    LP_Prob += lpSum([strategy_probability[j] for j in range(MIN, MAX + 1)]) == 1, f'Probability_Simplex_{i}'
    LP_Prob += strategy_probability[i] >= 0, f'LowBound_{i}'


# %%
print(LP_Prob)


# %%
LP_Prob.writeLP('IntegerGameProblem.lp')


# %%
# The Problem is Solved Using PuLP's Choice of Solver.
LP_Prob.solve()


# %%
print(f'Status: {LpStatus[LP_Prob.status]} \n')

optimal_strategies = {}
for variable in LP_Prob.variables() :
    if (variable.name != 'E') :
        if (variable.varValue in optimal_strategies) :
            # If Expected Payoff is Already in Dictionary
            optimal_strategies[variable.varValue].append(variable.name)
        else :
            optimal_strategies[variable.varValue] = [variable.name]
if (LpStatus[LP_Prob.status] == 'Optimal') :
    print(f'Optimal Value : Z = {value(LP_Prob.objective)}')
else :
    print(f'No Optimal Value. Status Code : {value(LP_Prob.objective)}')


# %%
for expected_payoff, strategy in optimal_strategies.items() :
    print(f'Expected Payoff : {expected_payoff}\n')
    print(f'Strategies : \n{strategy}\n')
