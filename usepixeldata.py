#import everything you need
import json
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")

#print statements
print("*")
print("*==============================*")
print("* BEGINNING SORTING ALGORITHM *")
print("*==============================*")
print '\n'

#open relevant JSON files and load them into defined variables
kf = open("tmp/pixels.json", "r")
ke = json.load(kf)
kf.close()

kg = open("tmp/klusters.json", "r")
kh = json.load(kg)
kg.close()

#define empty lists you will need for the sorting algorithm below
ID = []
size = []
edgepixels = []
width = []
height = []
linearity = []
density = []
counts = []
m = []
residuals = []
radius = []


#iterate over ke and kh to extract relevant information
#you can either append the information to an empty list or print them
'''
for k in ke:
	print k['ID']
	print k['size']

'''

for k in kh:
	ID.append(k['id'])
	size.append(k['size'])
	edgepixels.append(k['n_edgepixels'])
	width.append(k['width'])
	height.append(k['height'])
	linearity.append(k['lin_linearity'])
	density.append(k['density_uw'])
	counts.append(k['totalcounts'])
	m.append(k['lin_m'])
	residuals.append(k['lin_sumofres'])
	radius.append(k['radius_uw'])


#sorting algorithm starts here

#initialize cluster types
slugs=0
loopers=0
branchers=0
crossovers=0
straight_wiggly=0
boxy=0

for i in range(len(edgepixels)):
	if size[i] > 19:
		if density[i] > 0.1:
			if edgepixels[i] != size[i]:
				if width[i]/height[i] > 1.3 or width[i]/height[i] < 0.7:
					slugs+=1
					print 'slug - ' + ID[i]
				else:
					boxy+=1
					print 'boxy - ' + ID[i]
			else:
				if counts[i] > 450 and m[i] > 0:
					loopers+=1
					print 'looper - ' + ID[i]
		else:
			if size[i] > 100:
				if m[i] > 0 and counts[i] > 1800 and linearity[i]>1:
					branchers+=1
					print 'brancher - ' + ID[i]
				else:
					if residuals[i] > 150 and counts[i] > 1800:
						crossovers+=1
						print 'crossover - ' + ID[i]
					else:
						if counts[i] > 2800 and radius[i] > 45:
							straight_wiggly+=1
							print 'straight-wiggly - ' + ID[i]





#create a bar graph for data visualisation
'''
#initialize graph
graph = []

objects = (1,2,3,4,5,6)
y_pos = np.arange(len(objects))

graph.append(slugs)
graph.append(loopers)
graph.append(straight_wiggly)
graph.append(branchers)
graph.append(boxy)
graph.append(crossovers)

graphdata = [slugs, loopers,straight_wiggly,branchers, boxy, crossovers]

fig = plt.figure()
ax = plt.subplot2grid((4,4),(1,0), rowspan=3, colspan=4)
ax.set_ylabel('Frequency')
ax.set_title('Frequency of Clusters')
ax.set_xticklabels('slugs', 'loopers', 'straight-wiggly','branchers', 'boxy', 'crossovers')
ax.bar(objects,graphY)
plt.show()
'''

#print the frequency of each cluster type
print("slugs: '%d '" % (slugs))
print("loopers: '%d '" % (loopers))
print("straight-wiggly: '%d '" % (straight_wiggly))
print("branchers: '%d '" % (branchers))
print("boxy: '%d '" % (boxy))
print("crossovers: '%d '" % (crossovers))
