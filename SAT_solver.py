import sys
from copy import deepcopy
def solve(cnf,literals):
    new_t=[]
    while len(cnf)>0:
        unit_cl = [i[0] for i in cnf if len(i)==1]
        if len(unit_cl)==0:
            break
        for unit in unit_cl:
            model.append(unit)
            new_t.append(unit)
            i=0
            while i<len(cnf):
                if unit in cnf[i]:
                    cnf.remove(cnf[i])
                    i-=1
                elif -1*unit in cnf[i]:
                    cnf[i].remove(-1*unit)
                i+=1
        if sum(len(clause)==0 for clause in cnf):
            for i in new_t:
                model.remove(i)
            return False
    if len(cnf)==0:
        return True
    literals = [i for j in cnf for i in j]
    literals = list(set(literals))
    x = literals[0]
    if solve(deepcopy(cnf)+[[x]], deepcopy(literals)):
        return True
    elif solve(deepcopy(cnf)+[[-1*x]], deepcopy(literals)):
        return True
    else:
        for i in new_t:
            model.remove(i)
        return False

def dpll():
    cnf = []
    literals = []
    with open(sys.argv[1]) as f:
        for line in f:
            if line[0]=='p':
                n_var = int(line.split()[2])
            elif line[0]!='c':
                t = [int(i) for i in line.split() if i!='0']
                t = sorted(t)
                cnf.append(t)
                literals+=t
    literals  = list(set(literals))
    
    if solve(cnf, literals):
        print('SATISFIABLE')
        for i in range(1,n_var+1):
            if i in model:
                print(i)
            else:
                print(-1*i)
    else:
        print('UNSATISFIABLE')
        
model = []
dpll()