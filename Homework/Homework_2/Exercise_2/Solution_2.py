# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# # Homework 2 (Vanderbei Exercise 1.2)

# %%
import sys
get_ipython().system('{sys.executable} -m pip install pulp ')


# %%
import pulp
from pulp import *


# %%
"""
The Airline Revenue Maximization Problem

Author: Muntakim Rahman 2020
"""

# %% [markdown]
# ## Textbook Problem
#
# <img src = "Vanderbei_Exercise_1.2.JPG" alt = "Exercise 1.2 Problem Description" height = "500" width = "400"/>
# %% [markdown]
# ### Airline Revenue Maximization Problem
#
# \begin{gather*}
#     {\rm Maximize} \hspace{5mm} \\
#         \begin{bmatrix}
#             300 \\
#             220 \\
#             100 \\
#         \end{bmatrix}
#
#         \begin{bmatrix}
#             I-N_{\hspace{1mm}Y} & I-N_{\hspace{1mm}B} & I-N_{\hspace{1mm}M}
#         \end{bmatrix}
#
#         +
#
#         \begin{bmatrix}
#             160 \\
#             130 \\
#             80 \\
#         \end{bmatrix}
#
#         \begin{bmatrix}
#             N-B_{\hspace{1mm}Y} & N-B_{\hspace{1mm}B} & N-B_{\hspace{1mm}M}
#         \end{bmatrix}
#
#         +
#
#         \begin{bmatrix}
#             360 \\
#             280 \\
#             140 \\
#         \end{bmatrix}
#
#         \begin{bmatrix}
#             I-B_{\hspace{1mm}Y} & I-B_{\hspace{1mm}B} & I-B_{\hspace{1mm}M}
#         \end{bmatrix}
#
#         \\
# \end{gather*}
#
# \begin{gather*}
#     {\rm Subject \hspace{1mm} to} \hspace{5mm} \\
#         \begin{bmatrix}
#             I-N_{\hspace{1mm}Y} & I-N_{\hspace{1mm}B} & I-N_{\hspace{1mm}M}
#         \end{bmatrix}
#
#         \leq
#
#         \begin{bmatrix}
#             4 & 8 & 22
#         \end{bmatrix}
#
#         \\
# \end{gather*}
#
# <br/>
#
# \begin{gather*}
#         \begin{bmatrix}
#             N-B_{\hspace{1mm}Y} & N-B_{\hspace{1mm}B} & N-B_{\hspace{1mm}M}
#         \end{bmatrix}
#
#         \leq
#
#         \begin{bmatrix}
#             8 & 13 & 20
#         \end{bmatrix}
#
#         \\
# \end{gather*}
#
# <br/>
#
# \begin{gather*}
#         \begin{bmatrix}
#             I-B_{\hspace{1mm}Y} & I-B_{\hspace{1mm}B} & I-B_{\hspace{1mm}M}
#         \end{bmatrix}
#
#         \leq
#
#         \begin{bmatrix}
#             3 & 10 & 18
#         \end{bmatrix}
#
#         \\
# \end{gather*}
#
# <br/>
#
# \begin{gather*}
#         \begin{bmatrix}
#             I-N_{\hspace{1mm}Y} & I-N_{\hspace{1mm}B} & I-N_{\hspace{1mm}M}
#         \end{bmatrix}
#
#         +
#
#         \begin{bmatrix}
#             I-B_{\hspace{1mm}Y} & I-B_{\hspace{1mm}B} & I-B_{\hspace{1mm}M}
#         \end{bmatrix}
#
#         \leq 30 \\
# \end{gather*}
#
# <br/>
#
# \begin{gather*}
#         \begin{bmatrix}
#             N-B_{\hspace{1mm}Y} & N-B_{\hspace{1mm}B} & N-B_{\hspace{1mm}M}
#         \end{bmatrix}
#
#         +
#
#         \begin{bmatrix}
#             I-B_{\hspace{1mm}Y} & I-B_{\hspace{1mm}B} & I-B_{\hspace{1mm}M}
#         \end{bmatrix}
#
#         \leq 30 \\
# \end{gather*}
#
# <br/>
#
# \begin{gather*}
#         \begin{bmatrix}
#             I-N_{\hspace{1mm}Y} & I-N_{\hspace{1mm}B} & I-N_{\hspace{1mm}M}
#         \end{bmatrix} ,
#
#         \quad
#
#         \begin{bmatrix}
#             N-B_{\hspace{1mm}Y} & N-B_{\hspace{1mm}B} & N-B_{\hspace{1mm}M}
#         \end{bmatrix},
#
#         \quad
#
#         \begin{bmatrix}
#             I-B_{\hspace{1mm}Y} & I-B_{\hspace{1mm}B} & I-B_{\hspace{1mm}M}
#         \end{bmatrix}
#
#         \quad
#
#         \geq
#
#         \begin{bmatrix}
#             0 & 0 & 0
#         \end{bmatrix}
#
#         \\
# \end{gather*}
#

# %%
# Creates Lists of the Fare-Class Combinations for each Origin/Destination.
labels_IN = ['Ithaca-Newark_Y', 'Ithaca-Newark_B', 'Ithaca-Newark_M']
labels_NB = ['Newark-Boston_Y', 'Newark-Boston_B', 'Newark-Boston_M']
labels_IB = ['Ithaca-Boston_Y', 'Ithaca-Boston_B', 'Ithaca-Boston_M']

# Creates Lists of the Ticket Prices for each Origin/Destination.
ticket_prices_IN = [300, 220, 100]
ticket_prices_NB = [160, 130, 80]
ticket_prices_IB = [360, 280, 140]

# Creates Lists of the Forecasted Demand Bounds for each Origin/Destination.
potential_customers_IN = [4, 8, 22]
potential_customers_NB = [8, 13, 20]
potential_customers_IB = [3, 10, 18]

# Initialize Variables for Constraints.
max_passengers = 30
number_of_origin_destination_combinations = 3


# %%
# Create the 'LP_Prob' Variable to Contain the Problem Data for the LP Maximization Problem.
LP_Prob = LpProblem("Ivy_Air_Problem", LpMaximize)


# %%
# Create Lists of Empty Strings to Contain the Referenced Variables.
tickets_IN = ['', '', '']
tickets_NB = ['', '', '']
tickets_IB = ['', '', '']

# Create Decision Variables.
for i in range(number_of_origin_destination_combinations) :
    tickets_IN[i] = LpVariable(name = str(labels_IN[i]), lowBound = 0, cat = 'Integer')
    tickets_NB[i] = LpVariable(name = str(labels_NB[i]), lowBound = 0, cat = 'Integer')
    tickets_IB[i] = LpVariable(name = str(labels_IB[i]), lowBound = 0, cat = 'Integer')


# %%
## Print Lists of Different Tickets -> Mainly for Debugging Purposes.
print(tickets_IN)
print(tickets_NB)
print(tickets_IB)


# %%
Prob_IN = lpSum([ticket_prices_IN[i] * tickets_IN[i] for i in range(number_of_origin_destination_combinations)])
Prob_NB = lpSum([ticket_prices_NB[i] * tickets_NB[i] for i in range(number_of_origin_destination_combinations)])
Prob_IB = lpSum([ticket_prices_IB[i] * tickets_IB[i] for i in range(number_of_origin_destination_combinations)])

## Print Lists of Different Tickets -> Mainly for Debugging Purposes.
print(f'Objective Function Coefficients for IN : {Prob_IN}')
print(f'Objective Function Coefficients for NB : {Prob_NB}')
print(f'Objective Function Coefficients for IB : {Prob_IB}')

# The Objective Function is Added to 'LP_Prob' First.
LP_Prob += Prob_IN + Prob_NB + Prob_IB, 'Total_Revenue_of_Ivy_Air'


# %%
passengers_IN = lpSum([tickets_IN[i] for i in range(number_of_origin_destination_combinations)])
passengers_IB = lpSum([tickets_IB[i] for i in range(number_of_origin_destination_combinations)])
passengers_NB = lpSum([tickets_NB[i] for i in range(number_of_origin_destination_combinations)])

# The Constraints are Added to 'LP_Prob'
LP_Prob += passengers_IN + passengers_IB <= max_passengers, 'Seating_Limit_1'
LP_Prob += passengers_NB + passengers_IB <= max_passengers, 'Seating_Limit_2'

customers_constraint = '_Potential_Customers'
for i in range(number_of_origin_destination_combinations) :
    LP_Prob += tickets_IN[i] <= potential_customers_IN[i], str(labels_IN[i]) + customers_constraint
    LP_Prob += tickets_NB[i] <= potential_customers_NB[i], str(labels_NB[i]) + customers_constraint
    LP_Prob += tickets_IB[i] <= potential_customers_IB[i], str(labels_IB[i]) + customers_constraint


# %%
print(LP_Prob)


# %%
LP_Prob.writeLP('IvyAirModel.lp')


# %%
# The Problem is Solved Using PuLP's Choice of Solver.
LP_Prob.solve()


# %%
current_flight_classes = 0

print(f'Status: {LpStatus[LP_Prob.status]} \n')

for variable in LP_Prob.variables() :
    print(f'{variable.name} = {variable.varValue}')

    current_flight_classes += 1
    if (current_flight_classes == len(labels_IN)) :
        current_flight_classes = 0
        print('\n')
if (LpStatus[LP_Prob.status] == 'Optimal') :
    print(f'Optimal Value : Z = {value(LP_Prob.objective)}')
else :
    print(f'No Optimal Value. Status Code : {value(LP_Prob.objective)}')
