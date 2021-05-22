# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %%
import sys
get_ipython().system('{sys.executable} -m pip install pulp')


# %%
import pulp


# %%
# Create a LP maximization problem.
LP_prob = pulp.LpProblem('Your_LP_Problem', pulp.LpMaximize)


# %%
# Create Decision Variables.
x = pulp.LpVariable('x')
y = pulp.LpVariable('y')


# %%
# Add Objective Function to LP problem.
LP_prob += 3*x+5*y+5

# Then add Constraints.
LP_prob += 2*x+3*y <= 12
LP_prob += -x+y <= 3
LP_prob += x <= 4
LP_prob += y <= 3
LP_prob += 2*y <= 25-x
LP_prob += 4*y >= 2*x-8
LP_prob += y <= 2*x-5
LP_prob += x >= 0
LP_prob += y >= 0


# %%
# Display the LP problem.
print(LP_prob)


# %%
LP_prob.solve()
pulp.LpStatus[LP_prob.status]


# %%
print("x = ", pulp.value(x))
print("y = ", pulp.value(y))
print("z = ", pulp.value(LP_prob.objective))


# %%
for variable in LP_prob.variables() :
    print(variable.name, " = ", variable.varValue)
if (pulp.LpStatus[LP_prob.status] == 'Optimal') :
    print('Optimal Value : z = ', pulp.value(LP_prob.objective))
else :
    print('No Optimal Value. Status Code : ', pulp.value(LP_prob.objective))
