import networkx as nx
import matplotlib.pyplot as plt
import pylab
from random import *
import time
import copy

def next_permutation(s):
  for i in reversed(xrange(len(s))):
    if s[i] > s[i-1]:
      break
  if i == 0:
  	return [];
  i -= 1
  for j in reversed(xrange(i + 1, len(s))):
    if s[j] > s[i]: break
  t = s[i]
  s[i] = s[j]
  s[j] = t
  s[i + 1:] = reversed(s[i + 1:])
  return s

def travllingSalesmanProblem(G,n,nodes):
    # store all vertex apart from source vertex
    # store minimum weight Hamiltonian Cycle.
    min_path = n*1000;
    ans = []
    while(len(nodes) > 0):
 
        # store current Path weight(cost)
        current_pathweight = 0;
         
        #compute current path weight
        current_pathweight += G.edge[nodes[0]][1]['cost'];
        for i in  range(0,len(nodes)-1):
            current_pathweight += G.edge[nodes[i]][nodes[i+1]]['cost'];
        current_pathweight += G.edge[nodes[-1]][1]['cost'];
 
        #update minimum
        if(min_path > current_pathweight):
        	min_path = current_pathweight
        	ans = copy.deepcopy(nodes)
        nodes = next_permutation(nodes)
    return min_path,ans;

 
def visualize(G,graph_pos,node_color='red', node_alpha=0.3,
               node_text_size=12,
               edge_color='blue', edge_alpha=0.3, edge_tickness=1,
               edge_text_pos=0.3,
               text_font='sans-serif'):
    nx.draw_networkx_nodes(G,graph_pos,alpha=node_alpha, node_color=node_color)
    nx.draw_networkx_edges(G,graph_pos,width=edge_tickness,alpha=edge_alpha,edge_color=edge_color,arrows=True)
   

def tryit(G,n,nodes):
	#initializeing for base case 
	ans=[1,2,3,1]
	distance = G.edge[1][2]['cost'] + G.edge[2][3]['cost'] + G.edge[3][1]['cost']
	for i in range(4,len(nodes)+2):
		minimum_triangle = n*1000
		for j in range(0,len(ans)-1):
			triangle = -G.edge[ans[j]][ans[j+1]]['cost'] + G.edge[i][ans[j+1]]['cost'] + G.edge[i][ans[j]]['cost'];
			if(triangle < minimum_triangle):
				minimum_triangle = triangle
				k = j 
		distance += minimum_triangle
		ans.insert(k+1,i)	
	return distance, ans 
#enabling interactive mode in pylab
pylab.ion()                                 
#function to display and keep the image on screen till refreshing
pylab.show()
G=nx.Graph()
n = int(raw_input("enter the number of nodes"));

#storing the start time 
start_time = time.time()

nodes=[int(a) for a in range(2,n+1)]
# count=0;
# while(len(nodes)):
# 	print nodes;
# 	nodes = next_permutation(nodes);
# 	count+=1;
# print "hurray"
# print count;
# exit()
g = [ [468, 479, 421, 475, 433, 412],
	[479, 428, 409, 471, 403, 465],
	[421, 409, 456, 425, 492, 486],
	[475, 471, 425, 404, 490, 420]]
	#[433, 403, 492, 490, 481, 488] ]

G.add_nodes_from(nodes)
G.add_nodes_from([1])
for i in range(1,n+1):
    weights =[]
    for j in range(1,i):
    	weight = G.edge[i][j]['cost']
    	weights.append(weight)
    for j in range(i,n+1):
        weight =randint(400,500)
        G.add_edge(i,j,{'cost' : g[i-1][j-1]}) #weight })
        weights.append(g[i-1][j-1])
    print weights
graph_pos=nx.circular_layout(G)
visualize(G,graph_pos)
pylab.draw()
plt.pause(0.01)
print "Time of Program " + str(time.time()-start_time)
plt.pause(1)
#storing the start time 
start_time = time.time()
plt.clf()

print "naive solution:"
distance,path = travllingSalesmanProblem(G,n,nodes)
Gtsp=nx.Graph()
Gtsp.add_edge(1,path[0])
for i in range(0,len(path)-1):
	Gtsp.add_edge(path[i],path[i+1]);
Gtsp.add_edge(path[-1],1)
visualize(Gtsp,graph_pos)
pylab.draw()
print "Done"
print path;
print distance
print "Time of Program " + str(time.time()-start_time)
plt.pause(5)
plt.clf()

#storing the start time 
start_time = time.time()
print "my solution:"
distance,path = tryit(G,n,nodes)
Gnew=nx.Graph()
for i in range(0,len(path)-1):
	Gnew.add_edge(path[i],path[i+1]);
visualize(Gnew,graph_pos)
print "Done"
print path;
print distance
print "Time of Program " + str(time.time()-start_time)
pylab.draw()
plt.pause(5)

