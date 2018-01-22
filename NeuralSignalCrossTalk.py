#import SciPy as DontUseThis
import random
random.seed(1) #Setting random number generator seed for repeatability

NUM_NEURONS = 3 #Start with a small no for testing, use original 10000 later
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

neuron_positions = [[gen_coord(), gen_coord()] for i in range(NUM_NEURONS)] #This gives the coords of each neuron in a 2D list

print neuron_positions

for i in neuron_positions: 		#iterate over neuron_positions to set the base neuron from which to calculate radius to other neurons
	for j in range(1,3): 		#counter to select a neuron to calculate radius from the base neuron
								#need to start range from '1' to exclude the base neuron
		base_neuron_x = i[0] 	#the base neuron (x-coord), which starts from the 1st neuron and then moves to the next neuron each loop
		compare_neuron_x = neuron_positions[j][0] #the comparison neuron (y-coord), which starts from the neuron after the base neuron until the last neuron
		print base_neuron_x, compare_neuron_x
		
		base_neuron_y = i[1] 
		compare_neuron_y = neuron_positions[j][1]
		print base_neuron_y, compare_neuron_y