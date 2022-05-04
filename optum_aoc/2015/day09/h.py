import pulp
from pulp import *
import pandas as pd
import numpy as np
import time

tic = time.time()

# create Instructions matrix with distances to and from each city
raw_data = open("input.txt")
data = raw_data.read()
data = pd.Series([x for x in data.strip().splitlines() if x])
Instructions = data.str.split(r" ", expand=True)
Instructions.columns = ["City1","to", "City2","=","Distance"]
Instructions2 = pd.DataFrame(Instructions, columns= ["City2","to", "City1","=","Distance"])
Instructions2.columns = ["City1","to", "City2","=","Distance"]
Instructions_merge = pd.concat([Instructions, Instructions2])
cols_names = ['City1', 'City2', 'Distance']
Instructions_merge = Instructions_merge[cols_names]
Instructions_merge['Distance'] = pd.to_numeric(Instructions_merge['Distance'], errors='coerce')
Instructions_pivot = Instructions_merge.pivot(index='City1', columns='City2', values='Distance')
cols = Instructions_pivot.columns

# cheap way of ensuring that the LP never goes to and from the same city
Instructions_pivot[cols]=Instructions_pivot[cols].fillna(10000)
Instructions_array = Instructions_pivot.values
print(Instructions_array)

# input for constraints
n_start_cities = Instructions_array.shape[1]
n_destination_cities = Instructions_array.shape[0]
num_total_trips = Instructions_array.shape[1]-1
destinations_per_city = 1
starts_per_city = 1


model = LpProblem("minimize_travel", LpMinimize)

variable_names = [str(i)+str(j) for j in range(1, n_start_cities+1) for i in range(1,n_destination_cities+1)]
variable_names.sort()

DV_variables = LpVariable.matrix("X", variable_names , cat = "Integer" , lowBound= 0, upBound=1 )

allocation = np.array(DV_variables).reshape(Instructions_array.shape[0],Instructions_array.shape[1])

lpSum(allocation*Instructions_array)

obj_func = lpSum(allocation*Instructions_array)
model +=  obj_func
print()
print('Ojbective function: ')
print(obj_func)
print()
print('Ensure each city is only the starting point once (at most):')
print()
for i in range(n_destination_cities):
    print(lpSum(allocation[i][j] for j in range(n_destination_cities)) <= destinations_per_city)
    model += lpSum(allocation[i][j] for j in range(n_destination_cities)) <= destinations_per_city , "destinations_per_city_constraint" +str(i)
print()
print('Ensure each city is only visited once (at most):')
print()
for i in range(n_destination_cities):
    print(lpSum(allocation[j][i] for j in range(n_start_cities)) <= starts_per_city)
    model += lpSum(allocation[j][i] for j in range(n_start_cities)) <= starts_per_city , "starts_per_city_constraint" +str(i)
print()
print('Ensure each city is either a destination or starting point:')
print()
for i in range(n_destination_cities):
    print(lpSum(allocation[j][i] for j in range(n_start_cities)) + lpSum(allocation[i][j] for j in range(n_start_cities)) >= 1)
    model += lpSum(allocation[j][i] for j in range(n_start_cities)) + lpSum(allocation[i][j] for j in range(n_start_cities)) >= 1, "visit_each_city_constraint" +str(i)
print()
print('Ensure that there are exactly 7 trips:')
print()
print(lpSum(allocation[i] for i in range(n_start_cities)) == num_total_trips)
model += lpSum(allocation[i] for i in range(n_start_cities)) == num_total_trips , "total_trips_constraint" +str(i)
print()
model

model.writeLP("minimize_travel.lp")

model.solve()
# solvers.PULP_CBC_CMD(fracGap=0)
status =  LpStatus[model.status]


print("Total Distance:", model.objective.value())
# Decision Variables
final_matrix = []
for v in model.variables():
    try:
        final_matrix.append(v.value())
    except:
        print("error couldnt find value")
final_matrix = np.reshape(final_matrix,(Instructions_array.shape[0],Instructions_array.shape[1]))
print()
print("Final matrix:")
print(final_matrix)
print()
toc = time.time()
print("Part 1 time:" + str(1000*(toc-tic))+" ms")