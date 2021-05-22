# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# # Example
# %% [markdown]
# Most of the following is copied from
# https://github.com/benalexkeen/Introduction-to-linear-programming/blob/master/Introduction%20to%20Linear%20Programming%20with%20Python%20-%20Part%202.ipynb
# %% [markdown]
# # LP Problem
#
# Maximize  $3 x + 5 y +5$
#
# Subject to
#
# $2  x + 3 y \le 12$
#
# $-x + y <= 3$
#
# $x \le 4$
#
# $y \le 3$
#
# $2  y \le 25 - x$
#
# $4  y \ge 2  x - 8$
#
# $y \le 2  x - 5$
#
# and  $x, y\ge 0$
# %% [markdown]
# We import pulp, in the following two cells.

# %%
import sys
get_ipython().system('{sys.executable} -m pip install pulp ')


# %%
import pulp

# %% [markdown]
# To use the PuLP package, do the previous steps first before proceeding.
#
# After installing PuLP, we can set up our problem to solve. First, we define it.

# %%
# Create a LP Minimization problem.
Lp_prob = pulp.LpProblem('Your_LP_Problem', pulp.LpMaximize)
# We set up the problem using the command LpProblem in the PuLP package.

# %% [markdown]
# `#` makes the righthand side a commment, which doesn't run as code.
#
# pulp.LpProblme <-- pulp is the package, `pulp.LpProblem` means we are using the class `LpProblem` in the pulp package.
#
# For minimization problems, use `pulp.LpMinimize`.
#
# Here, `Your_LP_Problem` is the name of the problem which shows up when we display the problem. We used `_` as spaces are not permitted in the name.

# %%
# Create problem decision variables.

# Create a variable x >= 0.  "x" means we put `x' when printing this variable.
x = pulp.LpVariable("x")
# Create a variable y >= 0.
y = pulp.LpVariable("y")

# %% [markdown]
# We used the `LpVariable` class.
#
# Lower and Upper bounds can be assigned using the 'lowBound' and 'upBound' parameter instead.
#
# For example, `x = pulp.LpVariable("x", lowBound = 0)` creates a variable x >= 0 and `y = pulp.LpVariable("y", upBound = 10)` creates a variable y <= 10.
# %% [markdown]
# We now set up our LP problem.

# %%
# Objective Function
Lp_prob += 3 * x + 5 * y +5

# We put objective function first then constraints.

# Constraints:
Lp_prob += 2 * x + 3 * y <= 12
Lp_prob += -x + y <= 3
Lp_prob += x <= 4
Lp_prob += y <= 3
Lp_prob += 2 * y <= 25 - x
Lp_prob += 4 * y >= 2 * x - 8
Lp_prob += y <= 2 * x - 5
Lp_prob += x >= 0
Lp_prob += y >= 0

# %% [markdown]
# The objective function and constraints are added using the += operator to our model.
# The objective function is added first, then the individual constraints.

# %%
# Display the problem
print(Lp_prob)

# %% [markdown]
# You realize that the inequalities are rearranged to put numbers only in the right hand side.
# %% [markdown]
# We can solve this LP using the `solve` function. `Lp_prob.solve` means apply the `solve` function to the `Lp_prob` object we defined.

# %%
Lp_prob.solve()
pulp.LpStatus[Lp_prob.status]

# %% [markdown]
# It solved the LP problem and gave the result:
# There are 5 status codes:
#
# - Not Solved: Status prior to solving the problem.
# - Optimal: An optimal solution has been found.
# - Infeasible: There are no feasible solutions.
# - Unbounded: The constraints are not bounded, maximising the solution will tend towards infinity.
# - Undefined: The optimal solution may exist but may not have been found.
#
#
# %% [markdown]
# We can now view our optimal variable values and the optimal value of Z.

# %%
# Printing the final solution
print("x=", pulp.value(x), "y=", pulp.value(y), "z=", pulp.value(Lp_prob.objective))

# %% [markdown]
# Another way to show the solutions:

# %%
for variable in Lp_prob.variables():
        print(variable.name, "=", variable.varValue)
print("Optimal value is z = ", pulp.value(Lp_prob.objective))
