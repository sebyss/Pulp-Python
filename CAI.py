from pulp import*

prob = LpProblem('Maximul de cai fara sa se atace', LpMaximize)
n = 8
tabla = [(k,x)for k in range(n) for x in range(n)]
mutari = [(-2,-1), (-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2)] # toate directile in care poate merge calul 

cal = LpVariable.dicts("Cal",(tabla),0,1,LpBinary)
poz = LpVariable.dicts("poz",(tabla),0,1,LpBinary)

prob += sum( poz[i] for i in tabla )

for i in tabla:
    for m in mutari:
        x = (i[0] + m[0], i[1] + m[1])
        if x in tabla:
            prob += (( cal[i] ) + poz[x]) <= 1 
        
for j in tabla:
    prob += poz[j] - cal[j] <= 0
  
prob.solve()
print(prob)
print ("Status:", LpStatus[prob.status])

print("x = cal")
print("0 = pozitie goala")
print('')
print ("Maxim =", value(prob.objective), "de cai ")
print('')
for i in range(n):
  for j in range(n):
    pv = "0"
    if cal[(j,i)].varValue == 1: #0 -> caii sunt afisati pe culoarea neagra
      pv = "X"                   #1 -> caii sunt afisati pe culoarea alba
    print (pv,end=' '),
  print('')





