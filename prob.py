import random

#Number of simulations1
T = 20000

#Number of servers to be simulated
N = [10,15,20,25,30,35,40,45,50]

#Propagation rates to be simulated
G = [7,8,9,10]

#init

def propagate(servers,server,n,g):
    if(server not in visited):
        visited.append(server)
        gossip = random.sample(servers[0:server] + servers[server + 1:n],k=g)
        for s in gossip:
            propagate(servers,s,n,g)

for g in G:
    for n in N:
        p = 0
        servers = []
        for s in range(n):
            servers.append(s)
        for i in range(T):
            visited = []
            propagate(servers,0,n,g)
            if len(visited) == len(servers):
                p += 1
        #prints the success ratio
        #for each sample of variables to be simulated
        print(str(n) + "," + str(g) + " -> " + str(p/T))