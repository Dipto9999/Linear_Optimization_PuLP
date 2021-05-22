# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# # Homework 9 (Question 2)

# %%
import sys
get_ipython().system('{sys.executable} -m pip install pulp ')


# %%
import pulp
from pulp import *


# %%
import csv


# %%
"""
Investment Portfolio Problem

Author : Muntakim Rahman 2021
"""

# %% [markdown]
# ## Textbook Problem
#
# <img src = "Homework_9_Question_2.JPG" alt = "Question 2 Problem Description" height = "400" width = "500"/>
# %% [markdown]
# ## Portfolio Selection
#
# Let $R_{j}(t)$ denote the return on investment $j$ over $T$ monthly periods.
#
# \begin{equation}
#     R = \sum_j x_j R_j \quad \dots (1)
# \end{equation}
#
# Calculate the expected return (i.e. reward) with the formula :
#
# \begin{equation}
#     ER = \sum_j x_j E R_j \quad \dots (2)
#         \quad From \hspace{1mm} (1) \\
# \end{equation}
#
# For our purposes, assume that $R_j(t)$ is a random variable where values $t = 1 \dots T$ are taken with equal probability.
#
# \begin{equation}
#     \begin{aligned}
#         ER_j  &= \frac{1}{T} \sum_{t=1}^T R_j(t) \quad \dots (3) \\
#     \end{aligned}
# \end{equation}
#
#
# Let the mean absolute deviation from the mean ($MAD$) represent the risk associated with a portfolio of investments.
#
# For our purposes, the ($MAD$) is calculated as :
#
# \begin{equation}
#     \begin{aligned}
#         E {\left\lvert{R-ER}\right\rvert} & = E \left\lvert{\sum_j x_j R_j - \sum_j x_j E R_j}\right\rvert
#                                             \quad From \hspace{1mm} (1) \hspace{1mm} \& \hspace{1mm} (2) \\
#                                           & = E \left\lvert{\sum_j x_j (R_j - E R_j)}\right\rvert \\
#                                           & = \frac{1}{T} \sum_{t=1}^T
#                                             \left\lvert{\sum_j x_j \bigg[
#                                                 R_j(t) - \frac{1}{T} \sum_{t=1}^T R_j(t)
#                                             \bigg]}\right\rvert \quad \dots (4) \quad From \hspace{1mm} (3) \\
#     \end{aligned}
# \end{equation}
#
# ### Linear Programming Problem
#
# The LP Problem takes the positive risk/return parameter $\mu$ into account to form a linear combination between the risk and reward, as shown below.
#
# \begin{align*}
#     \begin{aligned}
#         {\rm Maximize} & \quad \mu \hspace{1mm} ER - E {\left\lvert{R-ER}\right\rvert} \\
#                        & = \mu \hspace{1mm} \sum_j x_j E R_j - \frac{1}{T} \sum_{t=1}^T
#                             \left\lvert{\sum_j x_j \bigg[
#                                 R_j(t) - \frac{1}{T} \sum_{t=1}^T R_j(t)
#                             \bigg]}\right\rvert \quad From \hspace{1mm} (2) \hspace{1mm} \& \hspace{1mm} (4) \\
#                        & = \frac{\mu}{T} \hspace{1mm} \sum_{t=1}^T \sum_j x_j R_j(t)
#                             - \frac{1}{T} \sum_{t=1}^T
#                             \left\lvert{\sum_j x_j \bigg[
#                                 R_j(t) - \frac{1}{T} \sum_{t=1}^T R_j(t)
#                             \bigg]}\right\rvert \quad From \hspace{1mm} (3) \\
#                        & = \frac{\mu}{T} \hspace{1mm} \sum_{t=1}^T \sum_j x_j R_j(t)
#                             - \frac{1}{T} \sum_{t=1}^T y_t
#                             \qquad Where \hspace{1mm} y_t =
#                             \left\lvert{\sum_j x_j \bigg[
#                                 R_j(t) - \frac{1}{T} \sum_{t=1}^T R_j(t)
#                              \bigg]}\right\rvert \\
#     \end{aligned}
# \end{align*}
#
# \begin{align*}
#     {\rm Subject \hspace{1mm} to}
#         \quad -y_t \leq \sum_j x_j \bigg[ R_j(t) - \frac{1}{T} \sum_{t=1}^T R_j(t) \bigg] \leq y_t \\
#         Which \hspace{1mm} can \hspace{1mm} also \hspace{1mm} be \hspace{1mm} written \hspace{1mm} as : \\
#         y_t \geq +\sum_j x_j \bigg[ R_j(t) - \frac{1}{T} \sum_{t=1}^T R_j(t) \bigg],
#               \quad  y_t \geq -\sum_j x_j \bigg[ R_j(t) - \frac{1}{T} \sum_{t=1}^T R_j(t) \bigg] \\
#         x_j \geq 0 \quad j = 1 \dots n,
#             \quad y_t \geq 0 \quad t = 1 \dots T \\
#         \quad \sum_j x_j = 1, \\
# \end{align*}
#
#
# At high value, $\mu$ maximizes reward regardless of risk. At low values, risk is minimized.
# %% [markdown]
# ## Import Data From CSV File

# %%
dates = []
investments = ['VAB', 'VCN', 'VXC', 'VBAL']

prices = {}
for j in range(len(investments)) :
    prices[investments[j]] = {}

## Print Prices Dictionary -> Mainly for Debugging Purposes.
print(prices)


# %%
with open('HW9P2.csv') as historical_prices :
    csv_reader = csv.reader(historical_prices, delimiter = ',')
    line_count = 0
    column_names = []

    row_count = 0
    for row_contents in csv_reader :
        if (row_count == 0) :
            for column_contents in row_contents :
                column_names.append(str(column_contents))
        else :
            # Column Count should be Equal to Total Number of Investments.
            n = 0
            for column_contents in row_contents :
                if (n == 0) :
                    current_date = str(column_contents)
                    dates.append(current_date)
                else :
                    j = investments[n - 1]
                    prices[j][current_date] = float(column_contents)

                n += 1
        row_count += 1

    # Number of Monthly Intervals in Which Returns are Calculated.
    T = row_count - 2

## Print CSV File Data to Screen -> Mainly for Debugging Purposes.
print(f'Columns Are \n{column_names}\n\n')

print(f'Dates : \n{dates}\n')

print('Prices :')
for j, price in prices.items() :
    print(f'Investment : {j}')
    print(f'Price : \n{price}\n')

print(f'Calculated T Value : {T}\n')


# %%
# Calculate Monthly Returns
returns = {}

for j in investments :
    returns[j] = {}

    ## Print Returns Dictionary -> Mainly for Debugging Purposes.
    print(f'Returns Before Assignment : \n{returns}\n')

    for t in range(1, T + 1) :
        returns[j][t] = prices[j][dates[t]] / prices[j][(dates[t - 1])]

    ## Print Returns for Investment -> Mainly for Debugging Purposes.
    print(f'Returns for Investment {j} : \n{returns[j]}\n')


# %%
# Calculate Mean Monthly Returns
mean_returns = {}

for j in investments :

    mean_returns[j] = 0
    for t in range(1, T + 1) :
        mean_returns[j] += returns[j][t]
    mean_returns[j] /= T

    ## Print Mean Returns for Investment -> Mainly for Debugging Purposes.
    print(f'Mean Returns for Investment {j} : {mean_returns[j]}\n')

# %% [markdown]
# ## Solve LP Problem

# %%
LP_Prob = LpProblem(name = 'Investment_Portfolio_Problem', sense = LpMaximize)

decision_variables_investment = {}
for j in range(len(investments)) :
    decision_variables_investment[investments[j]] = LpVariable(name = 'x_' + str(investments[j]), lowBound = 0)

decision_variables_deviation = {}
for t in range(1, T + 1) :
    decision_variables_deviation[t] = LpVariable(name = 'y_' + str(t), lowBound = 0)

    LP_Prob += decision_variables_deviation[t] >= 0, f'Low_Bound_Deviation_{t}'

for j in investments :
    LP_Prob += decision_variables_investment[j] >= 0, f'Low_Bound_Investment_{j}'

# Print Decision Variables -> Mainly for Debugging Purposes.
print(f'Investment Decision Variables : {decision_variables_investment}')
print(f'Deviation Decision Variables : {decision_variables_deviation}')

# %% [markdown]
# ### Risk/Return Parameter of 1

# %%
mu = 1

expected_investment_returns = lpSum([mu * mean_returns[j] * decision_variables_investment[j] for j in investments])
monthly_deviation = lpSum([decision_variables_deviation[t] for t in range(1, T + 1)])/T

# The Objective Function is Added to 'LP_Prob' First.
LP_Prob += expected_investment_returns - monthly_deviation, 'Maximize_Portfolio_Returns'


# %%
# The Constraints are Added to 'LP_Prob'
for t in range(1, T + 1) :
    monthly_deviation = lpSum([(returns[j][t] - mean_returns[j]) * decision_variables_investment[j] for j in investments])
    LP_Prob += decision_variables_deviation[t] >= -monthly_deviation, f'Deviation_Investment_Negative_Relation_{t}'
    LP_Prob += decision_variables_deviation[t] >= monthly_deviation, f'Deviation_Investment_Positive_Relation_{t}'

LP_Prob += lpSum([decision_variables_investment[j] for j in investments]) == 1, 'Probability_Simplex'


# %%
print(LP_Prob)


# %%
LP_Prob.writeLP('OriginalPortfolioProblemParameter1.lp')


# %%
# The Problem is Solved Using PuLP's Choice of Solver.
LP_Prob.solve()


# %%
print(f'Status: {LpStatus[LP_Prob.status]} \n')

for j, decision_variable in decision_variables_investment.items() :
    print(f'{decision_variable.name} = {decision_variable.varValue}')
print('\n')

if (LpStatus[LP_Prob.status] == 'Optimal') :
    print(f'Optimal Value : Z = {value(LP_Prob.objective)}')
else :
    print(f'No Optimal Value. Status Code : {value(LP_Prob.objective)}')

# %% [markdown]
# ### Risk/Return Parameter of 0.5

# %%
mu = 0.5

expected_investment_returns = lpSum([mu * mean_returns[j] * decision_variables_investment[j] for j in investments])
monthly_deviation = lpSum([decision_variables_deviation[t] for t in range(1, T + 1)])/T

# The Objective Function is Added to 'LP_Prob' First.
LP_Prob += expected_investment_returns - monthly_deviation, 'Maximize_Portfolio_Returns'


# %%
print(LP_Prob)


# %%
LP_Prob.writeLP('OriginalPortfolioProblemParameter0.5.lp')


# %%
# The Problem is Solved Using PuLP's Choice of Solver.
LP_Prob.solve()


# %%
print(f'Status: {LpStatus[LP_Prob.status]} \n')

for j, decision_variable in decision_variables_investment.items() :
    print(f'{decision_variable.name} = {decision_variable.varValue}')
print('\n')

if (LpStatus[LP_Prob.status] == 'Optimal') :
    print(f'Optimal Value : Z = {value(LP_Prob.objective)}')
else :
    print(f'No Optimal Value. Status Code : {value(LP_Prob.objective)}')

# %% [markdown]
# ### Risk/Return Parameter of 0

# %%
mu = 0

expected_investment_returns = lpSum([mu * mean_returns[j] * decision_variables_investment[j] for j in investments])
monthly_deviation = lpSum([decision_variables_deviation[t] for t in range(1, T + 1)])/T

# The Objective Function is Added to 'LP_Prob' First.
LP_Prob += expected_investment_returns - monthly_deviation, 'Maximize_Portfolio_Returns'


# %%
print(LP_Prob)


# %%
LP_Prob.writeLP('OriginalPortfolioProblemParameter0.lp')


# %%
# The Problem is Solved Using PuLP's Choice of Solver.
LP_Prob.solve()


# %%
print(f'Status: {LpStatus[LP_Prob.status]} \n')

for j, decision_variable in decision_variables_investment.items() :
    print(f'{decision_variable.name} = {decision_variable.varValue}')
print('\n')

if (LpStatus[LP_Prob.status] == 'Optimal') :
    print(f'Optimal Value : Z = {value(LP_Prob.objective)}')
else :
    print(f'No Optimal Value. Status Code : {value(LP_Prob.objective)}')

# %% [markdown]
# ## Change Portfolio Composition (Upper Limit 90% Stocks, 80% Canada)
# %% [markdown]
# ### Risk/Return Parameter of 1

# %%
mu = 1

expected_investment_returns = lpSum([mu * mean_returns[j] * decision_variables_investment[j] for j in investments])
monthly_deviation = lpSum([decision_variables_deviation[t] for t in range(1, T + 1)])/T

# The Objective Function is Added to 'LP_Prob' First.
LP_Prob += expected_investment_returns - monthly_deviation, 'Maximize_Portfolio_Returns'


# %%
stocks = {'VCN' : 1, 'VXC' : 1, 'VBAL' : 0.6}
canada_investments = {'VAB' : 1, 'VCN' : 1, 'VBAL' : 0.3}

# The New Constraints are Added to 'LP_Prob'
LP_Prob += lpSum([(percent * decision_variables_investment[stock]) for stock, percent in stocks.items()]) <= 0.9, 'Stocks_Limit'

LP_Prob += lpSum([(percent * decision_variables_investment[investment]) for investment, percent in canada_investments.items()]) <= 0.8, 'Canada_Limit'


# %%
print(LP_Prob)


# %%
LP_Prob.writeLP('NewPortfolioProblemParameter1.lp')


# %%
# The Problem is Solved Using PuLP's Choice of Solver.
LP_Prob.solve()


# %%
print(f'Status: {LpStatus[LP_Prob.status]} \n')

for j, decision_variable in decision_variables_investment.items() :
    print(f'{decision_variable.name} = {decision_variable.varValue}')
print('\n')

if (LpStatus[LP_Prob.status] == 'Optimal') :
    print(f'Optimal Value : Z = {value(LP_Prob.objective)}')
else :
    print(f'No Optimal Value. Status Code : {value(LP_Prob.objective)}')

# %% [markdown]
# ### Risk/Return Parameter of 0.5

# %%
mu = 0.5

# The Objective Function is Added to 'LP_Prob' First.
LP_Prob += mu*expected_investment_returns - monthly_deviation, 'Maximize_Portfolio_Returns'


# %%
print(LP_Prob)


# %%
LP_Prob.writeLP('NewPortfolioProblemParameter0.5.lp')


# %%
# The Problem is Solved Using PuLP's Choice of Solver.
LP_Prob.solve()


# %%
print(f'Status: {LpStatus[LP_Prob.status]} \n')

for j, decision_variable in decision_variables_investment.items() :
    print(f'{decision_variable.name} = {decision_variable.varValue}')
print('\n')

if (LpStatus[LP_Prob.status] == 'Optimal') :
    print(f'Optimal Value : Z = {value(LP_Prob.objective)}')
else :
    print(f'No Optimal Value. Status Code : {value(LP_Prob.objective)}')


# %%
### Risk/Return Parameter of 0


# %%
mu = 0

expected_investment_returns = lpSum([mu * mean_returns[j] * decision_variables_investment[j] for j in investments])
monthly_deviation = lpSum([decision_variables_deviation[t] for t in range(1, T + 1)])/T

# The Objective Function is Added to 'LP_Prob' First.
LP_Prob += expected_investment_returns - monthly_deviation, 'Maximize_Portfolio_Returns'


# %%
print(LP_Prob)


# %%
LP_Prob.writeLP('NewPortfolioProblemParameter0.lp')


# %%
# The Problem is Solved Using PuLP's Choice of Solver.
LP_Prob.solve()


# %%
print(f'Status: {LpStatus[LP_Prob.status]} \n')

for j, decision_variable in decision_variables_investment.items() :
    print(f'{decision_variable.name} = {decision_variable.varValue}')
print('\n')

if (LpStatus[LP_Prob.status] == 'Optimal') :
    print(f'Optimal Value : Z = {value(LP_Prob.objective)}')
else :
    print(f'No Optimal Value. Status Code : {value(LP_Prob.objective)}')
