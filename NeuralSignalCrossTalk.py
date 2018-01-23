#import SciPy as DontUseThis
import time
import random
random.seed(1) #Setting random number generator seed for repeatability

NUM_NEURONS = 10000 #Start with a small no for testing, use original 10000 later
NERVE_SIZE = 128000 #nanometers 
CONFLICT_RADIUS = 500 #nanometers
 
def check_for_conflicts(nerves, conflict_radius):
	
	start = time.time() #set start time of code
	k = 1 #need a second counter to shift the comparison neurons start point across by 1 to avoid overlap with the base neuron when restarting the loop
	      #see later in the code for how it is used
	conflict = [] #list of which elements in neuron_positions are causing a conflict

	for i in nerves: #iterate over neuron_positions to set the base neuron from which to calculate radius to other neurons
		for j in xrange(k, NUM_NEURONS): #selects neurons from 1 after the base neuron to the end of the neuron_positions list to compare with the base neuron
			radius = (((abs(neuron_positions[j][0] - i[0])) ** 2) + ((abs(neuron_positions[j][1] - i[1])) ** 2)) ** 0.5 #calculate the radius between the base neuron and the comparison neuron
			if radius < conflict_radius: 
				conflict.append(k-1) #appends the base neuron's position in the neuron_positions list to the conflict list
				conflict.append(k) #appends the comparison neuron's position in the neuron_positions list to the conflict list
		k += 1
	
	conflict = set(conflict) #removes any repeated neurons, as we already know they are in a conflicted state if they already appear in the list
	print time.time()-start #shows time taken for code to run
	return len(conflict)