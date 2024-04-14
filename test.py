import numpy as np
import matplotlib.pyplot as plt

def cluster(L, p):
    net = np.zeros((L,L))
    for i in range(L):
        for j in range(L):
            r = np.random.uniform(0,1)
            if r < p:
                net[i,j] = 1
            else:
                net[i,j] = 0
    k = 2
    #M_k = {1:1}
    for i in range(L):
        for j in range(L):
            if int(net[i,j]):        
                if j > 0:
                    left = net[i, j - 1] 
                else:
                    left = 0
                if i > 0:
                    top = net[i-1, j]
                else:
                    top = 0
                if left == 0 and top == 0:
                    net[i,j] = k
                    #M_k[k] = 1
                    k += 1
                elif left != 0 and top == 0:
                    net[i,j] = left
                    #M_k[int(left)] +=  1
                elif top != 0 and left == 0:
                    net[i,j] = top
                    #M_k[int(top)] +=  1
                else:
                    #M_k[int(left)] += M_k[int(net[i,j])] + 1
                    net= find_and_replace(net, i, j, top, left)
                    net[i,j] = left
    unique, counts = np.unique(net, return_counts=True)
    dict_ = dict(zip(unique, counts))
    clusters_count = []
    for key in dict_:
        if key != 0:
            clusters_count.append(dict_[key])
    return net, clusters_count

def find_and_replace(label, i, j, above, left):
    row, col = np.where(label == above)
    for r, c in zip(row, col):
        label[r, c] = left
        #M_k[int(label[r, c])] = M_k[int(above)]
    return label

net, counts = cluster(5, 0.6)
print(counts)
plt.imshow(net)
plt.colorbar()
plt.show()
            




