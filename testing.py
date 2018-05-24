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

		if(min_path == current_pathweight):
			if nodes < nodes[::-1]:
				ans.append([1] + copy.deepcopy(nodes) + [1])
			else:
				ans.append([1] + copy.deepcopy(nodes[::-1]) + [1])

        	#print "smaller value found at"
        	#print nodes
        #update minimum
		if(min_path > current_pathweight):
			ans = []
			min_path = current_pathweight
			if nodes < nodes[::-1]:
				ans.append([1] + copy.deepcopy(nodes) + [1])
			else:
				ans.append([1] + copy.deepcopy(nodes[::-1]) + [1])
			#print "smaller value found at"
			#print nodes 
		nodes = next_permutation(nodes)
    #removing duplicates
	ans.sort()
	for index in reversed(range(1,len(ans))):
		if ans[index] == ans[index - 1]:
			del ans[index]
	return min_path, ans

def visualize(G,graph_pos,node_color='red', node_alpha=0.3,
               node_text_size=12,
               edge_color='blue', edge_alpha=0.3, edge_tickness=1,
               edge_text_pos=0.3,
               text_font='sans-serif'):
    nx.draw_networkx_nodes(G,graph_pos,alpha=node_alpha, node_color=node_color)
    nx.draw_networkx_edges(G,graph_pos,width=edge_tickness,alpha=edge_alpha,edge_color=edge_color,arrows=True)
   

def tryit(G,n,nodes):
	#initializeing for base case 
	list_ans=[[1,2,3,1]]
	list_newans = []
	distance = G.edge[1][2]['cost'] + G.edge[2][3]['cost'] + G.edge[3][1]['cost']
	for i in range(4,len(nodes)+2):
		minimum_triangle = n*1000 #cost of adding 
		list_newans = copy.deepcopy(list_ans)
		for ans in list_ans:
			# for j in range(0,len(ans)-1):
			# 	triangle = -G.edge[ans[j]][ans[j+1]]['cost'] + G.edge[i][ans[j+1]]['cost'] + G.edge[i][ans[j]]['cost'];
			# 	if(triangle < minimum_triangle):
			# 		minimum_triangle = triangle
			# 		k = j 
			# distance += minimum_triangle
			# ans.insert(k+1,i)
			newans = copy.deepcopy(ans)
			for i1 in range(0,len(ans)-1):
				for i2 in range(i1+1,len(ans)):
					if ans[i1] == ans[i2]: #case 1 = 1 in [1,2,3,1]
						continue
					if(i1 + 1 == i2):
						triangle = -G.edge[ans[i1]][ans[i2]]['cost'] + G.edge[i][ans[i2]]['cost'] + G.edge[i][ans[i1]]['cost'];
					 	if(triangle == minimum_triangle):
					 		newans = copy.deepcopy(ans)
					 		newans.insert(i2,i)
					 		if(newans<newans[::-1]):
					 			list_newans.append(copy.deepcopy(newans)) 
					 		else:
					 			list_newans.append(copy.deepcopy(newans[::-1]))
					 		#print "running triangle"
					 		#print ans,list_newans

					 	if(triangle < minimum_triangle):
					 		list_newans = []
					 		minimum_triangle = triangle
					 		newans = copy.deepcopy(ans)
					 		newans.insert(i2,i)
					 		if(newans<newans[::-1]):
					 			list_newans.append(copy.deepcopy(newans)) 
					 		else:
					 			list_newans.append(copy.deepcopy(newans[::-1]))
					 		#print "running triangle"
					 		#print ans,list_newans
					else:
						cost = G.edge[ans[i1]][i]['cost'] + G.edge[ans[i2]][i]['cost'] - G.edge[ans[i1]][ans[i1+1]]['cost'] -G.edge[ans[i2]][ans[i2-1]]['cost'];
						if cost > minimum_triangle:
							continue
						tempans=ans[:i1+1] + [i] + ans[i2:] #[1,2,3,..i1] + [i] + [i2,...,1]

						for j in range(0,len(tempans)-1):
							triangle = -G.edge[tempans[j]][tempans[j+1]]['cost'] + G.edge[ans[i1+1]][tempans[j]]['cost'] + G.edge[ans[i2-1]][tempans[j+1]]['cost'];
					 		if(cost + triangle) == minimum_triangle:
					 			newans = tempans[:j+1] + ans[i1+1:i2] + tempans[j+1:]
					 			if(newans<newans[::-1]):
					 				list_newans.append(copy.deepcopy(newans)) 
					 			else:
					 				list_newans.append(copy.deepcopy(newans[::-1]))
					 			#print "running triangle 2"
					 			#print i1,i2,tempans,ans,list_newans
					 		if(cost + triangle) < minimum_triangle:
					 			list_newans = []
					 			minimum_triangle = cost + triangle;
					 			newans = tempans[:j+1] + ans[i1+1:i2] + tempans[j+1:]
					 			if(newans<newans[::-1]):
					 				list_newans.append(copy.deepcopy(newans)) 
					 			else:
					 				list_newans.append(copy.deepcopy(newans[::-1]))
					 			#print "running triangle 2"
					 			#print i1,i2,tempans,ans,list_newans
							
							triangle = -G.edge[tempans[j]][tempans[j+1]]['cost'] + G.edge[ans[i1+1]][tempans[j+1]]['cost'] + G.edge[ans[i2-1]][tempans[j]]['cost'];
					 		if(cost + triangle) == minimum_triangle:
					 			newans = tempans[:j+1] + ans[i2-1:i1:-1] + tempans[j+1:]
								if(newans<newans[::-1]):
						 			list_newans.append(copy.deepcopy(newans)) 
						 		else:
						 			list_newans.append(copy.deepcopy(newans[::-1]))
					 			#print "running triangle 3"
					 			#print i1,i2,tempans,ans,list_newans

					 		if(cost + triangle) < minimum_triangle:
					 			list_newans = []
					 			minimum_triangle = cost + triangle;
					 			newans = tempans[:j+1] + ans[i2-1:i1:-1] + tempans[j+1:]
						 		if(newans<newans[::-1]):
					 				list_newans.append(copy.deepcopy(newans)) 
					 			else:
					 				list_newans.append(copy.deepcopy(newans[::-1]))
					 			#print "running triangle 3"
					 			#print i1,i2,tempans,ans,list_newans

						if (i1!= 0 and i2 < len(ans)-2): #if i2 = len-2 there is no point between i1 & i2
					 		cost = G.edge[ans[i1]][i]['cost'] + G.edge[ans[i2]][i]['cost'] -G.edge[ans[i1]][ans[i1-1]]['cost'] -G.edge[ans[i2]][ans[i2+1]]['cost']
							if cost > minimum_triangle:
								continue
							tempans =ans[i1:i2+1] + [i] # [i1,,,,i2] 
							for j in range(0,len(tempans)-2):
								triangle = -G.edge[tempans[j]][tempans[j+1]]['cost'] + G.edge[ans[i1-1]][tempans[j]]['cost'] + G.edge[ans[i2+1]][tempans[j+1]]['cost'];
					 			if(cost + triangle) == minimum_triangle:
					 				newans = ans[:i1] + tempans[j::-1] + tempans[:j:-1] + ans[i2+1:] 
					 				if(newans<newans[::-1]):
					 					list_newans.append(copy.deepcopy(newans)) 
							 		else:
							 			list_newans.append(copy.deepcopy(newans[::-1]))
							 		#print "running triangle 4"
					 				#print i1,i2,tempans,ans,list_newans
								
					 			if(cost + triangle) < minimum_triangle:
					 				list_newans = []
					 				minimum_triangle = cost + triangle;
					 				newans = ans[:i1] + tempans[j::-1] + tempans[:j:-1] + ans[i2+1:] 
					 				if(newans<newans[::-1]):
							 			list_newans.append(copy.deepcopy(newans)) 
							 		else:
							 			list_newans.append(copy.deepcopy(newans[::-1]))
							 		#print "running triangle 4"
					 				#print i1,i2,tempans,ans,list_newans
								
								triangle = -G.edge[tempans[j]][tempans[j+1]]['cost'] + G.edge[ans[i1-1]][tempans[j+1]]['cost'] + G.edge[ans[i2+1]][tempans[j]]['cost'];
					 			if(cost + triangle) == minimum_triangle:
					 				newans = ans[:i1] + tempans[j+1:] + tempans[:j+1] + ans[i2+1:]
					 				if(newans<newans[::-1]):
							 			list_newans.append(copy.deepcopy(newans)) 
							 		else:
							 			list_newans.append(copy.deepcopy(newans[::-1]))
							 		#print "running triangle 5"
						 			#print i1,i2,tempans,ans,list_newans

					 			if(cost + triangle) < minimum_triangle:
					 				list_newans = []
					 				minimum_triangle = cost + triangle;
					 				newans = ans[:i1] + tempans[j+1:] + tempans[:j+1] + ans[i2+1:]
					 				if(newans<newans[::-1]):
							 			list_newans.append(copy.deepcopy(newans)) 
							 		else:
							 			list_newans.append(copy.deepcopy(newans[::-1]))
							 		#print "running triangle 5"
						 			#print i1,i2,tempans,ans,list_newans

		distance += minimum_triangle
		#removing duplicates
		list_newans.sort()
		for index in reversed(range(1,len(list_newans))):
			if list_newans[index] == list_newans[index - 1]:
				del list_newans[index]
		list_ans = list_newans
		#print "adding node" + str(i) 
		#print list_ans
	return distance, list_ans


"""
	main code from here
"""
z = 0 
while z < 100:
	z+=1

	#enabling interactive mode in pylab
	# pylab.ion()                                 
	#function to display and keep the image on screen till refreshing
	# pylab.show()

	G=nx.Graph()

	n = randint(6,11) #int(raw_input("enter the number of nodes")); #
	print str(z) +" " +  str(n) 
	#storing the start time 
	start_time = time.time()
	nodes=[int(a) for a in range(2,n+1)]
	# count=0;
	# while(len(nodes)):
	# 	#print nodes;
	# 	nodes = next_permutation(nodes);
	# 	count+=1;
	# #print "hurray"
	# #print count;
	# exit()
	g = []
	#g =[]
	for i in range(1,n+1):
	    weights =[]
	    for j in range(1,i):
	    	weight = G.edge[i][j]['cost']
	    	weights.append(weight)
	    for j in range(i,n+1):
	        weight = randint(400,500) #g[i-1][j-1] #
	        G.add_edge(i,j,{'cost' : weight })
	        weights.append(weight)
	    #print weights
	    g.append(weights)
	#print g
	# graph_pos=nx.circular_layout(G)
	# visualize(G,graph_pos)
	# pylab.draw()
	# plt.pause(0.01)
	#print "Time of Program " + str(time.time()-start_time)
	# plt.pause(1)
	#storing the start time 
	start_time = time.time()
	# plt.clf()

	distance1,path1 = travllingSalesmanProblem(G,n,nodes)
	# Gtsp=nx.Graph()
	#path = [1] + path + [1]
	# for i in range(0,len(path)-1):
	# 	Gtsp.add_edge(path[i],path[i+1]);
	# visualize(Gtsp,graph_pos)
	# pylab.draw()
	t1 = str(time.time()-start_time)
	# plt.pause(5)
	# plt.clf()

	#storing the start time 
	start_time = time.time()
	distance2,path2 = tryit(G,n,nodes)
	# Gnew=nx.Graph()
	# for i in range(0,len(path)-1):
	# 	Gnew.add_edge(path[i],path[i+1]);
	# visualize(Gnew,graph_pos)
	t2 = str(time.time()-start_time)
	# pylab.draw()
	# plt.pause(5)
	del G
	if(path1 != path2):
			print "#######################################################"
			for p in g:
				print p
			print "number of nodes : " + str(n)
			print "naive solution:"
			print "Done"
			print path1;
			print distance1
			print "Time of Program " + t1
			print "my solution:"
			print "Done"
			print path2;
			print distance2
			print "Time of Program " + t2 
			print "#######################################################"


