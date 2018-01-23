#import SciPy as DontUseThis
import time
import random
random.seed(1) #Setting random number generator seed for repeatability

NUM_NEURONS = 10000 #Start with a small no for testing, use original 10000 later
NERVE_SIZE = 128000 #nanometers 
CONFLICT_RADIUS = 500 #nanometers
 
def check_for_conflicts(nerves, conflict_radius):
	raise NotImplementedError()

def gen_coord():
	return int(random.random() * NERVE_SIZE)
	
'''
if __name__ == '__main__':
	neuron_positions = [[gen_coord(), gen_coord()] for i in range(NUM_NEURONS)]
	n_conflicts = check_for_conflicts(neuron_positions, CONFLICT_RADIUS)
	print " Neurons in conflict :{}".format (n_conflicts)
'''

neuron_positions = [[gen_coord(), gen_coord()] for i in xrange(NUM_NEURONS)] #This gives the coords of each neuron in a 2D list

#print neuron_positions

start = time.time() #set start time of code

k = 1 #need a second counter to shift the comparison neurons start point across by 1 to avoid overlap with the base neuron when restarting the loop
	  #see later in the code for how it is used

conflict = [] #list of which elements in neuron_positions are causing a conflict

for i in neuron_positions: #iterate over neuron_positions to set the base neuron from which to calculate radius to other neurons

	for j in xrange(k, NUM_NEURONS): #selects neurons from 1 after the base neuron to the end of the neuron_positions list to compare with the base neuron
								    #using 'k' as explained above
								
		
		radius = (((abs(neuron_positions[j][0] - i[0])) ** 2) + ((abs(neuron_positions[j][1] - i[1])) ** 2)) ** 0.5 #calculate the radius between the base neuron and the comparison neuron
		
		if radius < 500: 
		
			conflict.append(k-1) #appends the base neuron's position in the neuron_positions list to the conflict list
			
			conflict.append(k) #appends the comparison neuron's position in the neuron_positions list to the conflict list
			
	k += 1
	

conflict = set(conflict) #removes any repeated neurons, as we already know they are in a conflicted state if they already appear in the list

print len(conflict)

print time.time()-start #shows time taken for code to run
