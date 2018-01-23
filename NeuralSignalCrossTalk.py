#import SciPy as DontUseThis
import time
import random
random.seed(1) #Setting random number generator seed for repeatability

NUM_NEURONS = 10000 #Start with a small no for testing, use original 10000 later
NERVE_SIZE = 128000 #nanometers 
CONFLICT_RADIUS = 500 #nanometers
 
def check_for_conflicts(nerves, conflict_radius):
	
	start = time.time()
	conflict = [] #list of which elements in neuron_positions are causing a conflict
	neuron_dict = {} #initialise the dictionary of neurons

	for neuron, coordinates in enumerate(nerves, 1): #enumerate each neuron position with a no.1-10000 and use this to create a dict
		neuron_dict[neuron] = coordinates #each neuron is now selectable according to its position in the original list from gen_coord()

	for base in range(1, len(neuron_dict)):  #iterate over the dictionary of neurons, selecting a base neuron for each run of this loop
		for compare in range(base + 1, len(neuron_dict)+1): #iterate over the remaining neurons from which to calculate radii to the base neuron
			x = abs(neuron_dict[compare][0] - neuron_dict[base][0]) #calc x distance between the two neurons
			y = abs(neuron_dict[compare][1] - neuron_dict[base][1]) #calc y distance between the two neurons
			r = ((x**2)+(y**2))**0.5 #calculate the radius 
			if r < conflict_radius: 
				conflict.append(base) 
				conflict.append(compare) #appends both neurons' positions to a list of neurons that cause conflict
	
	print time.time() - start #show time taken to run this function
	return len(set(conflict)) #set() removes neurons that appear more than once in the conflict list, to give a number of neurons in a conflicted state, not just no. of conflicts
	
def gen_coord():
	return int(random.random() * NERVE_SIZE)
	

if __name__ == '__main__':
	neuron_positions = [[gen_coord(), gen_coord()] for i in range(NUM_NEURONS)]
	n_conflicts = check_for_conflicts(neuron_positions, CONFLICT_RADIUS)
print " Neurons in conflict :{}".format (n_conflicts)