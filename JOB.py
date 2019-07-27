from pulp import *

Joburi = ['mic','mediu','mare']

timp = {'mic' : 1,
        'mediu': 3,
        'mare': 10}

castig = {'mic': 5,
          'mediu': 10,
          'mare': 50}

prob = LpProblem("Castig maxim",LpMaximize)
job_vars = LpVariable.dicts("Job",Joburi,0,10,LpInteger)

prob += lpSum([castig[i]*job_vars[i] for i in Joburi])
prob += lpSum([job_vars[i] * timp[i] for i in Joburi]) == 48

for i in Joburi:
    prob+=job_vars[i] <=10

prob.solve()
print ("Status:", LpStatus[prob.status])

for v in prob.variables():
    print (v.name, "=", v.varValue , "ori")
   
print ("Castig maxim = $", value(prob.objective))

# max z = 5x1 + 10x2 + 50x3
# subject to:
# 1x1 + 3x2 + 10x3 <= 48
# x1 <= 10
# x2 <= 10
# x3 <= 10

