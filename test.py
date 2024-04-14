import numpy as np
L = 16
p = 0.5
net = np.zeros((L,L))
for i in range(L):
    for j in range(L):
        r = np.random.uniform(0,1)
        if r < p:
            net[i,j] = 1
        else:
            net[i,j] = 0
t = 2
for i in range(L):
    if net[0, i] == 1:
        net[0,i] = 2
any_neigbhours = True
last_row_reached = False
while any_neigbhours and not(last_row_reached):
    neigbours = 0
    for i in range(L):
        for j in range(L):
            if net[i,j] == t:
                if i - 1 >= 0:
                    if net[i - 1, j] == 1:
                        net[i - 1, j] = t + 1
                        neigbours += 1
                if i + 1 < L:
                    if net[i + 1, j] == 1:
                        net[i + 1, j] = t + 1
                        neigbours += 1
                if j - 1 >= 0:
                    if net[i, j - 1] == 1:
                        net[i, j - 1] = t + 1
                        neigbours += 1
                if j + 1 < L:
                    if net[i, j + 1] == 1:
                        net[i, j + 1] = t + 1
                        neigbours += 1
    for i in range(L):
        if t > 2:
            if net[L-1, i] == t-1:
                last_row_reached = True
    if neigbours == 0:
        any_neigbhours = False
    t += 1
if last_row_reached:
    print("Istnieje ścieżka łącząca pierwszy i ostatni rząd")
else:
    print("Nie istnieje ścieżka łącząca pierwszy i ostatni rząd")
print(net)
    
